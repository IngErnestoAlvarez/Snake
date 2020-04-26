import sys
import pygame
from clases import *


def main():

    pygame.init()

    screen = pygame.display.set_mode(size=(ANCHO, ALTO+30), display=1)

    pygame.display.set_caption("Snake")

    clock = pygame.time.Clock()

    cabeza = Cabeza()
    cola = Cola(cabeza)
    comida = Comida(cabeza=cabeza, cola=cola)

    puntaje = 0

    jugando = True

    ###############################################################
    # ##################### COMIENZOOOO   #########################
    ###############################################################

    titleFont = pygame.font.Font('freesansbold.ttf', 80)
    start = False
    screen.fill(MADERA)

    # Creo titulo "JUGAR"
    titulo = titleFont.render("JUGAR", True, BLACK, MADERA)
    titulox = (ANCHO//4)+40
    tituloy = (ALTO//4)+80

    screen.blit(titulo, (titulox, tituloy))
    pygame.display.flip()

    while not start:
        clock.tick(TICK)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            start = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if(pygame.mouse.get_pressed()[0]):
            position = pygame.mouse.get_pos()
            if position[0] > titulox and position[0] < (titulox+120):
                if position[1] > tituloy and position[1] < tituloy+80:
                    start = True

        pygame.time.delay(DELAY)

    # Fuente del puntaje
    fontScore = pygame.font.Font('freesansbold.ttf', 20)

#################################################################
# ##################### ARRANCA EL JUEGO ########################
#################################################################

    while jugando:
        if(cola.largo != 0):
            jugando = cola.mover()
            if not jugando:
                break
        clock.tick(TICK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            cabeza.cambiarDireccion("abajo")
            pygame.time.delay(10)
        if keys[pygame.K_UP]:
            cabeza.cambiarDireccion("arriba")
            pygame.time.delay(10)
        if keys[pygame.K_RIGHT]:
            cabeza.cambiarDireccion("derecha")
            pygame.time.delay(10)
        if keys[pygame.K_LEFT]:
            cabeza.cambiarDireccion("izquierda")
            pygame.time.delay(10)

        screen.fill(WHITE)

        cabeza.mover()

        # Dibuja la comida
        pygame.draw.rect(screen,  # En donde
                         RED,  # Color y abajo la posicion(1,2) y tamaño(3,4)
                         [comida.posx*block, comida.posy*block, block, block])

        # Dibuja la cabeza
        pygame.draw.rect(screen,
                         GREEN,
                         [cabeza.posx*block, cabeza.posy*block, block, block])

        # Dibuja la cola
        if(cola.largo != 0):
            for i in range(0, cola.largo):
                pygame.draw.rect(screen,
                                 BLUE,
                                 [cola.posiciones[i][0]*block,
                                  cola.posiciones[i][1]*block,
                                  block,
                                  block])

        if(comida.esComida(cabeza)):
            comida = Comida(cabeza=cabeza, cola=cola)
            cola.sumarCola()
            puntaje += 1
        texto = fontScore.render("puntaje: "+str(puntaje), True, BLACK, WHITE)

        screen.blit(texto, (ANCHO//2, ALTO))
        pygame.time.delay(DELAY)

        pygame.display.flip()

if __name__ == '__main__':
    main()
