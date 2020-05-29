import pygame
from random import randint
 
branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
 
try:
    pygame.init()
except:
    print("O modulo pygame não foi inicializado com sucesso")
 
largura=640
altura=520
placar=40
tamanho = 10
pos_x=randint(0,(largura-tamanho)/10)*10
pos_y=randint(placar,(altura-tamanho)/10)*10 
maca_x=randint(0,(largura-tamanho)/10)*10
maca_y=randint(placar,(altura-tamanho)/10)*10
velocidade_x=0
velocidade_y=0
CobraXY=[]
Cobracomp=1
pontos=0
 
fps = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Jogo Snake")
fonte_texto=pygame.font.SysFont(None, 32)
texto=fonte_texto.render('Game Over',True,vermelho)
 
jogo = True
fimdejogo= False