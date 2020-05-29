import pygame
from random import randint
pygame.init() 


branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
tamanho = 10 
largura=320
altura=280
placar=40
pontos = 0
fps = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Jogo Snake")

class Texto:
    def __init__(self, mensagem, cor, tamanho):
        self.fonte_texto = pygame.font.SysFont(None, tamanho)
        self.texto = self.fonte_texto.render(mensagem, True, cor)
        self.texto2 = self.fonte_texto.render(mensagem + str(snake.pontos), True, cor)  
      
    def aparece_na_tela(self, x, y):
        fundo.blit(self.texto, [x,y])
    def aparece_na_tela2(self, x, y):
        fundo.blit(self.texto2, [x,y])


class Maca:
    def __init__(self):
        self.x = randint(0,(largura-tamanho)/10)*10
        self.y = randint(0,(altura-tamanho)/10)*10
    def imagem_m(self):
        pygame.draw.rect(fundo, vermelho, [self.x, self.y, tamanho, tamanho])
    def posicao_m(self):
        self.x = randint(0,(largura-tamanho)/10)*10
        self.y = randint(0,(altura-tamanho)/10)*10

class Cobra:
    def __init__(self):
        self.x = randint(tamanho,(largura-tamanho)/10)*10
        self.y = randint(tamanho,(altura-tamanho)/10)*10
        self.vel_x = 0
        self.vel_y = 0
        self.cobra_xy = []
        self.cobra_comp = 1
        self.cobra_0 = []
        self.pontos = 0
    def movimento_c(self):
        self.cobra_0 = [self.x,self.y]
        self.cobra_xy.append(self.cobra_0) 
    def crescimento_c(self):
        self.cobra_comp += 1
    def imagem_c(self):
        for XY in self.cobra_xy:
            pygame.draw.rect(fundo,verde,[XY[0],XY[1],tamanho,tamanho])
    def resto(self):
        if len(self.cobra_xy) > self.cobra_comp:
            del self.cobra_xy[0]
    def morte(self):
        if any(Bloco == self.cobra_0 for Bloco in self.cobra_xy[:-1]):
            self.fimdejogo = True
       
jogo = True
fimdejogo= False

snake = Cobra()
apple = Maca()
text = Texto("Game Over", vermelho, 35)
text2 = Texto("Pontuação: ", branco, 30)

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