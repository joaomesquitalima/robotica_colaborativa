from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
from time import sleep

SERVER_IP = '192.168.1.252'
SERVER_PORT = 502
DEVICE_ID = 1

print('tentando conectar')
client = ModbusClient(host=SERVER_IP, port=SERVER_PORT)

if client.open():
    print('Connetion to Robot %s:%d established sucesso' %(SERVER_IP,SERVER_PORT))

else:
    print('erro')
    exit()

play_pause = client.write_single_coil(7104,1)

sleep(1)

while True:
    green_button = client.read_discrete_inputs(3,1)[0]
    red_button = client.read_discrete_inputs(4,1)[0]
    sensor_1 = client.read_discrete_inputs(1,1)[0]
    print('verde: ', green_button,'vermelho: ', red_button,"sensor: ",sensor_1)
    sleep(1)
   
