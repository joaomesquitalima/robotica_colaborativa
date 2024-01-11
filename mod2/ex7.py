from classe_float import FloatModbusClient
from pyModbusTCP import utils
from time import sleep

# Define device/robot parameters
SERVER_IP = '192.168.1.254' # TMrobot
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
# modbus_play = client.write_single_coil(7104, 1)

sleep(1)

while True:
    value_z = float(input('Digite um valor para o Move no eixo z:'))
    value_j1 = float(input('Digite um valor para a junta:'))
    
    client.write_float(9000,[value_z])
    client.write_float(9002,[value_j1])
    sleep(1)

