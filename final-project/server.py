import http.server
from http import HTTPStatus
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import jinja2
import os
import json
from Seq1 import Seq


PORT = 8080
HTML_FOLDER = "html"
ENSEMBLE_SERVER = "rest.ensembl.org"
RESOURCE_TO_ENSEMBL_REQUEST = {
    '/listSpecies': {'resource': "/info/species", 'params': "content-type=application/json"},
    "/karyotype": {"resource": "/info/assembly/", 'params': "content-type=application/json"},
    "/chromosomeLength": {"resource": "/info/assembly/", 'params': "content-type=application/json"},
    "/geneSeq": {"resource": "/sequence/id/", 'params': "content-type=application/json"},
    "/geneInfo": {"resource": "/overlap/id/", 'params': "content-type=application/json"},
    "/geneCalc": {"resource": "/sequence/id/", 'params': "content-type=application/json"},
    "/geneList": {"resource": "/overlap/region/human/", 'params': "content-type=application/json"}
                 }
RESOURCE_NOT_AVAILABLE_ERROR = "Resource not available"
ENSEMBL_COMMUNICATION_ERROR = "Error in communication with the Ensembl server"



def read_html_template(file_name):
    file_path = os.path.join(HTML_FOLDER, file_name)
    contents = Path(file_path).read_text()
    contents = jinja2.Template(contents)
    return contents


def server_request(server, url):
    import http.client

    error = False
    data = None
    try:
        connection = http.client.HTTPSConnection(server)
        connection.request("GET", url)
        response = connection.getresponse()
        if response.status == HTTPStatus.OK:
            json_str = response.read().decode()
            data = json.loads(json_str)
        else:
            error = True
    except Exception:  # Comment
        error = True
    return error, data


def handle_error(endpoint, message):
    context = {
        'endpoint': endpoint,
        'message': message
    }
    return read_html_template("error.html").render(context=context)


