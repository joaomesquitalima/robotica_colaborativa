from classe_float import FloatModbusClient
from pyModbusTCP import utils
from time import sleep
import pygame
import sys
# Define device/robot parameters

SERVER_IP = '192.168.1.254'
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

pygame.init()
janela = pygame.display.set_mode([640, 480])
while True:
    txt='hello world'                                 ##### armazena o texto
    pygame.font.init()                                ##### inicia font
    fonte=pygame.font.get_default_font()              ##### carrega com a fonte padrão
    fontesys=pygame.font.SysFont(fonte, 60)

    x_coordenada = client.read_input_registers_float(7001,2)[0]
    y_coordenada = client.read_input_registers_float(7003,2)[0]
    z_coordenada = client.read_input_registers_float(7005,2)[0]
    
    eixo_x = f'Coordenada: X {x_coordenada:.1f}'
    eixo_y = f'Coordenada: Y {y_coordenada:.1f}'
    eixo_z = f'Coordenada: Z {z_coordenada:.1f}'



    janela.fill((255, 255, 255))
    
    for event in pygame.event.get():
        

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                stop = client.write_single_coil(7105,1)
                
            if event.key == pygame.K_p:
                play = client.write_single_coil(7105,1)
                


    x = fontesys.render(eixo_x, 1, (0,0,0))
    y = fontesys.render(eixo_y, 1, (0,0,0))  
    z = fontesys.render(eixo_z, 1, (0,0,0))
    
    janela.blit(x,(100,100))
    janela.blit(y,(100,200))
    janela.blit(z,(100,300))

    pygame.display.flip()

