from classe_float import FloatModbusClient
from pyModbusTCP import utils
from time import sleep
import pygame
import sys
# Define device/robot parameters

SERVER_IP = '192.168.1.252'
SERVER_PORT = 502 
DEVICE_ID = 1 

# Establish TCP connection
print('Trying to establish connection.....')
client = FloatModbusClient(host=SERVER_IP, port=SERVER_PORT, auto_open=True)

if client.open():
    print("Connection to Robot %s:%d established succesfully" % (SERVER_IP, SERVER_PORT))
else:
    print("[Error] Fail to connect to modbus slave %s:%d." % (SERVER_IP, SERVER_PORT))
    exit()
# Define Parameters

play_pause = client.write_single_coil(7104,1)


coordenadas_1 = client.write_float(9000,[470, 0, 350, 180.00,0.00,90.00])

while True:
    x_position = float(input("X: "))

    coordenadas = client.write_float(9000,[x_position, 0, 350, 180.00,0.00,90.00])
    print(coordenadas)
