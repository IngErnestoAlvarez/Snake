import random

block = 30

grilla = (30, 20)

ANCHO = grilla[0]*block
ALTO = grilla[1]*block

DELAY = 70
TICK = 70

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (100, 180, 70)
GREEN = (32, 160, 70)
RED = (152, 24, 21)
MADERA = (238, 208, 157)


class Cabeza(object):

    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.direccion = "derecha"

    def cambiarDireccion(self, direccionNueva):
        if((self.direccion == "izquierda") and (direccionNueva == "derecha")):
            return
        if((self.direccion == "derecha") and (direccionNueva == "izquierda")):
            return
        if((self.direccion == "abajo") and (direccionNueva == "arriba")):
            return
        if((self.direccion == "arriba") and (direccionNueva == "abajo")):
            return

        self.direccion = direccionNueva

    def mover(self):
        if(self.direccion == "izquierda"):
            self.moveLeft()
        if(self.direccion == "derecha"):
            self.moveRight()
        if(self.direccion == "arriba"):
            self.moveUp()
        if(self.direccion == "abajo"):
            self.moveDown()

    def moveRight(self):
        if ((self.posx*block + block) >= ANCHO):
            self.posx = 0
        else:
            self.posx += 1

    def moveLeft(self):
        if (self.posx <= 0):
            self.posx = (grilla[0]-1)
        else:
            self.posx -= 1

    def moveUp(self):
        if (self.posy <= 0):
            self.posy = (grilla[1]-1)
        else:
            self.posy -= 1

    def moveDown(self):
        if ((self.posy*block+block) >= ALTO):
            self.posy = 0
        else:
            self.posy += 1


class Cola(object):

    def __init__(self, cabeza):
        self.cabeza = cabeza
        self.largo = 0
        self.posiciones = []
        self.direccion = "izquierda"

    def sumarCola(self):
        if(self.largo == 0):
            self.posiciones.append([self.cabeza.posx, self.cabeza.posy])
        else:
            self.posiciones.append([self.posiciones[self.largo-1][0], self.posiciones[self.largo-1][1]])
        self.largo += 1

    def cambiarDireccion(self, direccionNueva):
        if((self.direccion == "izquierda") and (direccionNueva == "derecha")):
            return
        if((self.direccion == "derecha") and (direccionNueva == "izquierda")):
            return
        if((self.direccion == "abajo") and (direccionNueva == "arriba")):
            return
        if((self.direccion == "arriba") and (direccionNueva == "abajo")):
            return

        self.direccion = direccionNueva

    def mover(self):
        if(self.largo == 0):
            return True
        for i in range(1, self.largo):
            if((self.posiciones[self.largo-i][0] == self.cabeza.posx) and (self.posiciones[self.largo-i][1] == self.cabeza.posy)):
                return False
            self.posiciones[self.largo-i][0] = self.posiciones[self.largo-i-1][0]
            self.posiciones[self.largo-i][1] = self.posiciones[self.largo-i-1][1]
        self.posiciones[0][0] = self.cabeza.posx
        self.posiciones[0][1] = self.cabeza.posy
        return True


class Comida(object):

    def __init__(self, cabeza, cola):
        diferente = False
        while not diferente:
            diferente = True
            x = random.randrange(0, grilla[0])
            y = random.randrange(0, grilla[1])
            if((cabeza.posx == x) and (cabeza.posy == y)):
                diferente = False
            for pos in cola.posiciones:
                if((pos[0] == x) and (pos[1] == y)):
                    diferente = False

        self.posx = x
        self.posy = y

    def esComida(self, cabeza):
        if(self.posx == cabeza.posx):
            if(self.posy == cabeza.posy):
                return True
        return False
