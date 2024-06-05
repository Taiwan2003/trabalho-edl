import pygame
import sys
import csv
from settings import *

# Inicializa o Pygame
pygame.init()

# Configura a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Roguelike")

# Relógio para controlar a taxa de frames
clock = pygame.time.Clock()

# Criação do personagem
class Personagem():
    def __init__(self, x, y, w, h, cor, forca, vida, velocidade):
        self.rect = pygame.Rect(x, y, w, h)
        self.cor = cor
        self.forca = forca
        self.vida = vida
        self.velocidade = velocidade
        self.vel_y = 0
        self.pulando = False
    
    def movimentar(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.velocidade
        if keys[pygame.K_a]:
            self.rect.x -= self.velocidade
        if keys[pygame.K_SPACE] and not self.pulando:
            self.pulando = True
            self.vel_y = -15
        
    def gravidade(self):
        if self.pulando:
            self.vel_y += 1
            self.rect.y += self.vel_y
            if self.rect.y == SCREEN_HEIGHT/2:
                self.pulando = False
    
    def update(self):
        self.movimentar()
        self.gravidade()
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.cor, self.rect)



def main():
    running = True
    
    personagem = Personagem(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 50, 50, (0, 0, 255), forca=10, vida=100, velocidade=5)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualiza a tela
        screen.fill(BLACK)
        
        
        # Atualiza e desenha o personagem
        personagem.update()
        personagem.draw(screen)
        
        pygame.draw.rect(screen, (255,255,255),(0,351,800,50))
        pygame.display.flip()

        # Controle da taxa de frames
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
