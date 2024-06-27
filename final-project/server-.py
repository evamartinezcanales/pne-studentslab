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


port = 8080
ensemble_server = "rest.ensembl.org"

def read_html_template(file_name):
    file_path = os.path.join("html", file_name)
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
    except Exception:
        error = True
    return error, data


def handle_error(endpoint, message, json_format=False):
    context = {
        'endpoint': endpoint,
        'message': message
    }

    code = HTTPStatus.NOT_FOUND
    if json_format:
        content_type = "application/json"
        contents = json.dumps(context)
    else:
        content_type = "text/html"
        contents = read_html_template("error.html").render(context=context)
    return code, content_type, contents

def is_json(parameters):
    try:
        json_param = parameters["json"][0]
        if json_param == "1":
            json_param = True
        else:
            json_param = False
    except KeyError:
        json_param = False
    return json_param

def content_ctype(html, parameters, context):
    _json = is_json(parameters)
    if _json:
        content_type = "application/json"
        contents = json.dumps(context)
    else:
        content_type = "text/html"
        contents = read_html_template(html).render(context=context)
    return content_type, contents


def get_id(gene):
    url = f"/homology/symbol/human/{gene}?content-type=application/json"
    error, data = server_request(ensemble_server, url)
    if not error:
        return next(str(e["id"]) for e in data["data"])
    return None


socketserver.TCPServer.allow_reuse_address = True

class Myhandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        parsed_url = urlparse(self.path)
        endpoint = parsed_url.path
        print(f"Endpoint: {endpoint}")
        parameters = parse_qs(parsed_url.query)
        print(f"Parameters: {parameters}")

        content_type = "text/html"
        code = HTTPStatus.OK

        if endpoint == "/":
            file_path = os.path.join("html", "index.html")
            code = HTTPStatus.OK
            content_type = "text/html"
            contents = Path(file_path).read_text()

        elif endpoint == "/listSpecies":
            limit = parameters["limit"][0]
            try:
                limit = int(limit)
                url = f"/info/species?content-type=application/json"
                error, data = server_request(ensemble_server, url)
                print("error", error)
                if not error:
                    species = data['species']
                    name_species = []
                    for specie in species[:limit]:
                        name_species.append(specie['display_name'])
                    context = {
                        'number_of_species': len(species),
                        'limit': limit,
                        'name_species': name_species
                    }
                    code = HTTPStatus.OK

                    content_type, contents = content_ctype("species.html", parameters, context)
                else:
                    code, content_type, contents = handle_error(endpoint, "Error in communication with Ensembl server", json_format='json' in parameters and parameters['json'][0] == '1')
            except ValueError:
                code, content_type, contents = handle_error(endpoint, "Error in communication with Ensembl server", json_format='json' in parameters and parameters['json'][0] == '1')

        elif endpoint == "/karyotype":
            specie = parameters["species"][0]
            url = f"/info/assembly/{specie}?content-type=application/json"
            error, data = server_request(ensemble_server, url)
            print(error, data)
            if not error:
                context = {"specie": specie,
                           "karyotype": data["karyotype"]
                           }

                code = HTTPStatus.OK
                content_type, contents = content_ctype("karyotype.html", parameters, context)
            else:
                code, content_type, contents = handle_error(endpoint, "Error in communication with Ensembl server", json_format='json' in parameters and parameters['json'][ 0] == '1')

        elif endpoint == "/chromosomeLength":
            specie = parameters["species"][0]
            chromosome = parameters["chromo"][0]
            url = f"/info/assembly/{specie}?content-type=application/json"
            error, data = server_request(ensemble_server, url)

            if not error:
                length = next(i["length"] for i in data["top_level_region"] if i["name"] == chromosome)
                context = {"specie": specie,
                           "length": length,
                           "number_chromosome": chromosome
                           }
                code = HTTPStatus.OK
                content_type, contents = content_ctype("chrom.html", parameters, context)
            else:
                code, content_type, contents = handle_error(endpoint, "Error in communication with Ensembl server", json_format='json' in parameters and parameters['json'][0] == '1')

        elif endpoint == "/geneSeq":
            gene = parameters["gene"][0]
            id_2 = get_id(gene)
            print(id)
            if id_2:
                url = f"/sequence/id/{id_2}?content-type=application/json"
                error, data = server_request(ensemble_server, url)
                print("error", error)
                seq = data["seq"]
                if not error:
                    context = {"gene": gene,
                               "seq": seq
                               }
                    code = HTTPStatus.OK

                    content_type, contents = content_ctype("human_seq.html", parameters, context)
                else:
                    code, content_type, contents = handle_error(endpoint, "Error in communication with Ensembl server", json_format='json' in parameters and parameters['json'][0] == '1')
            else:
                code, content_type, contents = handle_error(endpoint, "Error in communication with Ensembl server", json_format='json' in parameters and parameters['json'][0] == '1')

        elif endpoint == "/geneInfo":
            gene = parameters["gene"][0]
            id_2 = get_id(gene)
            url = f"/overlap/id/{id_2}?feature=gene;content-type=application/json"
            error, data = server_request(ensemble_server, url)
            print(data)

            if not error:
                for i in data:
                    start = i["start"]
                    end = i["end"]
                length = int(end) - int(start)

                context = {"name": data[0]["assembly_name"],
                           "start": data[0]["start"],
                           "end": end,
                           "length": length,
                           "id": id_2
                           }
                code = HTTPStatus.OK
                content_type, contents = content_ctype("geneInfo.html", parameters, context)
            else:
                code, content_type, contents = handle_error(endpoint, "Error in communication with Ensembl server", json_format='json' in parameters and parameters['json'][0] == '1')

        elif endpoint == "/geneCalc":
            gene = parameters["gene"][0]
            id_2 = get_id(gene)
            if id_2:
                url = f"/sequence/id/{id_2}?content-type=application/json"
                error, data = server_request(ensemble_server, url)
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
                    code = HTTPStatus.OK6
                    content_type, contents = content_ctype("geneCalc.html", parameters, context)
            else:
                code, content_type, contents = handle_error(endpoint, "Error in communication with Ensembl server", json_format='json' in parameters and parameters['json'][0] == '1')

        elif endpoint == "/geneList":
            chromo = parameters["chromo"][0]
            start = parameters["start"][0]
            end = parameters["end"][0]
            url = f"/overlap/region/human/{chromo}:{start}-{end}?feature=gene;feature=transcript;feature=cds;feature=exon;content-type=application/json"
            print(url)
            error, data = server_request(ensemble_server, url)

            if not error:
                names = []
                for i in data:
                    try:
                        name = i["assembly_name"]
                        names.append(name)
                    except KeyError:
                        pass

                context = {"names": names,
                           "chromosome_num": chromo
                           }

                code = HTTPStatus.OK

                content_type, contents = content_ctype("geneList.html", parameters, context)
            else:
                code, content_type, contents = handle_error(endpoint, "Error in communication with Ensembl server", json_format='json' in parameters and parameters['json'][0] == '1')

        else:
            contents = handle_error(endpoint, "Sorry, resource not available")
            code = HTTPStatus.NOT_FOUND

        self.send_response(code)
        contents_bytes = contents.encode()
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(contents_bytes)))
        self.end_headers()

        self.wfile.write(contents_bytes)


with socketserver.TCPServer(("", port), Myhandler) as httpd:
    print("Serving at PORT...", port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print("Stopped by the user")
        httpd.server_close()
