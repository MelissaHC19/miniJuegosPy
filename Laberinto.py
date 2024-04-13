import pygame
import os
from time import sleep

def laberintoGame():
    def paredes(Ventana, Color):
        p1 = pygame.draw.rect(Ventana, Color, (200,100,5,100))
        p2 = pygame.draw.rect(Ventana, Color, (200,250,5,250))
        p3 = pygame.draw.rect(Ventana, Color, (200,500,400,5))
        p4 = pygame.draw.rect(Ventana, Color, (200,100,250,5))
        p5 = pygame.draw.rect(Ventana, Color, (500,100,100,5))
        p6 = pygame.draw.rect(Ventana, Color, (600,100,5,405))
        p7 = pygame.draw.rect(Ventana, Color, (545,150,5,50))
        p8 = pygame.draw.rect(Ventana, Color, (450,200,100,5))
        p9 = pygame.draw.rect(Ventana, Color, (500,250,100,5))
        p10 = pygame.draw.rect(Ventana, Color, (200,200,50,5))
        p11 = pygame.draw.rect(Ventana, Color, (250,200,5,55))
        p12 = pygame.draw.rect(Ventana, Color, (200,300,100,5))
        p13 = pygame.draw.rect(Ventana, Color, (295,250,5,50))
        p14 = pygame.draw.rect(Ventana, Color, (300,250,50,5))
        p15 = pygame.draw.rect(Ventana, Color, (345,150,5,100))
        p16 = pygame.draw.rect(Ventana, Color, (250,150,100,5))
        p17 = pygame.draw.rect(Ventana, Color, (295,150,5,55))
        p18 = pygame.draw.rect(Ventana, Color, (395,150,50,5))
        p19 = pygame.draw.rect(Ventana, Color, (445,105,5,200))
        p20 = pygame.draw.rect(Ventana, Color, (350,300,155,5))
        p21 = pygame.draw.rect(Ventana, Color, (345,300,5,150))
        p22 = pygame.draw.rect(Ventana, Color, (295,450,55,5))
        p23 = pygame.draw.rect(Ventana, Color, (395,250,5,50))
        p24 = pygame.draw.rect(Ventana, Color, (350,200,50,5))
        p25 = pygame.draw.rect(Ventana, Color, (500,105,5,50))
        p26 = pygame.draw.rect(Ventana, Color, (250,350,100,5))
        p27 = pygame.draw.rect(Ventana, Color, (250,400,50,5))
        p28 = pygame.draw.rect(Ventana, Color, (250,400,5,100))
        p29 = pygame.draw.rect(Ventana, Color, (545,250,5,100))
        p30 = pygame.draw.rect(Ventana, Color, (395,350,155,5))
        p31 = pygame.draw.rect(Ventana, Color, (395,355,5,100))
        p32 = pygame.draw.rect(Ventana, Color, (400,400,150,5))
        p33 = pygame.draw.rect(Ventana, Color, (445,450,105,5))
        p34 = pygame.draw.rect(Ventana, Color, (445,450,5,50))

        paredes = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34]

        return paredes

    pygame.init()
    pygame.font.init()
    tamano = (800,600)
    Negro = (0,0,0)
    Blanco = (255,255,255)

    #Musica
    pygame.mixer.music.load("Laberinto/Sonidos/musicalaberinto.mp3")
    pygame.mixer.music.play(-1)#-1 para que se repita la musica

    #Jugador 1
    AltoPlayer = 25
    AnchoPlayer = 25
    posX = 200
    posY = 220
    velX = 0
    velY = 0
    movi = 1
    direccion = 'right'
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("Gotic", 30)
    fuente2 = pygame.font.SysFont("Courier New", 40, True)
    Iniciar = True
    nvidas = 3


    #Imagen de fondo
    imgPasto = pygame.image.load(os.path.join('Laberinto/Imagenes/Grass.png'))

    #Imagen de premio
    mouse = pygame.image.load(os.path.join('Laberinto/Imagenes/Mouse.png'))

    #Imagenes del movimiento del jugador
    jugador1 = pygame.image.load(os.path.join("Laberinto/Imagenes/Right (1).png"))
    right1 = pygame.image.load(os.path.join("Laberinto/Imagenes/Right (1).png"))
    right2 = pygame.image.load(os.path.join("Laberinto/Imagenes/Right (2).png"))
    right3 = pygame.image.load(os.path.join("Laberinto/Imagenes/Right (3).png"))
    left1 = pygame.image.load(os.path.join("Laberinto/Imagenes/Left (1).png"))
    left2 = pygame.image.load(os.path.join("Laberinto/Imagenes/Left (2).png"))
    left3 = pygame.image.load(os.path.join("Laberinto/Imagenes/Left (3).png"))
    up1 = pygame.image.load(os.path.join("Laberinto/Imagenes/Up (1).png"))
    up2 = pygame.image.load(os.path.join("Laberinto/Imagenes/Up (2).png"))
    up3 = pygame.image.load(os.path.join("Laberinto/Imagenes/Up (3).png"))
    down1 = pygame.image.load(os.path.join("Laberinto/Imagenes/Down (1).png"))
    down2 = pygame.image.load(os.path.join("Laberinto/Imagenes/Down (2).png"))
    down3 = pygame.image.load(os.path.join("Laberinto/Imagenes/Down (3).png"))

    #Imagen de ganar y perder
    ganar = pygame.image.load("Laberinto/Imagenes/winGame.png")
    perder = pygame.image.load("Laberinto/Imagenes/gameOver.png")

    Ventana = pygame.display.set_mode(tamano)
    Ventana.fill(Blanco)

    #Efecto de sonido de las paredes
    efecto = pygame.mixer.Sound("Laberinto/Sonidos/sonidodepared.ogg")

    while Iniciar:
        tiempo = pygame.time.get_ticks()/1000
        vida = pygame.image.load("Laberinto/Imagenes/"+f"{nvidas}"+"vidas.png")
        if nvidas == 0:
            #Para perder el jugador, deberá perder las 3 vidas
            vida = pygame.image.load("Laberinto/Imagenes/0vidas.png")
            Ventana.blit(vida, (315, 540))
            sleep(1)
            Ventana.blit(perder, (100,102))
            pygame.display.update()
            sleep(5)
            pygame.quit()
            Iniciar = False

        if posY < 110:
            if posX > 450 and posX < 500:
                #Para ganar el jugador, deberá llegar al premio
                Ventana.blit(ganar, (100,102))
                tiempo = int(tiempo)
                tiempo = str(tiempo)
                texto2 = fuente2.render("s",True,Negro)
                texto3 = fuente2.render(tiempo,True,Negro)
                Ventana.blit(texto3, (410,375))
                Ventana.blit(texto2, (490,375))
                pygame.display.update()
                sleep(8)
                pygame.quit()
                Iniciar = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    velY = -5
                    direccion = 'up'
                if event.key == pygame.K_DOWN:
                    velY = 5
                    direccion = 'down'
                if event.key == pygame.K_LEFT:
                    velX = -5
                    direccion = 'left'
                if event.key == pygame.K_RIGHT:
                    velX = 5
                    direccion = 'right'
                
                if direccion == 'up':
                    if movi == 1:
                        jugador1 = up1
                        movi = 2
                    elif movi == 2:
                        jugador1 = up2
                        movi = 3
                    elif movi == 3:
                        jugador1 = up3
                        movi = 1
                elif direccion == 'down':
                    if movi == 1:
                        jugador1 = down1
                        movi = 2
                    elif movi == 2:
                        jugador1 = down2
                        movi = 3
                    elif movi == 3:
                        jugador1 = down3
                        movi = 1
                elif direccion == 'left':
                    if movi == 1:
                        jugador1 = left1
                        movi = 2
                    elif movi == 2:
                        jugador1 = left2
                        movi = 3
                    elif movi == 3:
                        jugador1 = left3
                        movi = 1
                elif direccion == 'right':
                    if movi == 1:
                        jugador1 = right1
                        movi = 2
                    elif movi == 2:
                        jugador1 = right2
                        movi = 3
                    elif movi == 3:
                        jugador1 = right3
                        movi = 1
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    velY = 0
                if event.key == pygame.K_DOWN:
                    velY = 0
                if event.key == pygame.K_LEFT:
                    velX = 0
                if event.key == pygame.K_RIGHT:
                    velX = 0

            #Modificar las coordenadas
            posX += velX
            posY += velY
            Ventana.fill(Blanco)

            #Restricciones jugador
            if posX < 200:
                posX = 200
            elif posX > 700:
                posX = 700
        
            if posY < 100:
                posY = 100
            elif posY > 500:
                posY = 500
            
            #Zona de dibujo
            jugador = pygame.draw.rect(Ventana, Blanco, (posX,posY-5,AnchoPlayer,AltoPlayer))
            pygame.display.set_caption("Laberinto")
            laberinto = paredes(Ventana, Negro)
            #Ventana.blit(imgPasto, (0,0))
            #Ventana.blit(vida, (315, 540))
            #Ventana.blit(jugador1, (posX, posY-5))
            #pygame.display.update()

            #Colisiones
            for laberinto in paredes(Ventana, Negro):
                if jugador.colliderect(laberinto):
                    # Si el jugador choca con una pared, regresa a la posición inicial
                    efecto.play()
                    posX = 200
                    posY = 220
                    nvidas -= 1
            Ventana.blit(imgPasto, (0,0))
            Ventana.blit(vida, (315,540))
            Ventana.blit(mouse, (465,90))
            Ventana.blit(jugador1, (posX, posY-5))

        #Contar y mostrar tiempo que se demora llegando al final
        tiempo = int(tiempo)
        tiempo = str(tiempo)
        texto = fuente.render(tiempo,True,Negro)
        mensaje = fuente.render("Tiempo:",True,Negro)
        pygame.draw.rect(Ventana,Blanco,(340,20,150,40))
        Ventana.blit(texto, (450,30))
        Ventana.blit(mensaje, (350,30))
        pygame.display.update()