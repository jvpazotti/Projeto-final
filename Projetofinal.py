import pygame
from random import randint
 
branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
 

pygame.init()

 
largura=320
altura=280
#placar=40
tamanho = 10
pos_x=randint(0,(largura-tamanho)/10)*10
pos_y=randint(0,(altura-tamanho)/10)*10 
maca_x=randint(0,(largura-tamanho)/10)*10
maca_y=randint(0,(altura-tamanho)/10)*10
velocidade_x=0
velocidade_y=0
CobraXY=[]
Cobracomp=1
pontos=0
 
fps = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Jogo Snake")
fonte_texto=pygame.font.SysFont(None, 35)
fonte_texto2=pygame.font.SysFont(None, 30)
texto=fonte_texto.render('Game Over',True,vermelho)
 
jogo = True
fimdejogo= False

while jogo:
    fps.tick(15)
    fundo.fill(azul)
    CobraInicio=[]
    CobraInicio.append(pos_x)
    CobraInicio.append(pos_y)
    CobraXY.append(CobraInicio)
    texto2=fonte_texto2.render('Pontuação : '+ str(pontos),True,branco)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                velocidade_y=0
                velocidade_x=-tamanho
            if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                velocidade_y=0
                velocidade_x=tamanho
            if event.key == pygame.K_UP and velocidade_y != tamanho:
                velocidade_x=0
                velocidade_y=-tamanho
            if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                velocidade_x=0
                velocidade_y=tamanho
    
    #pygame.draw.rect(fundo,preto,[0,0,largura,placar])
    fundo.blit(texto2,[10,10])


    pos_x+=velocidade_x
    pos_y+=velocidade_y
    pygame.draw.rect(fundo, vermelho, [maca_x, maca_y, tamanho, tamanho])
    
    if len(CobraXY) > Cobracomp:
        del CobraXY[0]
   
    for XY in CobraXY:
        pygame.draw.rect(fundo,verde,[XY[0],XY[1],tamanho,tamanho])
    
    if pos_x == maca_x and pos_y == maca_y:
        maca_x=randint(0,(largura-tamanho)/10)*10
        maca_y=randint(0,(altura-tamanho)/10)*10
        Cobracomp+=1
        pontos+=1
    
    if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
        fimdejogo = True

    while fimdejogo:
        fundo.fill(preto)
        fundo.blit(texto,[95,130])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jogo = False
                fimdejogo= False

    
    if pos_x + tamanho> largura:
        fimdejogo=True
    if pos_x < 0:
        fimdejogo=True
    if pos_y + tamanho> altura:
        fimdejogo=True
    if pos_y < 0:
        fimdejogo=True

    

    pygame.display.update()