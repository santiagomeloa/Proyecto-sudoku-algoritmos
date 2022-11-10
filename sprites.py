import pygame, random
from pygame.locals import *
import functions

#class casilla---------------------------------------------------------
class Casilla(pygame.sprite.Sprite):
    def __init__(self, dat= 0):
        super().__init__()

        self._dato = dat
        self.picture = 'images/Casilla.png' # localización de la imagen a ser usada para la clase
        self.image = functions.load_image(self.picture) # convertir la imagen en un formato aceptado por pygame para ser tratado
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(0, 800)
        self.rect.centery = random.randint(0, 800)

    @property
    def dato(self):
        return self._dato

    @dato.setter
    def dato(self, dato):
        self._dato = dato
 
    def printc(self):
        print(self._dato, end= " ") #imprime el número y sigue en la misma linea

    def draw(self, surface): #Método para mostrar el sprint en pantalla
                             # surface = pantalla
        surface.blit(self.image, self.rect)

#class subcuadricula--------------------------------------------------
class Subcuadricula(pygame.sprite.Sprite):
    def __init__(self, fila=3, columna=3):
        super().__init__()
        self.filas=fila
        self.columnas=columna
        self.matriz=[]
        for i in range(self.columnas):
            lista=[] #crea la lista vacia donde guarda cada fila
            for j in range(self.filas):
                c=Casilla() #crea un objeto casilla
                lista.append(c) #lo agrega a la lista de fila
            self.matriz.append(lista)
            lista=[]
           
    def prin(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j].printc()
            print("\n")
           
           
    def insert(self, fila, columna, num):
        c = self.matriz[fila][columna]
        c.setCasilla(num)
       
    def search(self, num):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j].getCasilla()==num:
                    return True
        return False

    def draw(self, surface): #Método para mostrar el sprint en pantalla
                             # surface = pantalla
        for i in range(self.filas):
            for j in range(self.columnas):
                (self.matriz[i][j]).draw(surface)
        

class Cuadricula(pygame.sprite.Sprite):
    def __init__(self, filas= 3, columnas= 3):
        super().__init__()

        self.filas = filas
        self.columnas = columnas
        self.matriz = []

        for f in range(self.filas):
            lis = []
            for c in range(self.columnas):
                sub = Subcuadricula()
                lis.append(sub)
            self.matriz.append(lis)

    def draw(self, surface): #Método para mostrar el sprint en pantalla
                             # surface = pantalla
        for i in range(self.filas):
            for j in range(self.columnas):
                (self.matriz[i][j]).draw(surface)
 