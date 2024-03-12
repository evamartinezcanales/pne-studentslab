from client0 import Client
c = Client("127.0.0.1", 8081)
correct = True
while correct:
    request = input("Enter a number")
    response = c.talk(request)
    print(response)
    if response != "lower" and response != "higher":
        correct = False