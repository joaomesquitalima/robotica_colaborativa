
from pyModbusTCP.client import ModbusClient 
from pyModbusTCP import utils 
from time import sleep 
import pygame
import sys

# Define device/robot parameters 
SERVER_IP = '192.168.1.254' #TMRobot tm12
SERVER_IP2 = '192.168.1.252' #TMRobot tm12
SERVER_PORT = 502 
DEVICE_ID = 1 

# Establishing TCP connection 
print('trying to establish connection TM12.......')
client = ModbusClient(host=SERVER_IP, port=SERVER_PORT) 
# Establishing TCP connection 
print('trying to establish connection TM5.......')
client2 = ModbusClient(host=SERVER_IP2, port=SERVER_PORT) 

if client.open():
    print("Connection to Robot TM12 %s:%d established succesfully" % (SERVER_IP, SERVER_PORT))
else: 
    print ("[Error] TM12 Fail to connect to modbus slave %s:%d." % (SERVER_IP, SERVER_PORT))


if client2.open():
    print("Connection to Robot TM5 %s:%d established succesfully" % (SERVER_IP2, SERVER_PORT))
else: 
    print("[Error] TM5 Fail to connect to modbus slave %s:%d." % (SERVER_IP2, SERVER_PORT))


# Define Parameters 
    
play_pause = client.write_single_coil(7104,1)
play_pause2 = client2.write_single_coil(7104,1)
# modbus_play = client.write_single_coil(7104,1) 

pygame.init()
janela = pygame.display.set_mode([640, 480])


t = 'ON'

count = 0
while True:
    # Sensor 1
    txt='hello world'                                 
    pygame.font.init()                               
    fonte=pygame.font.get_default_font()              
    fontesys=pygame.font.SysFont(fonte, 60)
    estado = f'ESTADO : {t}'

    green_button = client.read_discrete_inputs(3,1)[0]
    red_button = client.read_discrete_inputs(4,1)[0]
    
    if green_button == 1:
        client2.write_single_coil(4,True)
        client2.write_single_coil(5,True)
        client2.write_single_coil(6,True)
        client2.write_single_coil(7,True)

    if red_button == 1:
        client2.write_single_coil(4,False)
        client2.write_single_coil(5,False)
        client2.write_single_coil(6,False)
        client2.write_single_coil(7,False)

        


    janela.fill((255, 255, 255))
    
    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                stop = client.write_single_coil(7105,1)
                t = 'STOP'

            if event.key == pygame.K_p:
                play = client.write_single_coil(7104,1)
                count+=1
                if count %2 == 1:
                    t = 'PLAY'
                else:
                    t = "Pause"



    # estado_verde = fontesys.render(f'Verde {str(sinal_verde)}',1,(0,0,0))
    # estado_vermelho = fontesys.render(f'Vermelho {str(sinal_vermelho)}',1,(0,0,0))
    # estado_laranja = fontesys.render(f'Laranja {str(sinal_laranja)}',1,(0,0,0))

    # janela.blit(estado_verde,(100,100))
    # janela.blit(estado_vermelho,(100,200))
    # janela.blit(estado_laranja,(100,300))

    pygame.display.flip()
