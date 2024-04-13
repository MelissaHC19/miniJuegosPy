
import pygame
from time import sleep

pygame.init()

#variables
def pong():
    tamano=(800,600)
    altoplayer=90
    anchoplayer=15
    negro=(0,0,0)
    blanco=(255,255,255)
    azul=(0,0,255)
    rojo=(255,0,0)
    PuntajeP1=0
    PuntajeP2=0

    pygame.font.init()
    Fuente=pygame.font.SysFont("Gotic", 50)
    Fuente2=pygame.font.SysFont("Gotic", 30)
    Fuente3=pygame.font.SysFont("Marker Felt", 40)

    #Imagen de fondo
    fondo=pygame.image.load("fondopong.png")

    #Raquetas y pelota
    raqueta1 = pygame.image.load("RAQUETA1.png")
    raqueta2 = pygame.image.load("RAQUETA2.png")
    ball = pygame.image.load("Tennisball.png")

    #Ganador
    ganaJ1 = pygame.image.load("GanaJ1.png")
    ganaJ2 = pygame.image.load("GanaJ2.png")

    #Musica
    pygame.mixer.music.load("sonidoFondoPong.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1) #-1 para que se repita la musica

    ventana=pygame.display.set_mode(tamano)
    clock=pygame.time.Clock()

    #sonido
    gol=pygame.mixer.Sound("Gol.mp3")
    raqueta=pygame.mixer.Sound("Raqueta.mp3")
    rebote=pygame.mixer.Sound("Rebote.mp3")

    #jugador 1
    coorJ1_x=50
    coorJ1_y=255
    veloJ1_y=0

    #jugador 2
    coorJ2_x=750
    coorJ2_y=255
    veloJ2_y=0

    #pelota
    pelota_x=400
    pelota_y=300
    velopelota_x=4
    velopelota_y=4

    game_over=False

    while(not game_over):
        tiempo = pygame.time.get_ticks()/1000
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                #jugador 1
                if event.key==pygame.K_w:
                    veloJ1_y=-3
                if event.key==pygame.K_s:
                    veloJ1_y=3
                #jugador 2
                if event.key==pygame.K_UP:
                    veloJ2_y=-3
                if event.key==pygame.K_DOWN:
                    veloJ2_y=3
            
            if event.type==pygame.KEYUP:
                #jugador 1
                if event.key==pygame.K_w:
                    veloJ1_y=0
                if event.key==pygame.K_s:
                    veloJ1_y=0
                #jugador 2
                if event.key==pygame.K_UP:
                    veloJ2_y=0
                if event.key==pygame.K_DOWN:
                    veloJ2_y=0
        if pelota_y>590 or pelota_y <10:
            velopelota_y*=-1 
            rebote.play()  

        #pelota se va hacia la derecha
        if pelota_x>800:
            pelota_x=400
            pelota_y=300
            velopelota_x*=-1   
            velopelota_y*=-1
            PuntajeP1 +=1
            gol.play()

        #pelota se va hacia la izquierda   
        if pelota_x<0:
            pelota_x=400
            pelota_y=300
            velopelota_x*=-1   
            velopelota_y*=-1
            PuntajeP2 +=1
            gol.play()
  
        #modifica las coordenadas de los objetos
        coorJ1_y+=veloJ1_y
        coorJ2_y+=veloJ2_y
        pelota_x+=velopelota_x
        pelota_y+=velopelota_y

        #restricciones 
        if coorJ1_y<=0:
            coorJ1_y=0
        if coorJ1_y>=510:
            coorJ1_y=510
        if coorJ2_y<=0:
            coorJ2_y=0
        if coorJ2_y>=510:
            coorJ2_y=510

        '''#contador de puntaje
        if (PuntajeP1==5 or PuntajeP2==5):
            game_over=True
            pygame.time.delay(200)
            #si el jugador 1 gana
            if PuntajeP1==5:
                TextoGanador=Fuente.render("Jugador 1 Gana",1,azul)
                ventana.blit(TextoGanador,(400,300))
                pygame.display.flip()
                pygame.time.delay(2000)
            #si el jugador 2 gana
            if PuntajeP2==5:
                TextoGanador=Fuente.render("Jugador 2 Gana",1,rojo)
                ventana.blit(TextoGanador,(400,300))
                pygame.display.flip()
                pygame.time.delay(2000)'''

        #zona de dibujo
        J1=pygame.draw.rect(ventana,azul,(coorJ1_x,coorJ1_y,anchoplayer,altoplayer))
        J2=pygame.draw.rect(ventana,rojo,(coorJ2_x,coorJ2_y,anchoplayer,altoplayer))
        pelota=pygame.draw.circle(ventana,blanco,(pelota_x,pelota_y),10)
        TextoP1=Fuente.render(str(PuntajeP1),1,blanco)
        TextoP2=Fuente.render(str(PuntajeP2),1,blanco)
        ventana.blit(fondo,(0,0))
        ventana.blit(TextoP1,(200,10))
        ventana.blit(TextoP2,(600,10))

        #mostrar el tiempo que el juego esta abierto
        tiempo=int(tiempo)
        tiempo=str(tiempo)
        texto=Fuente2.render(tiempo,True,negro)
        mensaje=Fuente2.render("Tiempo:",True,negro)
        pygame.draw.rect(ventana,blanco,(330,20,150,40))
        ventana.blit(texto,(440,30))
        ventana.blit(mensaje,(340,30))

        #contador de puntaje
        if (PuntajeP1==5 or PuntajeP2==5):
            game_over=True
            pygame.time.delay(200)
            #si el jugador 1 gana
            if PuntajeP1==5:
                ventana.blit(ganaJ1,(200,150))
                tiempo = int(tiempo)
                tiempo = str(tiempo)
                texto2 = Fuente3.render("s",True,blanco)
                texto3 = Fuente3.render(tiempo,True,blanco)
                ventana.blit(texto3, (425,355))
                ventana.blit(texto2, (505,355))
                pygame.display.update()
                sleep(8)
                pygame.quit()
                game_over = False
            #si el jugador 2 gana
            if PuntajeP2==5:
                ventana.blit(ganaJ2,(200,150))
                tiempo = int(tiempo)
                tiempo = str(tiempo)
                texto2 = Fuente3.render("s",True,blanco)
                texto3 = Fuente3.render(tiempo,True,blanco)
                ventana.blit(texto3, (425,355))
                ventana.blit(texto2, (505,355))
                pygame.display.update()
                sleep(8)
                pygame.quit()
                game_over = False

        #colisiones
        if pelota.colliderect(J1) or pelota.colliderect(J2):
            velopelota_x*= -1
            raqueta.play()

        ventana.blit(raqueta1, (coorJ1_x-5,coorJ1_y))
        ventana.blit(raqueta2, (coorJ2_x+5,coorJ2_y))
        ventana.blit(ball, (pelota_x,pelota_y))

        '''#mostrar el tiempo que el juego esta abierto
        tiempo=int(tiempo)
        tiempo=str(tiempo)
        texto=Fuente2.render(tiempo,True,negro)
        mensaje=Fuente2.render("Tiempo:",True,negro)
        pygame.draw.rect(ventana,blanco,(340,20,150,40))
        ventana.blit(texto,(450,30))
        ventana.blit(mensaje,(350,30))'''

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()