import pygame
from pygame.locals import *
from sys import exit
import Button
from db import Banco

#fase de desenvolvimento,sujeio a alteracoes

pygame.init()

font_titulo=pygame.font.Font("alagard.ttf",100)
font_menu_1=pygame.font.Font("alagard.ttf",40)
font_menu_2=pygame.font.Font("alagard.ttf",60)

titulo=font_titulo.render("Forsaken Legacy",True,(255,255,255))
saves=font_menu_1.render("Saves",True,(255,255,255))
texto_nome=font_menu_2.render("Nome:",True,(255,255,255))

pausado=False
estado_menu="menu principal"

menu=pygame.display.set_mode((1280,720))
pygame.display.set_caption('Forsaken Legacy')

jogar_img=pygame.image.load('jogar1.png').convert_alpha()
carregar_img=pygame.image.load('carregar2.png').convert_alpha()
sair_img=pygame.image.load('sair2.png').convert_alpha()
confirmar_img=pygame.image.load('confirmar1.png').convert_alpha()
deletar_img=pygame.image.load('deletar1.png').convert_alpha()

#botoes do menu principal
jogar=Button.Button(500,300,jogar_img,0.7)
carregar=Button.Button(500,420,carregar_img,0.7)
sair=Button.Button(500,540,sair_img,0.7)

#botao para inciar um save novo
iniciar=Button.Button(500,400,jogar_img,0.7)

#botoes de carregamento de saves
carregar_botao1=Button.Button(1000,150,carregar_img,0.3)
carregar_botao2=Button.Button(1000,250,carregar_img,0.3)
carregar_botao3=Button.Button(1000,350,carregar_img,0.3)

#botoes de deletar saves
deletar_botao1=Button.Button(1000,200,deletar_img,0.3)
deletar_botao2=Button.Button(1000,300,deletar_img,0.3)
deletar_botao3=Button.Button(1000,400,deletar_img,0.3)

text_font=pygame.font.Font(None,50)
input_box=pygame.Rect(230,215,600,50)
line_rect=pygame.Rect(230,250,600,3)
username=''


while True:
    menu.fill((66,66,111))

    if estado_menu=="menu principal":
            menu.blit(titulo,(250,100))
            if jogar.draw(menu):
                estado_menu="jogar"
            if carregar.draw(menu):
                estado_menu="carregar"
            if sair.draw(menu):
                pygame.quit()
                exit()
    if estado_menu=="carregar":
            menu.blit(saves,(50,50))
            lista_saves=Banco.lista_saves_strings()
            if len(lista_saves)==1:
                carregar_save1=font_menu_1.render(lista_saves[0],True,(255,255,255))
                menu.blit(carregar_save1,(50,150))
                if carregar_botao1.draw(menu):
                    pass
            elif len(lista_saves)==2:
                carregar_save1=font_menu_1.render(lista_saves[0],True,(255,255,255))
                carregar_save2=font_menu_1.render(lista_saves[1],True,(255,255,255))
                menu.blit(carregar_save1,(50,150))
                menu.blit(carregar_save2,(50,250))
                if carregar_botao1.draw(menu):
                    pass
                if carregar_botao2.draw(menu):
                    pass
            elif len(lista_saves)==3:
                carregar_save1=font_menu_1.render(lista_saves[0],True,(255,255,255))
                carregar_save2=font_menu_1.render(lista_saves[1],True,(255,255,255))
                carregar_save3=font_menu_1.render(lista_saves[2],True,(255,255,255))
                menu.blit(carregar_save1,(50,150))
                menu.blit(carregar_save2,(50,250))
                menu.blit(carregar_save3,(50,350))
                if carregar_botao1.draw(menu):
                    pass
                if carregar_botao2.draw(menu):
                    pass
                if carregar_botao3.draw(menu):
                    pass
                
    if estado_menu=="jogar":
            menu.blit(texto_nome,(50,200))
            text_surface=text_font.render(username,True,(255,255,255))
            menu.blit(text_surface,input_box)
            pygame.draw.rect(menu,(66,66,111),input_box,2)
            pygame.draw.rect(menu,(255,255,255),line_rect)
            if iniciar.draw(menu) and len(username)>0:
                if Banco.salvar(username,1):
                    pass
                else:
                   estado_menu="erro"

    if estado_menu=="erro":
             menu.fill((0,0,0))
             erro1=font_menu_1.render("todos os slots estao ocupados",True,(255,255,255))
             erro2=font_menu_1.render("deseja liberar um slot de memoria?",True,(255,255,255))
             menu.blit(erro1,(50,50))
             menu.blit(erro2,(45,100))
             lista_saves=Banco.lista_saves_strings()
             deletar_lista=Banco.lista_saves()
             carregar_save1=font_menu_1.render(lista_saves[0],True,(255,255,255))
             carregar_save2=font_menu_1.render(lista_saves[1],True,(255,255,255))
             carregar_save3=font_menu_1.render(lista_saves[2],True,(255,255,255))
             menu.blit(carregar_save1,(50,200))
             menu.blit(carregar_save2,(50,300))
             menu.blit(carregar_save3,(50,400))
             if deletar_botao1.draw(menu):
                if Banco.deletar(deletar_lista[0]):
                    estado_menu="sucesso"
             if deletar_botao2.draw(menu):
                if Banco.deletar(deletar_lista[1]):
                    estado_menu="sucesso"
             if deletar_botao3.draw(menu):
                if Banco.deletar(deletar_lista[2]):
                    estado_menu="sucesso"

    if estado_menu=="sucesso":
            menu.fill((0,0,0))
            sucesso=font_menu_1.render("deletado com sucesso",True,(255,255,255))
            menu.blit(sucesso,(300,250))
            Banco.salvar(username,1)
             
                
    for event in pygame.event.get():
       if event.type == pygame.KEYDOWN:
            if estado_menu=="jogar":
                if event.key==pygame.K_BACKSPACE:
                    username=username[:-1]
                elif event.key==pygame.K_ESCAPE:
                   estado_menu="menu principal"
                else:
                    if len(username)<20:
                        username+=event.unicode
                        
            else:
                if event.key == pygame.K_a and pausado == False:
                   pausado=True
                elif event.key == pygame.K_a and pausado == True:
                   pausado=False
                elif event.key == pygame.K_ESCAPE and estado_menu=="carregar":
                   estado_menu="menu principal"
                elif event.key == pygame.K_ESCAPE and estado_menu=="erro":
                    estado_menu="jogar"
                
       if event.type == QUIT:
           pygame.quit()
           exit()
            
    pygame.display.update()
            
