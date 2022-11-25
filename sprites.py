import pygame, random
from pygame.locals import *
import functions
from functions import HEIGHT, WHITE, WIDTH
from dokusan import generators
import numpy as np


#Clase numeros botones
class Numbers(pygame.sprite.Sprite):
    def __init__(self, image, x, y, number:int):
        super().__init__()

        self.image = pygame.transform.scale(image, (100, 100))
        self.pos_x = x
        self.pos_y = y
        self.number = number
        self.rect = self.image.get_rect()
        self.rect.topleft = ((self.pos_x, self.pos_y))

    def get_number(self):
        return self.number

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return self.number
        else:
            return 0

#Clase numeros casillas
class Numbers_casillas(pygame.sprite.Sprite):
    def __init__(self, x, y, number:int=0):
        super().__init__()
        
        self.tam = WIDTH/50
        self.number = number
        self.num_images = {
            0:"Imagenes/WHITE.png",
            1:"Imagenes/1.png",
            2:"Imagenes/2.png",
            3:"Imagenes/3.png",
            4:"Imagenes/4.png",
            5:"Imagenes/5.png",
            6:"Imagenes/6.png",
            7:"Imagenes/7.png",
            8:"Imagenes/8.png",
            9:"Imagenes/9.png",
        }
        self.image = functions.load_image(self.num_images[self.number], self.tam, self.tam, True) # convertir la imagen en un formato aceptado por pygame para ser tratado
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        # self.rect.topleft = ((self.pos_x, self.pos_y))

    def set_number(self, num:int):
        self.number = num
        self.update()

    def get_number(self):
        return self.number

    def update(self):
        self.image = functions.load_image(self.num_images[self.number], self.tam, self.tam, True) # convertir la imagen en un formato aceptado por pygame para ser tratado


    def draw(self, surface):
        surface.blit(self.image, self.rect)


#class casilla---------------------------------------------------------
class Casilla(pygame.sprite.Sprite):
    def __init__(self, dat:int= 2, pos:tuple= (0, 0, 0, 0, 0, 0)):
        super().__init__()

        self.tam = WIDTH/20.2
        self.picture = 'Imagenes/Casilla.png' # localización de la imagen a ser usada para la clase
        self.image = functions.load_image(self.picture, self.tam, self.tam, True) # convertir la imagen en un formato aceptado por pygame para ser tratado
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
        
        self._dato = Numbers_casillas(self.rect.centerx, self.rect.centery, dat)

    def get_dato(self):
        return self._dato.get_number()

    def set_dato(self, dato:int):
        self._dato.set_number(dato)
        self.update()
 
    def printc(self):
        print(self._dato, end= " ") #imprime el número y sigue en la misma linea

    def update(self):
        self._dato.update()
        

    def draw(self, surface): #Método para mostrar el sprint en pantalla
                             # surface = pantalla
        surface.blit(self.image, self.rect)
        self._dato.draw(surface)

    def put_number(self, position, number):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.set_dato(number)

            # if(number == 1):
            #     one = Numbers_casillas(pygame.image.load('Imagenes/1.png').convert_alpha(), self.pos_x, self.pos_y, "1")
            #     one.draw(screen)
            # if(number == 2):
            #     two = Numbers_casillas(pygame.image.load('Imagenes/2.png').convert_alpha(), self.pos_x, self.pos_y, "2")
            #     two.draw(screen)
            # if(number == 3):
            #     three = Numbers_casillas(pygame.image.load('Imagenes/3.png').convert_alpha(), self.pos_x, self.pos_y, "3")
            #     three.draw(screen)
            # if(number == 4):
            #     four = Numbers_casillas(pygame.image.load('Imagenes/4.png').convert_alpha(), self.pos_x, self.pos_y, "4")
            #     four.draw(screen)
            # if(number == 5):
            #     five = Numbers_casillas(pygame.image.load('Imagenes/5.png').convert_alpha(), self.pos_x, self.pos_y, "5")
            #     five.draw(screen)
            # if(number == 6):
            #     six = Numbers_casillas(pygame.image.load('Imagenes/6.png').convert_alpha(), self.pos_x, self.pos_y, "6")
            #     six.draw(screen)
            # if(number == 7):
            #     seven = Numbers_casillas(pygame.image.load('Imagenes/7.png').convert_alpha(), self.pos_x, self.pos_y, "7")
            #     seven.draw(screen)
            # if(number == 8):
            #     eight = Numbers_casillas(pygame.image.load('Imagenes/8.png').convert_alpha(), self.pos_x, self.pos_y, "8")
            #     eight.draw(screen)
            # if(number == 9):
            #     nine = Numbers_casillas(pygame.image.load('Imagenes/9.png').convert_alpha(), self.pos_x, self.pos_y, "9")
            #     nine.draw(screen)

#class subcuadricula--------------------------------------------------
class Subcuadricula(pygame.sprite.Sprite):
    def __init__(self, fila=3, columna=3, pos:tuple = (0, 0, 0, 0, 0, 0)):
        super().__init__()
        # 220Numbers

        self.li = [2,1,0]
        self.tam = WIDTH/7.2
        self.picture = 'Imagenes/Subcuadricula.png' # localización de la imagen a ser usada para la clase
        self.image = functions.load_image(self.picture, self.tam, self.tam, True) # convertir la imagen en un formato aceptado por pygame para ser tratado
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
            print("\t")
    
    def get_dato(self, x, y):
        return self.matriz[x][y].get_dato()

    def set_dato(self, num:int, x:int, y:int):
        self.matriz[x][self.li[y]].set_dato(num)
      

    def insert(self, fila, columna, num):
        c = self.matriz[fila][columna]
        c.setCasilla(num)
       
    def revisar_sub(self, num):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j].getCasilla()==num:
                    return False
        return True

    def update(self):
        # for f in range(self.filas):
        #     for c in range(self.columnas):
        #         self.matriz[f][c].update()
        self.casillas_group.update()
    
    def casillitas(self):
        lista=[] 
        for i in range(self.filas):
            for j in range(self.columnas):
                lista.append(self.matriz[i][j])
        return lista
    
    def get_casillas_group(self):
        return self.casillas_group

    def draw(self, surface): #Método para mostrar el sprint en pantalla
                             # surface = pantalla
        surface.blit(self.image, self.rect)
        for i in range(self.filas):
            for j in reversed(range(self.columnas)):
                (self.matriz[i][j]).draw(surface)

        

