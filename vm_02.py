import socket
import random
import requests


# temp is an abbreviation for temperature
def receive_temp_vm_2(request, temp_sensor_01_socket, k):    
    # Define API URL
    api_url = 'http://127.0.0.1:5000'

    if request == "DEC01": 
        ADCval = random.randrange(0, 128+1) # random number from 0 to 128
        t2 = k * ADCval + 5 # temperature_2 equation
        
        # Show response from temp_sensor_02
        print(f"VM-01 Request: {request} >> T2 = {k} * {ADCval} + 5 = {t2}")
        
        # Sending response to temp_sensor_01
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

    # Pass temperature value from sensor 02 as a dictionary
    temperature_json = {
        't2': t2,
    }

    # POST to Flask API
    try:
        jsonResponse = requests.post(
            api_url + '/temperature_2', # define path to access temp_sensor_01
            json=temperature_json, # pass temperature value to API
        )
    # Let the temp_sensors run even without connection to API
    except:
        pass

def run_temp_sensor_02():
    temp_sensor_02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define temp_sensor_02 ip and port
    temp_sensor_02_ip = "127.0.0.1"
    temp_sensor_02_port = 8000

    # Bind temp_sensor_02 socket to specific address and port
    temp_sensor_02.bind((temp_sensor_02_ip, temp_sensor_02_port))
    # Listen to incoming connections
    temp_sensor_02.listen(0)
    print(f"Listening on {temp_sensor_02_ip}:{temp_sensor_02_port}")

    # Accept incoming connection
    temp_sensor_01_socket, temp_sensor_01_address = temp_sensor_02.accept()
    print(f"Accepted connection from {temp_sensor_01_address[0]}:{temp_sensor_01_address[1]}")
    
    # Define the value of k
    k = 5

    # Receive data from temp_sensor_01
    while True:
        request = temp_sensor_01_socket.recv(1024)
        request = request.decode("utf-8") # convert bytes to string

        # Checking for input by user
        if request == "DEC01":
            k += -1 # decrease/increase the value of k based on user's input
            receive_temp_vm_2(request, temp_sensor_01_socket, k) # call function

        elif request == "DEC02":
            k += -2
            receive_temp_vm_2(request, temp_sensor_01_socket, k)

        elif request == "INC01":
            k += 1
            receive_temp_vm_2(request, temp_sensor_01_socket, k)

        elif request == "INC02":
            k += 2
            receive_temp_vm_2(request, temp_sensor_01_socket, k)

        # Close connection if the input is 'close'
        elif request.lower() == "close":
            temp_sensor_01_socket.send("closed".encode("utf-8"))
            break # stop while loop

        else: # if the input is not available
            temp_sensor_01_socket.send("Wrong input".encode("utf-8"))

    # Close connection socket with temp_sensor_01
    temp_sensor_01_socket.close()
    print("Connection to temp_sensor_01 closed")
    temp_sensor_02.close() # Close temp_sensor_02 socket


run_temp_sensor_02()
