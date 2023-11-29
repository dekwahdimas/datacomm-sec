import socket
import random
import requests


# temp is an abbreviation for temperature
def run_temp_sensor_01():
    temp_sensor_01 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define temp_sensor_02 ip and port
    temp_sensor_02_ip = "127.0.0.1"
    temp_sensor_02_port = 8000  

    # Initialize a connection with temp_sensor_02
    temp_sensor_01.connect((temp_sensor_02_ip, temp_sensor_02_port))

    # Define API URL
    api_url = 'http://127.0.0.1:5000'

    # Input data from temp_sensor_01
    while True:
        # Input parameter of k and capitalize it
        k_param = input("Enter parameter of 'k': ").upper()

        # Define random int
        random_num = random.randrange(-1, 1+1) # random number from -1 to 1
        t1 = random_num * 5 + 40 # temperature_1 equation

        # Pass temperature value from sensor 01 as a dictionary
        temperature_json = {
            't1': t1,
        }

        # POST to Flask API
        try: 
            jsonResponse = requests.post(
                api_url + '/temperature_1', # define path to access temp_sensor_01
                json = temperature_json, # pass temperature value to API
            )
        # Let the temp_sensors run even without connection to API
        except:
            pass
        
        # Sending input parameter to temp_sensor_02
        temp_sensor_01.send(k_param.encode("utf-8")[:1024])

        # Receive response from temp_sensor_02
        response = temp_sensor_01.recv(1024)
        response = response.decode("utf-8")

        # Close connection if the input is 'close'
        if response.lower() == "closed":
            break
        
        # Show response from temp_sensor_02
        print(f"VM-02 Response: {response}")

    # Close temp_sensor_01 socket
    temp_sensor_01.close()
    print("Connection to temp_sensor_02 closed")


run_temp_sensor_01()
