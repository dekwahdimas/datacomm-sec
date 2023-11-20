import socket
import random
import requests
import json

def receiveTemp2():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"
    port = 8000

    server.bind((server_ip, port))
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")

    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    api_url = 'http://127.0.0.1:5000'

    k = 5
    
    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8")

        if request == "DEC01":
            k += -1
            ADCval = random.randrange(0, 128+1)
            t2 = k * ADCval + 5
            
            print(f"VM-01 Request: {request}")
            response = f"{request}: {t2} = {k} * {ADCval} + 5".encode("utf-8")
            client_socket.send(response)

        elif request == "DEC02":
            k += -2
            ADCval = random.randrange(0, 128+1)
            t2 = k * ADCval + 5
            
            print(f"VM-01 Request: {request}")
            response = f"{request}: {t2} = {k} * {ADCval} + 5".encode("utf-8")
            client_socket.send(response)

        elif request == "INC01":
            k += 1
            ADCval = random.randrange(0, 128+1)
            t2 = k * ADCval + 5
            
            print(f"VM-01 Request: {request}")
            response = f"{request}: {t2} = {k} * {ADCval} + 5".encode("utf-8")
            client_socket.send(response)

        elif request == "INC02":
            k += 2
            ADCval = random.randrange(0, 128+1)
            t2 = k * ADCval + 5
            
            print(f"VM-01 Request: {request}")
            response = f"{request}: {t2} = {k} * {ADCval} + 5".encode("utf-8")
            client_socket.send(response)

        elif request.lower() == "close":
            client_socket.send("closed".encode("utf-8"))
            break
        else:
            client_socket.send("Wrong input".encode("utf-8"))

        temperature_json = {
            't2': t2,
        }

        jsonResponse = requests.post(
            api_url + '/temperature_2',
            json = json.dumps(temperature_json),
        )

    client_socket.close()
    print("Connection to client closed")
    server.close()

    return jsonResponse

# run_server()
receiveTemp2()
