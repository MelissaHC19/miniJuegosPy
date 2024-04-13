import pygame
import pong_game
import Laberinto
import time

pygame.init()

#abra intro.jpg con un  timer.tick() de 3 segundos y abra menu
def intro():
    ventana=pygame.display.set_mode((800,400))
    pygame.display.set_caption("Intro")
    imgMenu=pygame.image.load("Intro.png")
    ventana.blit((imgMenu),(0,0))
    pygame.display.update()
    #comando para inhabilitar el mouse
    #pygame.mouse.set_visible(False)
    time.sleep(5)
    menu()

def menu():
    ventana=pygame.display.set_mode((800,400))
    pygame.display.set_caption("Menu")
    imgMenu=pygame.image.load("menu.jpg")
    ventana.blit((imgMenu),(0,0))
    pygame.display.update()
    #comando para habilitar el mouse
    #pygame.mouse.set_visible(True)
    
    while True:
        for eventos in pygame.event.get():
            if eventos.type==pygame.QUIT:
                pygame.quit()
                quit()
            if eventos.type==pygame.MOUSEBUTTONDOWN:
                if eventos.button==1:
                    x,y=eventos.pos
                    if x>0 and x<800 and y>0 and y<400:
                        if x>74 and x<738 and y>106 and y<173:
                            print("Juego Pong")
                            pong_game.pong()
                        if x>74 and x<738 and y>179 and y<246:
                            print("Juego Laberinto")
                            Laberinto.laberintoGame()
                        if x>74 and x<738 and y>252 and y<319:
                            print("Salir")
                            pygame.quit()
            if eventos.type==pygame.MOUSEMOTION:
                x,y=eventos.pos
                if x>0 and x<800 and y>0 and y<400:
                    if x>74 and x<738 and y>106 and y<173:
                        imgPong=pygame.image.load("Pong.png")
                        ventana.blit(imgPong,(74,106))
                        pygame.display.update()
                    if x>74 and x<738 and y>179 and y<246:
                        imgLaberinto=pygame.image.load("Laberinto.png")
                        ventana.blit(imgLaberinto,(74,179))
                        pygame.display.update()
                    if x>74 and x<738 and y>252 and y<319:
                        imgSalir=pygame.image.load("Salir.png")
                        ventana.blit(imgSalir,(74,252))
                        pygame.display.update()

            pygame.display.update()
            ventana.blit(imgMenu,(0,0))                                
#--------------------------------------------------------------
intro()