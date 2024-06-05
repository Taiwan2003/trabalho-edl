import pygame
import sys
from pytmx import load_pygame, TiledTileLayer
from settings import *

# Inicializa o Pygame
pygame.init()

# Configura a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Roguelike")

# Relógio para controlar a taxa de frames
clock = pygame.time.Clock()

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
        
    def gravidade(self, platforms):
        if self.pulando:
            self.vel_y += 1
            self.rect.y += self.vel_y
            
            # Detectar colisão com plataformas
            collision_indices = self.rect.collidelistall(platforms)
            if collision_indices:
                for index in collision_indices:
                    platform = platforms[index]
                    if self.vel_y > 0:  # Caindo
                        self.rect.bottom = platform.top
                        self.pulando = False
                        self.vel_y = 0

    def update(self, platforms):
        self.movimentar()
        self.gravidade(platforms)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.cor, self.rect)
    
def load_map(filename):
    return load_pygame(filename)

def draw_map(tmx_data):
    platforms = []
    for layer in tmx_data.visible_layers:
        if isinstance(layer, TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))
                    # Adiciona a plataforma à lista
                    tile_rect = pygame.Rect(x * tmx_data.tilewidth, y * tmx_data.tileheight, tmx_data.tilewidth, tmx_data.tileheight)
                    platforms.append(tile_rect)
    return platforms

def main():
    tmx_data = load_map('assets/maps/4.tmx')
    running = True
    
    personagem = Personagem(100, 100, 50, 50, (0, 0, 255), forca=10, vida=100, velocidade=5)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualiza a tela
        screen.fill(BLACK)
        platforms = draw_map(tmx_data)
        
        # Atualiza e desenha o personagem
        personagem.update(platforms)
        personagem.draw(screen)

        pygame.display.flip()

        # Controle da taxa de frames
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
