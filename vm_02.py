import socket
import random
import requests


# temp is an abbreviation for temperature
def receive_temp_vm_2(request, temp_sensor_01_socket, k):    
    api_url = 'http://127.0.0.1:5000'

    if request == "DEC01":
        ADCval = random.randrange(0, 128+1)
        t2 = k * ADCval + 5
        
        print(f"VM-01 Request: {request} >> T2 = {k} * {ADCval} + 5 = {t2}")
        response = f"{request} >> T2 = {k} * {ADCval} + 5 = {t2} ".encode("utf-8")
        temp_sensor_01_socket.send(response)

    elif request == "DEC02":
        ADCval = random.randrange(0, 128+1)
        t2 = k * ADCval + 5
        
        print(f"VM-01 Request: {request} >> T2 = {k} * {ADCval} + 5 = {t2}")
        response = f"{request} >> T2 = {k} * {ADCval} + 5 = {t2} ".encode("utf-8")
        temp_sensor_01_socket.send(response)

    elif request == "INC01":
        ADCval = random.randrange(0, 128+1)
        t2 = k * ADCval + 5
        
        print(f"VM-01 Request: {request} >> T2 = {k} * {ADCval} + 5 = {t2}")
        response = f"{request} >> T2 = {k} * {ADCval} + 5 = {t2} ".encode("utf-8")
        temp_sensor_01_socket.send(response)

    elif request == "INC02":
        ADCval = random.randrange(0, 128+1)
        t2 = k * ADCval + 5
        
        print(f"VM-01 Request: {request} >> T2 = {k} * {ADCval} + 5 = {t2}")
        response = f"{request} >> T2 = {k} * {ADCval} + 5 = {t2} ".encode("utf-8")
        temp_sensor_01_socket.send(response)

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

def run_temp_sensor_02():
    temp_sensor_02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    temp_sensor_02_ip = "127.0.0.1"
    port = 8000

    temp_sensor_02.bind((temp_sensor_02_ip, port))
    temp_sensor_02.listen(0)
    print(f"Listening on {temp_sensor_02_ip}:{port}")

    temp_sensor_01_socket, temp_sensor_01_address = temp_sensor_02.accept()
    print(f"Accepted connection from {temp_sensor_01_address[0]}:{temp_sensor_01_address[1]}")
    
    k = 5

    while True:
        request = temp_sensor_01_socket.recv(1024)
        request = request.decode("utf-8")

        if request == "DEC01":
            k += -1
            receive_temp_vm_2(request, temp_sensor_01_socket, k)

        elif request == "DEC02":
            k += -2
            receive_temp_vm_2(request, temp_sensor_01_socket, k)

        elif request == "INC01":
            k += 1
            receive_temp_vm_2(request, temp_sensor_01_socket, k)

        elif request == "INC02":
            k += 2
            receive_temp_vm_2(request, temp_sensor_01_socket, k)

        elif request.lower() == "close":
            temp_sensor_01_socket.send("closed".encode("utf-8"))
            break

        else:
            temp_sensor_01_socket.send("Wrong input".encode("utf-8"))

    temp_sensor_01_socket.close()
    print("Connection to temp_sensor_01 closed")
    temp_sensor_02.close()


run_temp_sensor_02()
