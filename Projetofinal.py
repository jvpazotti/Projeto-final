# importamos as bibliotecas utilizadas no código

import pygame
from random import randint
import os


def main():
    # inicializamos o pygame
    pygame.init() 
    
    #definimos as cores que utilizamos nos textos , na cobra e na maçã
    branco=(255,255,255)
    preto=(0,0,0)
    vermelho=(255,0,0)
    verde=(0,255,0)
    azul=(0,0,255)

    # definimos variáveis para tela do jogo e cobra
    tamanho = 10 
    largura=320
    altura=280

    #definimos o fps, tela do jogo(seu tamanho) e o nome do jogo 
    fps = pygame.time.Clock()
    tela = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption("Jogo Snake")

    #colocamos as músicas e a imagem da tela do jogo
    arquivo1=os.path.join('Music','morte mario.mp3')
    arquivo=os.path.join('Music','Sexy And I Know It-LMFAO (Instrumental).mp3')
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    terra_tela = pygame.image.load('img/fundo do jogo.png').convert() 
    terra_tela = pygame.transform.scale(terra_tela,(largura,altura)) 


    def randomiza_posicao():
        coordenada_x = randint(0,(largura-tamanho)/10)*10
        coordenada_y = randint(0,(altura-tamanho)/10)*10
        return coordenada_x, coordenada_y

    def determina_velocidade(velocidade_x, velocidade_y):
        return velocidade_x, velocidade_y

    #definimos do que o nosso texto é composto a partir da seguinte classe:
    
    #podemos fazer uma superclasse de texto pois pode dividir texto com ponto e sem ponto
    class Texto:
        def __init__(self, mensagem, cor, tamanho):#pontos=0):
            self.fonte_texto = pygame.font.SysFont(None, tamanho)
            self.cor=cor
            self.mensagem=mensagem
            self.texto = self.fonte_texto.render(self.mensagem, True, self.cor)
            #self.texto2 = self.fonte_texto.render(self.mensagem+str(pontos) , True, self.cor)  
        
        def aparece_na_tela(self, x, y):
            tela.blit(self.texto, [x,y])
        
        #def aparece_na_tela2(self, x, y):
           # tela.blit(self.texto2, [x,y])
        
        
        #def atualiza_pontos(self,pontos):
            #self.texto2 = self.fonte_texto.render(self.mensagem+str(pontos) , True, self.cor)  

    # Subclasse de texto para separar texto com pontuação de texto sem pontuação
    class TextoPontos(Texto):
        def __init__(self, mensagem, cor,tamanho):
            super().__init__(mensagem,cor,tamanho) 
            self.fonte_texto = pygame.font.SysFont(None, tamanho)    
            self.pontos=0
            self.texto = self.fonte_texto.render(self.mensagem+str(self.pontos) , True, self.cor)
        def atualiza_pontos(self,pontos):
            self.texto = self.fonte_texto.render(self.mensagem+str(pontos) , True, self.cor)

        def restart(self):
            self.pontos = 0
    #definimos do que a nossa maçã é composta a partir da seguinte classe: 

    #funcao para juntar as contas de posicao

    class Maca:
        def __init__(self):
            # self.x = randint(0,(largura-tamanho)/10)*10
            # self.y = randint(0,(altura-tamanho)/10)*10
            self.x, self.y = randomiza_posicao()
        def imagem_m(self):
            pygame.draw.rect(tela, vermelho, [self.x, self.y, tamanho, tamanho])
        
        #Essa função faz nada no código, pode ser retirada
        def posicao_m(self):
            # self.x = randint(0,(largura-tamanho)/10)*10
            # self.y = randint(0,(altura-tamanho)/10)*10
            self.x, self.y = randomiza_posicao()


    #definimos do que a nossa cobra é composta a partir da seguinte classe: 
    class Cobra:
        def __init__(self):
            # self.x = randint(0,(largura-tamanho)/10)*10
            # self.y = randint(0,(altura-tamanho)/10)*10
            self.x, self.y = randomiza_posicao()
            #self.vel_x = 0
            #self.vel_y = 0
            self.vel_x, self.vel_y = determina_velocidade(0,0)
            self.cobra_xy = []
            self.cobra_comp = 1
            self.cobra_0 = []
            #self.pontos = 0
            self.fimdejogo = False
        
        def movimento_c(self):
            self.cobra_0 = [self.x,self.y]
            self.cobra_xy.append(self.cobra_0) 
        def crescimento_c(self):
            self.cobra_comp += 1
        def imagem_c(self):
            for XY in self.cobra_xy:
                pygame.draw.rect(tela,verde,[XY[0],XY[1],tamanho,tamanho])
        def resto(self):
            if len(self.cobra_xy) > self.cobra_comp:
                del self.cobra_xy[0]
        def morte(self):
            if any(Bloco == self.cobra_0 for Bloco in self.cobra_xy[:-1]):
                self.fimdejogo = True
        
        def recomeco(self):
            # self.x = randint(0,(largura-tamanho)/10)*10
            # self.y = randint(0,(altura-tamanho)/10)*10
            self.x, self.y = randomiza_posicao()
            #self.vel_x = 0
            #self.vel_y = 0
            self.vel_x, self.vel_y = determina_velocidade(0,0)
            self.cobra_xy = []
            self.cobra_comp = 1
            #self.cobra_0 = []
            #self.pontos = 0
            #self.fimdejogo = False
            
    # criamos variaveis para iniciar/encerrar o loop 
    jogo = False
    fimdejogo = False
    antesdojogo = True

    # criamos os objetos para as classes
    snake = Cobra()
    apple = Maca()
    text = Texto("Game Over", vermelho, 35)
    text2 = TextoPontos("Pontuação: " , branco, 27)
    text3 = Texto("Aperte espaço",branco,27)
    text4 = Texto("Deseja continuar?",branco,27)
    text5= Texto("Snake Game",branco,35)
    text6= Texto("Aperte C para começar",branco,27)

    #tela inicial do jogo
    while antesdojogo:
        tela.blit(terra_tela,(0,0)) 
        text5.aparece_na_tela(80,130)
        text6.aparece_na_tela(60,160)
        pygame.display.update()
        # movimentação com as teclas
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                antesdojogo=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    jogo=True

     #iniciamos loop do jogo
        while jogo:
            # aplicação dos parâmetros no loop
            fps.tick(15)
            tela.blit(terra_tela,(0,0)) 
            snake.movimento_c()
            text2.aparece_na_tela(90,5)
            
            # movimentação com as teclas
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jogo = False
                    antesdojogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and snake.vel_x != tamanho:
                        #snake.vel_y = 0
                        #snake.vel_x = -tamanho
                        snake.vel_x, snake.vel_y = determina_velocidade(-tamanho, 0)
                    if event.key == pygame.K_RIGHT and snake.vel_x != -tamanho:
                        snake.vel_y = 0
                        snake.vel_x = tamanho
                        snake.vel_x, snake.vel_y = determina_velocidade(tamanho,0)
                    if event.key == pygame.K_UP and snake.vel_y != tamanho:
                        #snake.vel_x = 0
                        #snake.vel_y = -tamanho
                        snake.vel_x, snake.vel_y = determina_velocidade(0,-tamanho)
                    if event.key == pygame.K_DOWN and snake.vel_y != -tamanho:
                        #snake.vel_x = 0
                        #snake.vel_y = tamanho
                        snake.vel_x, snake.vel_y = determina_velocidade(0,tamanho)
            
           
            # implementação do movimento da cobra
            snake.x += snake.vel_x
            snake.y += snake.vel_y
        
            # implementação das funções gerais
            apple.imagem_m()
            snake.resto()
            snake.imagem_c()
            snake.morte() 
        
            # funções que definem a colisão cobra+maça
            if snake.x == apple.x and snake.y == apple.y:
                # apple.x = randint(0,(largura-tamanho)/10)*10
                # apple.y = randint(0,(altura-tamanho)/10)*10
                apple.x, apple.y = randomiza_posicao()
                snake.cobra_comp += 1
                #snake.pontos += 1
                text2.pontos+=1
                text2.atualiza_pontos(text2.pontos)
            
            # tela de fim de jogo
            while fimdejogo:
                    tela.fill(preto)
                    text.aparece_na_tela(95,130)
                    text2.aparece_na_tela(95,160)
                    text3.aparece_na_tela(175,210)
                    text4.aparece_na_tela(5,210)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            jogo = False
                            fimdejogo = False
                            antesdojogo = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                fimdejogo=False
                                jogo=True
                                snake.recomeco()
                                text2.restart()
                                apple.posicao_m()
                                text2.atualiza_pontos(text2.pontos)
                                pygame.mixer.music.load(arquivo)
                                pygame.mixer.music.set_volume(0.1)
                                pygame.mixer.music.play(-1)
            
                                

            # definição da colisão da cobra com as paredes        
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
            if fimdejogo == True:
                # música do fim de jogo
                pygame.mixer.music.pause()
                pygame.mixer.music.load(arquivo1)
                pygame.mixer.music.set_volume(0.1) 
                pygame.mixer.music.play(1)

            # atualização da tela em loop
            pygame.display.update()
if __name__ == "__main__":
    main()


    