def list_species(endpoint, parameters):
    request = RESOURCE_TO_ENSEMBL_REQUEST[endpoint]
    url = f"{request['resource']}?{request['params']}"
    error, data = server_request(ENSEMBLE_SERVER, url)
    if not error:
        limit = None
        if 'limit' in parameters:
            limit = int(parameters['limit'][0])
        species = data['species']  # list<dict>
        name_species = []
        for specie in species[:limit]:
            name_species.append(specie['display_name'])
        context = {
            'number_of_species': len(species),
            'limit': limit,
            'name_species': name_species
        }
        contents = read_html_template("species.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, ENSEMBL_COMMUNICATION_ERROR)
        code = HTTPStatus.SERVICE_UNAVAILABLE  # Comment
    return code, contents

def karyotype(endpoint, parameters):
    request = RESOURCE_TO_ENSEMBL_REQUEST[endpoint]
    specie = parameters["species"][0]
    url = f"{request['resource']}{specie}?{request['params']}"
    error, data = server_request(ENSEMBLE_SERVER, url)
    if not error:
        context = {"specie": specie,
                   "karyotype": data["karyotype"]
                   }
        contents = read_html_template("karyotype.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, ENSEMBL_COMMUNICATION_ERROR)
        code = HTTPStatus.SERVICE_UNAVAILABLE  # Comment
    return code, contents


def chromosome_length(endpoint, parameters):
    request = RESOURCE_TO_ENSEMBL_REQUEST[endpoint]
    specie = parameters["species"][0]
    chromosome = parameters["chromo"][0]
    url = f"{request['resource']}{specie}?{request['params']}"
    error, data = server_request(ENSEMBLE_SERVER, url)
    top = data["top_level_region"]
    for i in top:
        name = i["name"]
        if name == chromosome:
            length = i["length"]
            break

    if not error:
        context = {"specie": specie,
                   "length": length,
                   "number_chromosome": chromosome
                   }
        contents = read_html_template("chrom.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, ENSEMBL_COMMUNICATION_ERROR)
        code = HTTPStatus.SERVICE_UNAVAILABLE  # Comment
    return code, contents


def get_id(gene):
    url = f"/homology/symbol/human/{gene}?content-type=application/json"
    error, data = server_request(ENSEMBLE_SERVER, url)
    if not error:
        data = data["data"]
        for e in data:
            id = str(e["id"])
        print(id)
    return id


def geneSeq(endpoint, parameters):
    gene = parameters["gene"][0]
    id_2 = get_id(gene)
    if id_2:
        request = RESOURCE_TO_ENSEMBL_REQUEST[endpoint]
        url = f"{request['resource']}{id_2}?{request['params']}"
        error, data = server_request(ENSEMBLE_SERVER, url)
        seq = data["seq"]
        if not error:
            context = {"gene": gene,
                       "seq": seq
                       }
            contents = read_html_template("human_seq.html").render(context=context)
            code = HTTPStatus.OK
        else:
            contents = handle_error(endpoint, ENSEMBL_COMMUNICATION_ERROR)
            code = HTTPStatus.SERVICE_UNAVAILABLE  # Comment

    return code, contents

def geneInfo(endpoint, parameters):
    gene = parameters["gene"][0]
    id_2 = get_id(gene)
    request = RESOURCE_TO_ENSEMBL_REQUEST[endpoint]
    url = f"{request['resource']}{id_2}?feature=gene;{request['params']}"
    error, data = server_request(ENSEMBLE_SERVER, url)
    print(data)
    for i in data:
        start = i["start"]
        end = i["end"]
        name = i["assembly_name"]
    length = int(end) - int(start)
    if not error:
        context = {"name": name,
                   "start": start,
                   "end": end,
                   "length": length,
                   "id": id_2
                   }
        contents = read_html_template("geneInfo.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, ENSEMBL_COMMUNICATION_ERROR)
        code = HTTPStatus.SERVICE_UNAVAILABLE  # Comment
    return code, contents


def geneCalc(endpoint, parameters):
    gene = parameters["gene"][0]
    id_2 = get_id(gene)
    request = RESOURCE_TO_ENSEMBL_REQUEST[endpoint]
    url = f"{request['resource']}{id_2}?{request['params']}"
    error, data = server_request(ENSEMBLE_SERVER, url)
    seq = data["seq"]
    seq = Seq(seq)
    length = seq.len()
    e, percentage = seq.info()
    print(percentage)
    if not error:
        context = {"name": gene,
                   "length": length,
                   "percentage": percentage
                   }
        contents = read_html_template("geneCalc.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, ENSEMBL_COMMUNICATION_ERROR)
        code = HTTPStatus.SERVICE_UNAVAILABLE  # Comment
    return code, contents


def geneList(endpoint, parameters):
    chromo = parameters["chromo"][0]
    start = parameters["start"][0]
    end = parameters["end"][0]
    request = RESOURCE_TO_ENSEMBL_REQUEST[endpoint]
    url = f"{request['resource']}{chromo}:{start}-{end}?feature=gene;feature=transcript;feature=cds;feature=exon;{request['params']}"
    print(url)
    error, data = server_request(ENSEMBLE_SERVER, url)
    print(data)
    names = []
    for i in data:
        try:
            name = i["assembly_name"]
            names.append(name)
        except KeyError:
            pass

    print(names)
    if not error:
        context = {"names": names,
                   "chromosome_num": chromo
                   }
        contents = read_html_template("geneList.html").render(context=context)
        code = HTTPStatus.OK
    else:
        contents = handle_error(endpoint, ENSEMBL_COMMUNICATION_ERROR)
        code = HTTPStatus.SERVICE_UNAVAILABLE  # Comment
    return code, contents


socketserver.TCPServer.allow_reuse_address = True

class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        parsed_url = urlparse(self.path)
        endpoint = parsed_url.path  # resource or path
        print(f"Endpoint: {endpoint}")
        parameters = parse_qs(parsed_url.query)
        print(f"Parameters: {parameters}")
        url = f"{endpoint}?{parameters}"

        code = HTTPStatus.OK
        content_type = "text/html"
        contents = ""
        if endpoint == "/":
            file_path = os.path.join(HTML_FOLDER, "index.html")
            contents = Path(file_path).read_text()
        elif endpoint == "/listSpecies":
            code, contents = list_species(endpoint, parameters)
        elif endpoint == "/karyotype":
            code, contents = karyotype(endpoint, parameters)
        elif endpoint == "/chromosomeLength":
            code, contents = chromosome_length(endpoint, parameters)
        elif endpoint == "/geneSeq":
            code, contents = geneSeq(endpoint, parameters)
        elif endpoint == "/geneInfo":
            code, contents = geneInfo(endpoint, parameters)
        elif endpoint == "/geneCalc":
            code, contents = geneCalc(endpoint, parameters)
        elif endpoint == "/geneList":
            code, contents = geneList(endpoint, parameters)
        else:
            contents = handle_error(endpoint, RESOURCE_NOT_AVAILABLE_ERROR)
            code = HTTPStatus.NOT_FOUND

        self.send_response(code)
        contents_bytes = contents.encode()
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(contents_bytes)))
        self.end_headers()

        self.wfile.write(contents_bytes)


with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print("Serving at PORT...", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Stopped by the user")
        httpd.server_close()
