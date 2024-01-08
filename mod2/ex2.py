from pyModbusTCP.client import ModbusClient 
from pyModbusTCP import utils 
from time import sleep 

# Define device/robot parameters 
SERVER_IP = '192.168.1.252' #TMRobot
SERVER_PORT = 502 
DEVICE_ID = 1 

# Establishing TCP connection 
print ('trying to establish connection.......')
client = ModbusClient(host=SERVER_IP, port=SERVER_PORT) 

if client.open():
    print ("Connection to Robot %s:%d established succesfully" % (SERVER_IP, SERVER_PORT))
else: 
    print ("[Error] Fail to connect to modbus slave %s:%d." % (SERVER_IP, SERVER_PORT))

# Define Parameters 
    
play_pause = client.write_single_coil(7104,1)
# modbus_play = client.write_single_coil(7104,1) 
sleep(1)

while True: 
    startup_tool = client.read_holding_registers(9001,1)[0]
    grip = client.read_holding_registers(9002,1)[0]
    release = client.read_holding_registers(9003,1)[0]

    print('-'*40)
    if startup_tool == 1:
        print('Ferramenta status: ON')
    else:
        print('Ferramenta status : OFF')
    
    if grip == 1 and release == 0:
        print('Grip status: YES')
    else:
        print('Grip status: NO')

    if release == 1 and grip == 0:
        print('Release status: YES')
    else:
        print('Release status: NO')

    sleep(1)
