import pygame, random
from pygame.locals import *
import functions
from functions import WIDTH, HEIGHT
from main import WHITE

#class casilla---------------------------------------------------------
class Casilla(pygame.sprite.Sprite):
    def __init__(self, dat:int= 0, pos:tuple= (0, 0, 0, 0, 0, 0)):
        super().__init__()

        self._dato = dat
        self.picture = 'Imagenes/Casilla.png' # localización de la imagen a ser usada para la clase
        self.image = functions.load_image(self.picture, 100, 100, True) # convertir la imagen en un formato aceptado por pygame para ser tratado
        self.rect = self.image.get_rect()

        if pos[0] != None:
            self.rect.top = pos[0]
        if pos[1] != None:
            self.rect.bottom = pos[1]
        if pos[2] != None:
            self.rect.right = pos[2]
        if pos[3] != None:
            self.rect.left = pos[3]
        if pos[4] != None:
            self.rect.centerx = pos[4]
        if pos[5] != None:
            self.rect.centery = pos[5]
        

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
    def __init__(self, fila=3, columna=3, pos:tuple = (0, 0, 0, 0, 0, 0)):
        super().__init__()
        # 220
        self.tamx = 330
        self.tamy = 330
        self.picture = 'Imagenes/BLUE.png' # localización de la imagen a ser usada para la clase
        self.image = functions.load_image(self.picture, self.tamx, self.tamy) # convertir la imagen en un formato aceptado por pygame para ser tratado
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        if pos[0] != None:
            self.rect.top = pos[0]
        if pos[1] != None:
            self.rect.bottom = pos[1]
        if pos[2] != None:
            self.rect.right = pos[2]
        if pos[3] != None:
            self.rect.left = pos[3]
        if pos[4] != None:
            self.rect.centerx = pos[4]
        if pos[5] != None:
            self.rect.centery = pos[5]

        self.filas=fila
        self.columnas=columna
        self.matriz=[]
        self.casillas_group = pygame.sprite.Group()

        self.pos_casillas = {
                    1: (self.rect.top, None, self.rect.right, None, None, None), 
                    2: (self.rect.top, None, None, None, self.rect.centerx, None),
                    3: (self.rect.top, None, None, self.rect.left, None, None),

                    4: (None, None, self.rect.right, None, None, self.rect.centery),
                    5: (None, None, None, None, self.rect.centerx, self.rect.centery),
                    6: (None, None, None, self.rect.left, None, self.rect.centery),
                    
                    7: (None, self.rect.bottom, self.rect.right, None, None, None),
                    8: (None, self.rect.bottom, None, None, self.rect.centerx, None),
                    9: (None, self.rect.bottom, None, self.rect.left, None, None)
                    }
  
        self.contador = 1
        for f in range(self.filas):
            lis=[] #crea la lista vacia donde guarda cada fila
            for c in range(self.columnas):
                cas = Casilla(0, self.pos_casillas[self.contador]) #crea un objeto casilla
                self.casillas_group.add(cas)
                lis.append(cas) #lo agrega a la lista de fila
                self.contador += 1
            self.matriz.append(lis)

            
           
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
    
    def casillitas(self):
        lista=[] 
        for i in range(self.filas):
            for j in range(self.columnas):
                lista.append(self.matriz[i][j])
        return lista
    

    def draw(self, surface): #Método para mostrar el sprint en pantalla
                             # surface = pantalla
        surface.blit(self.image, self.rect)
        self.casillas_group.draw(surface)
        # for i in range(self.filas):
        #     for j in range(self.columnas):
        #         (self.matriz[i][j]).draw(surface)

        

class Cuadricula(pygame.sprite.Sprite):
    def __init__(self, filas= 3, columnas= 3, pos:tuple = (0, 0)):
        super().__init__()

        self.picture = 'Imagenes/BLACK.png' # localización de la imagen a ser usada para la clase
        self.image = functions.load_image(self.picture, WIDTH/1.8, WIDTH/1.8, True) # convertir la imagen en un formato aceptado por pygame para ser tratado
        self.rect = self.image.get_rect()

        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

        self.filas = filas
        self.columnas = columnas
        self.matriz = []
        self.subcuadricula_group = pygame.sprite.Group()

        self.contador = 1
        self.pos_subcuadricula = {
                    1: (self.rect.top, None, self.rect.right, None, None, None), 
                    2: (self.rect.top, None, None, None, self.rect.centerx, None),
                    3: (self.rect.top, None, None, self.rect.left, None, None),

                    4: (None, None, self.rect.right, None, None, self.rect.centery),
                    5: (None, None, None, None, self.rect.centerx, self.rect.centery),
                    6: (None, None, None, self.rect.left, None, self.rect.centery),
                    
                    7: (None, self.rect.bottom, self.rect.right, None, None, None),
                    8: (None, self.rect.bottom, None, None, self.rect.centerx, None),
                    9: (None, self.rect.bottom, None, self.rect.left, None, None)
                    }

        for f in range(self.filas):
            lis = []
            for c in range(self.columnas):
                sub = Subcuadricula(self.filas, self.columnas, self.pos_subcuadricula[self.contador])
                self.subcuadricula_group.add(sub)
                lis.append(sub)
                self.contador += 1
            self.matriz.append(lis)

    def draw(self, surface): #Método para mostrar el sprint en pantalla
                             # surface = pantalla

        surface.blit(self.image, self.rect)
        for i in range(self.filas):
            for j in range(self.columnas):
                (self.matriz[i][j]).draw(surface)

 
