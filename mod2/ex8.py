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
# client.write_single_register(9000,0)
# client.write_single_register(9001,0)
# client.write_single_register(9002,0)
# client.write_single_register(9003,0)

s = 0
s2 = 0
s3 = 0
seq = 0

while True:
    s = int(input('Digite o valor em segundos 1:'))  
    s2 = int(input('Digite o valor em segundos 2:'))
    s3 = int(input('Digite o valor em segundos 3:'))
    
    seq = int(input('Digite a seq:'))
   
    s = s*1000
    s2 = s2*1000
    s3 = s3*1000
    client.write_single_register(9000,s)
    client.write_single_register(9001,s2)
    client.write_single_register(9002,s3)
    
    client.write_single_register(9003,seq)
    sleep(1)
    

