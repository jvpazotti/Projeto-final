import os
import sys
import pygame

CINZA = (127, 127, 127)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

class Caneca(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        arquivo = os.path.join('/Users/Gamer/OneDrive - Insper - Institudo de Ensino e Pesquisa/Projeto Final python/imagens', 'Snake.png')
        try:
            self.image = pygame.image.load(arquivo).convert_alpha()
        except pygame.error:
            print('Erro ao tentar ler imagem: Snake.png')
            sys.exit()

        self.rect = self.image.get_rect()

        self.velocidade = [0.2, 0.27]

    def update(self, delta_time):
        largura, altura = pygame.display.get_surface().get_size()
        self.rect.x += self.velocidade[0] * delta_time
        self.rect.y += self.velocidade[1] * delta_time
        if self.rect.right > largura :
            self.velocidade[0] = -self.velocidade[0]
            self.rect.right = largura
        elif self.rect.x < 0:
            self.velocidade[0] = -self.velocidade[0]
            self.rect.x = 0
        if self.rect.bottom > altura:
            self.velocidade[1] = -self.velocidade[1]
            self.rect.bottom = altura
        elif self.rect.y < 0:
            self.velocidade[1] = -self.velocidade[1]
            self.rect.y = 0


def main():
    """Rotina principal do Exemplo de Jogo com pygame."""

    pygame.init()  # inicia rotinas do pygame

    surf = pygame.display.set_mode((400, 400)) # cria superficie para o jogo

    pygame.display.set_caption("Exemplo pygame")

    # caneca = Caneca()
    # caneca2 = Caneca()
    # caneca2.rect.x = 100

    sprites = pygame.sprite.Group()
    # sprites.add(caneca)
    # sprites.add(caneca2)

    pos_circulo = [200, 200]
    delta_circulo = {"esquerda":0, "direita":0, "acima":0, "abaixo":0}
    velocidade_circulo = 0.3

    barra_espaco = False
    botao_mouse = False

    clock = pygame.time.Clock() # objeto para controle da atualizações de imagens

    pygame.time.set_timer(pygame.USEREVENT, 1000) # acontece a cada 1 segundo

    # Game Loop
    while True:
        delta_time = clock.tick(60) # garante um FPS máximo de 60Hz
        
        # Coleta de eventos
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                pygame.quit() # terminado a aplicação pygame
                sys.exit()    # sai pela rotina do sistema
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    delta_circulo["esquerda"] = 1
                elif evento.key == pygame.K_RIGHT:
                    delta_circulo["direita"] = 1
                elif evento.key == pygame.K_UP:
                    delta_circulo["acima"] = 1
                elif evento.key == pygame.K_DOWN:
                    delta_circulo["abaixo"] = 1
                elif evento.key == pygame.K_SPACE:
                    barra_espaco = True

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT:
                    delta_circulo["esquerda"] = 0
                if evento.key == pygame.K_RIGHT:
                    delta_circulo["direita"] = 0
                elif evento.key == pygame.K_UP:
                    delta_circulo["acima"] = 0
                elif evento.key == pygame.K_DOWN:
                    delta_circulo["abaixo"] = 0
                elif evento.key == pygame.K_SPACE:
                    barra_espaco = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                botao_mouse = True
            
            if evento.type == pygame.MOUSEBUTTONUP:
                botao_mouse = False

            if evento.type == pygame.MOUSEMOTION:
                pos_circulo = list(pygame.mouse.get_pos())

            if evento.type == pygame.USEREVENT:
                Caneca(sprites) # criando sprites da caneca e já colocando no grupo de sprites

        surf.fill(CINZA) # preenche a tela com a cor preta

        # Desenha Caneca
        sprites.update(delta_time)
        sprites.draw(surf)
        
        # Desenho do Círculo
        
        pygame.display.flip() # faz a atualização da tela

if __name__ == "__main__":
    main()