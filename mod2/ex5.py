from pyModbusTCP.client import ModbusClient 
from pyModbusTCP import utils 
from time import sleep 
import pygame
import sys

# Define device/robot parameters 
SERVER_IP = '192.168.1.252' #TMRobot
SERVER_PORT = 502 
DEVICE_ID = 1 

# Establishing TCP connection 
print('trying to establish connection.......')
client = ModbusClient(host=SERVER_IP, port=SERVER_PORT) 

if client.open():
    print ("Connection to Robot %s:%d established succesfully" % (SERVER_IP, SERVER_PORT))
else: 
    print ("[Error] Fail to connect to modbus slave %s:%d." % (SERVER_IP, SERVER_PORT))

# Define Parameters 
    
play_pause = client.write_single_coil(7104,1)
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

    sinal_verde = client.read_coils(4,1)[0]
    sinal_vermelho = client.read_coils(5,1)[0]
    sinal_laranja = client.read_coils(6,1)[0]
    esteira = client.read_coils(7,1)[0]

    janela.fill((255, 255, 255))
    
    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                stop = client.write_single_coil(7105,1)
                t = 'STOP'

            if event.key == pygame.K_b:
                pass
                
            if event.key == pygame.K_p:
                play = client.write_single_coil(7104,1)
                count+=1
                if count %2 == 1:
                    t = 'PLAY'
                else:
                    t = "Pause"
    estado_verde = fontesys.render(f'Verde {str(sinal_verde)}',1,(0,0,0))
    estado_vermelho = fontesys.render(f'Vermelho {str(sinal_vermelho)}',1,(0,0,0))
    estado_laranja = fontesys.render(f'Laranja {str(sinal_laranja)}',1,(0,0,0))

    janela.blit(estado_verde,(100,100))
    janela.blit(estado_vermelho,(100,200))
    janela.blit(estado_laranja,(100,300))

    pygame.display.flip()