class Cuadricula(pygame.sprite.Sprite):
    def __init__(self, filas= 3, columnas= 3, pos:tuple = (0, 0)):
        super().__init__()

        self.li = [2,1,0]
        self.tam = WIDTH/2.4
        self.picture = 'Imagenes/Cuadricula.png' # localización de la imagen a ser usada para la clase
        self.image = functions.load_image(self.picture, self.tam, self.tam, True) # convertir la imagen en un formato aceptado por pygame para ser tratado
        self.rect = self.image.get_rect()
        self.mat_rand = np.array(list(str(generators.random_sudoku(avg_rank=100)))).reshape(9,9).astype(int)

        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.rect.top = 0

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

    def prin(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j].prin()
            print("\n")
    
    def get_dato(self, x:int, y:int, xs:int, ys:int):
        return self.matriz[x][y].get_dato(xs, ys)

    def set_dato(self, num:int, x:int, y:int, xs:int, ys:int):
        self.matriz[x][self.li[y]].set_dato(num, xs, ys)

    # def fill_sudoku(self):
    #     random_pos = (random.choice([x for x in range(self.filas)]), random.choice([y for y in range(self.columnas)]))

    #     self.set_dato(random.choice([d for d in range(1, 10)]), random_pos[0], random_pos[1], random_pos[1], random_pos[1])
    #     print(self.get_dato(random_pos[0], random_pos[1], random_pos[0], random_pos[1])) 

    def draw(self, surface): #Método para mostrar el sprint en pantalla
                             # surface = pantalla

        surface.blit(self.image, self.rect)
        for i in range(self.filas):
            for j in reversed(range(self.columnas)):
                (self.matriz[i][j]).draw(surface)
                
    # def revisar_fila (self, pos_cua, pos_sub, num):
    #     for i in range(3):
    #         sub_cuadricula=self.matriz[pos_cua][i]
    #         for j in range(3):
                
    #             if sub_cuadricula.get_dato(pos_sub, j) == num:
    #                 return False
    #     return True
    
    # def revisar_columna(self, pos_cua, pos_sub, num):
    #     for i in range(3):
    #         sub_cuadricula=self.matriz[i][pos_cua]
    #         for j in range(3):
            
    #             if sub_cuadricula.get_dato(j, pos_sub) == num:
    #                 return False
    #     return True
                
    # def revisar_sub_cua(self, posx, posy, num):
    #     return self.matriz[posx][posy].revisar_sub(num)

    # def fill_fila(self, pos_cuax, pos_subx):
    #     lista = [1,2,3,4,5,6,7,8,9]
    #     for i in range(self.columnas):
    #         sub_cuadricula=self.matriz[pos_cuax][i]
    #         for j in range(self.columnas):
    #             num = lista.pop(0)
    #             while not self.revisar_columna(i, j, num) and not self.revisar_sub_cua(pos_cuax, i):
    #                 lista.append(num)
    #                 num = lista.pop(0)
                    
    #             sub_cuadricula.set_dato(num, pos_subx, j)

    def posible_numero(self, fila, columna, numero):
        for i in range(0, 9):
            if self.mat_rand[fila][i] == numero:
                return False

        for i in range(0, 9):
            if self.mat_rand[i][columna] == numero:
                return False

        x_sub = (fila//3)*3
        y_sub = (columna//3)*3

        for i in range(0,3):
            for j in range(0,3):
                if self.mat_rand[x_sub + i][y_sub + j] == numero:
                    return False

        return True

    def update(self):
        # for f in range(self.filas):
        #     for c in range(self.columnas):
        #         self.matriz[f][c].update()
        self.subcuadricula_group.update()

    def sudoku_solver(self):
        for filas in range(0,9):
            for columnas in range(0,9):
                if self.mat_rand[filas][columnas] == 0:
                    for numero in range(1, 10):
                        if(self.posible_numero(filas, columnas, numero)):
                            self.mat_rand[filas][columnas] = numero
                            self.sudoku_solver()
                            self.mat_rand[filas][columnas] = 0
                    return
                
    
    def generador(self):
        self.sudoku_solver()
        xs = 0
        x = 0
        y = 0
        print(self.mat_rand, end="\n")
        for f in range(9):
            
            if f<=2:
                x = 0
            elif 2<f<=5:
                x = 1
            elif 5<f<=8:
                x = 2
            for c in range(9):
                if c == 0 or c == 1 or c == 2:
                    y = 0
                elif c == 3 or c == 4 or c==5:
                    y = 1
                elif c == 6 or c == 7 or c == 8:
                    y = 2
                self.set_dato(self.mat_rand[f][c], x, y, xs, c%3)
                # print(self.mat_rand[f][c], x, y, xs, c%3, "c = ", c)
            if xs == 2:
                xs = 0
            else:
                xs += 1
    def get_casillas_group(self):
        casillas_group = pygame.sprite.Group()

        for f in range(self.filas):
            for c in range(self.columnas):
                group = self.matriz[f][c].get_casillas_group().sprites()
                for sprite in group:
                    casillas_group.add(sprite)

        return casillas_group