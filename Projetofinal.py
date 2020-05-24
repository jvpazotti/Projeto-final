import os
import sys
import pygame
import random

CINZA = (127, 127, 127)

def main():
    pygame.init()  # inicia rotinas do pygame

    surf = pygame.display.set_mode((600, 600)) # crio superficie para o jogo

    pygame.display.set_caption('Jogo Snake')

    arquivo = os.path.join('/Users/rafae/Documents/Insper/DesSoft/Projeto final/Projeto-final', 'Snake.png')
    arquivo2 = os.path.join('/Users/rafae/Documents/Insper/DesSoft/Projeto final/Projeto-final', 'apple.png')
    arquivo3 = os.path.join('/Users/rafae/Documents/Insper/DesSoft/Projeto final/Projeto-final', 'body.png')
   
    try:
        Snake = pygame.image.load(arquivo).convert_alpha()
    except pygame.error:
        print('Erro ao tentar ler Snake: caneca.png')
        sys.exit()
    try:
        apple = pygame.image.load(arquivo2).convert_alpha()
    except pygame.error:
        print('Erro ao tentar ler Snake: caneca.png')
        sys.exit()
    try:
        body = pygame.image.load(arquivo3).convert_alpha()
    except pygame.error:
        print('Erro ao tentar ler Snake: caneca.png')
        sys.exit()

    pos_cobra = [0,0]
    x = random.randint(20,590) 
    y = random.randint(20,590) 
    pos_maca = [x,y]

    delta_cobra={"esquerda":0, "direita":0, "acima":0, "abaixo":0}
    velocidade_cobra = 0.18

    clock = pygame.time.Clock() # objeto para controle da atualizações de imagens

    # Game Loop
    while True:
        delta_time = clock.tick(60) # garante um FPS máximo de 60Hz
        
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit() # terminado a aplicação pygame
                sys.exit()    # sai pela rotina do sistema

            
            if evento.type == pygame.KEYDOWN:   #funções de cada tecla
                if evento.key == pygame.K_LEFT:
                    delta_cobra["esquerda"] = 1
                elif evento.key == pygame.K_RIGHT:
                    delta_cobra["direita"] = 1
                elif evento.key == pygame.K_UP:
                    delta_cobra["acima"] = 1
                elif evento.key == pygame.K_DOWN:
                    delta_cobra["abaixo"] = 1

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                    delta_cobra["esquerda"] = 0
                if evento.key == pygame.K_RIGHT:
                    delta_cobra["direita"] = 0
                elif evento.key == pygame.K_UP:
                    delta_cobra["acima"] = 0
                elif evento.key == pygame.K_DOWN:
                    delta_cobra["abaixo"] = 0
 
        surf.fill(CINZA) # preenche a tela com a cor preta  
        
        pos_cobra[0] += (delta_cobra["direita"] - delta_cobra["esquerda"]) * velocidade_cobra * delta_time
        pos_cobra[1] += (delta_cobra["abaixo"] - delta_cobra["acima"]) * velocidade_cobra * delta_time
            
        if pos_cobra[0]>surf.get_width()-Snake.get_width():
                pygame.quit()
                sys.exit()
        elif pos_cobra[0]<0:
                pygame.quit()
                sys.exit()
        if pos_cobra[1]>surf.get_height()-Snake.get_width():
                pygame.quit()
                sys.exit()
        if pos_cobra[1]<0:
                pygame.quit()
                sys.exit()
        if pos_cobra == pos_maca:
            x = random.randint()
            y = random.randint()
            pos_maca = [x,y]

        surf.blit(Snake, pos_cobra)
        surf.blit(apple, pos_maca)
        pygame.display.flip() # faz a atualização da tela
        print(pos_cobra,pos_maca)
if __name__ == '__main__':
    main()