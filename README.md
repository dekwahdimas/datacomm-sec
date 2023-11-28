# Data Communication Security Project

Data communication security is applied between three virtual machines using socket programming and rest-api.

> _the main goals were achieved but it's still a work in progress_

## About Virtual Machines

1. Virtual Machine 1 (VM-01)
   - Act as a temperature sensor-1.
   - `temperature_1 = random_int * 5 + 40`. random_int varies from -1 to 1.
   - Able to communicate with VM-02 using socket programming.
   - Able to send sensor state to VM-03 using rest-api.
   - Able to receive input from user to trigger VM-02. More explanation will be written in a table down below.

2. Virtual Machine 2 (VM-02)
   - Act as a temperature sensor-2.
   - `temperature_2 = k * ADCval + 5`. The value of k is preset to 5 and ADCval varies from 0-128
   - Able to communicate with VM-01 using socket programming.
   - Able to send sensor state to VM-03 using rest-api.
   - Able to receive user input from VM-01, then give response base on the input. More explanation will be written in a table down below.

3. Virtual Machine 3 (VM-03)
   - Act as a server, a rest-api, and a place to host the website.
   - Able to receive sensor state from VM-01 and VM-02 using rest-api.
   - `temperature_3 = temperature_1 - temperature_2`.
   - Able to show temperature values to the website.

### Explanation about input and response

|Input by User|Input send to VM-02|Response by VM-02 |
|:-----------:|:-----------------:|:----------------:|
|DEC01/dec01  |DEC01              |k = -1            |
|DEC02/dec02  |DEC02              |k = -2            |
|INC02/inc01  |INC01              |k = +1            |
|INC02/inc02  |INC02              |k = +2            |

## What to Achieves

- [x] Create 3 virtual machines.
- [x] VM-01 & VM-02 able to communicate using socket programming.
- [x] VM-01 & VM-02 able to communicate with VM-03 using API.
- [x] VM-03 able to show VM-01 & VM-02 data to the web.
- [ ] Create/use a cool-looking html template.

## References

|<center>Title</center>|URL|
|-----|:---:|
|A Complete Guide to Socket Programming in Python|[DataCamp](https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python)|
|Build a REST API using Flask|[Geeks for Geeks](https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/)|
|How to Send and Receive Data in Flask|[Software Development for Everyone](https://www.realpythonproject.com/how-to-send-and-receive-data-in-flask/)|
