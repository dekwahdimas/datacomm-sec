import socket
import random
import requests


# temp is an abbreviation for temperature
def run_temp_sensor_01():
    temp_sensor_01 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    temp_sensor_02_ip = "127.0.0.1"
    temp_sensor_02_port = 8000  

    temp_sensor_01.connect((temp_sensor_02_ip, temp_sensor_02_port))

    api_url = 'http://127.0.0.1:5000'

    while True:
        msg = input("Enter parameter of 'k': ").upper()

        random_num = random.randrange(-1, 1+1) # random number from -1 to 1
        t1 = random_num * 5 + 40

        temperature_json = {
            't1': t1,
        }

        try:
            jsonResponse = requests.post(
                api_url + '/temperature_1',
                json = temperature_json,
            )
        except:
            pass

        temp_sensor_01.send(msg.encode("utf-8")[:1024])

        response = temp_sensor_01.recv(1024)
        response = response.decode("utf-8")

        if response.lower() == "closed":
            break

        print(f"VM-02 Response: {response}")

    temp_sensor_01.close()
    print("Connection to temp_sensor_02 closed")


run_temp_sensor_01()
