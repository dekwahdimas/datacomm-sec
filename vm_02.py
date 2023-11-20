import socket
import random
import requests


def receive_temp_vm_2(request, client_socket, k):    
    api_url = 'http://127.0.0.1:5000'

    if request == "DEC01":
        ADCval = random.randrange(0, 128+1)
        t2 = k * ADCval + 5
        
        print(f"VM-01 Request: {request} >> T2 = {k} * {ADCval} + 5 = {t2}")
        response = f"{request} >> T2 = {k} * {ADCval} + 5 = {t2} ".encode("utf-8")
        client_socket.send(response)

    elif request == "DEC02":
        ADCval = random.randrange(0, 128+1)
        t2 = k * ADCval + 5
        
        print(f"VM-01 Request: {request} >> T2 = {k} * {ADCval} + 5 = {t2}")
        response = f"{request} >> T2 = {k} * {ADCval} + 5 = {t2} ".encode("utf-8")
        client_socket.send(response)

    elif request == "INC01":
        ADCval = random.randrange(0, 128+1)
        t2 = k * ADCval + 5
        
        print(f"VM-01 Request: {request} >> T2 = {k} * {ADCval} + 5 = {t2}")
        response = f"{request} >> T2 = {k} * {ADCval} + 5 = {t2} ".encode("utf-8")
        client_socket.send(response)

    elif request == "INC02":
        ADCval = random.randrange(0, 128+1)
        t2 = k * ADCval + 5
        
        print(f"VM-01 Request: {request} >> T2 = {k} * {ADCval} + 5 = {t2}")
        response = f"{request} >> T2 = {k} * {ADCval} + 5 = {t2} ".encode("utf-8")
        client_socket.send(response)

    temperature_json = {
        't2': t2,
    }

    try:
        # POST
        jsonResponse = requests.post(
            api_url + '/temperature_2',
            # headers={"Content-Type": "application/json"},
            json=temperature_json,
        )
        return k
    except:
        return k

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"
    port = 8000

    server.bind((server_ip, port))
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")

    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    
    k = 5

    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8")

        if request == "DEC01":
            k += -1
            receive_temp_vm_2(request, client_socket, k)

        elif request == "DEC02":
            k += -2
            receive_temp_vm_2(request, client_socket, k)

        elif request == "INC01":
            k += 1
            receive_temp_vm_2(request, client_socket, k)

        elif request == "INC02":
            k += 2
            receive_temp_vm_2(request, client_socket, k)

        elif request.lower() == "close":
            client_socket.send("closed".encode("utf-8"))
            break

        else:
            client_socket.send("Wrong input".encode("utf-8"))

    client_socket.close()
    print("Connection to client closed")
    server.close()


run_server()
