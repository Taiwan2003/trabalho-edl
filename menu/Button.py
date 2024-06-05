import pygame
from pygame.locals import *

class Button():
    def __init__(self,x,y,image,escala):
        largura=image.get_width()
        altura=image.get_height()
        self.image=pygame.transform.scale(image,(int(largura * escala),int(altura * escala)))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.click=False

    def draw(self,tela):
        action=False
        tela.blit(self.image,(self.rect.x,self.rect.y))
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.click ==False:
                self.click=True
                action=True

        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False


        return action
