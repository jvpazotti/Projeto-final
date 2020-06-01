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
    def __init__(self, mensagem, cor, tamanho,pontos=0):
        self.fonte_texto = pygame.font.SysFont(None, tamanho)
        self.cor=cor
        self.mensagem=mensagem
        self.texto = self.fonte_texto.render(self.mensagem, True, self.cor)
        self.texto2 = self.fonte_texto.render(self.mensagem+str(pontos) , True, self.cor)  
      
    def aparece_na_tela(self, x, y):
        fundo.blit(self.texto, [x,y])
    def aparece_na_tela2(self, x, y):
        fundo.blit(self.texto2, [x,y])
    def atualiza_pontos(self,pontos):
        self.texto2 = self.fonte_texto.render(self.mensagem+str(pontos) , True, self.cor)  
    
 
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
        self.x = randint(0,(largura-tamanho)/10)*10
        self.y = randint(0,(altura-tamanho)/10)*10
        self.vel_x = 0
        self.vel_y = 0
        self.cobra_xy = []
        self.cobra_comp = 1
        self.cobra_0 = []
        self.pontos = 0
        self.fimdejogo = False
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
text2 = Texto("Pontuação: " , branco, 27)
 
while jogo:
    fps.tick(15)
    fundo.fill(azul)
    snake.movimento_c()
    text2.aparece_na_tela2(10,10)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.vel_x != tamanho:
                snake.vel_y = 0
                snake.vel_x = -tamanho
            if event.key == pygame.K_RIGHT and snake.vel_x != -tamanho:
                snake.vel_y = 0
                snake.vel_x = tamanho
            if event.key == pygame.K_UP and snake.vel_y != tamanho:
                snake.vel_x = 0
                snake.vel_y = -tamanho
            if event.key == pygame.K_DOWN and snake.vel_y != -tamanho:
                snake.vel_x = 0
                snake.vel_y = tamanho
 
    snake.x += snake.vel_x
    snake.y += snake.vel_y
 
    apple.imagem_m()
 
    snake.resto()
 
    snake.imagem_c()
 
    snake.morte() 
 
    if snake.x == apple.x and snake.y == apple.y:
        apple.x = randint(0,(largura-tamanho)/10)*10
        apple.y = randint(0,(altura-tamanho)/10)*10
        snake.cobra_comp += 1
        snake.pontos += 1
        text2.atualiza_pontos(snake.pontos)
    while fimdejogo:
            fundo.fill(preto)
            text.aparece_na_tela(95,130)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jogo = False
                    fimdejogo= False
            
    if snake.x + tamanho> largura:
            fimdejogo=True
    if snake.x < 0:
            fimdejogo=True
    if snake.y + tamanho> altura:
            fimdejogo=True
    if snake.y < 0:
            fimdejogo=True
    if snake.fimdejogo == True:
            fimdejogo=True
        
    pygame.display.update()