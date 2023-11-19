import socket
import random
import requests
import json

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"
    server_port = 8000  

    client.connect((server_ip, server_port))

    api_url = 'http://127.0.0.1:5000'

    while True:
        msg = input("Enter message: ")

        random_num = random.randrange(-1, 1+1) # random number from -1 to 1
        t1 = random_num * 5 + 40

        temperature_json = {
            't1': t1,
        }

        jsonResponse = requests.post(
            api_url + '/temperature_1',
            json = json.dumps(temperature_json),
        )

        client.send(msg.encode("utf-8")[:1024])

        response = client.recv(1024)
        response = response.decode("utf-8")

        if response.lower() == "closed":
            break

        print(f"VM-02 Response: {response}")

    client.close()
    print("Connection to server closed")

    return jsonResponse

run_client()
