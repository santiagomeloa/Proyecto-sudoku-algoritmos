import pygame, random
from pygame.locals import *
import functions
from functions import HEIGHT, WHITE, WIDTH


#Clase numeros botones
class Numbers(pygame.sprite.Sprite):
    def __init__(self, image, x, y, number):
        super().__init__()

        self.image = pygame.transform.scale(image, (100, 100))
        self.pos_x = x
        self.pos_y = y
        self.number = number
        self.rect = self.image.get_rect()
        self.rect.topleft = ((self.pos_x, self.pos_y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return self.number
        else:
            return 0

#Clase numeros casillas
class Numbers_casillas(pygame.sprite.Sprite):
    def __init__(self, image, x, y, number):
        super().__init__()

        self.image = pygame.transform.scale(image, (80, 80))
        self.pos_x = x
        self.pos_y = y
        self.number = number
        self.rect = self.image.get_rect()
        self.rect.topleft = ((self.pos_x, self.pos_y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)


#class casilla---------------------------------------------------------
class Casilla(pygame.sprite.Sprite):
    def __init__(self, dat:int= 0, pos:tuple= (0, 0, 0, 0, 0, 0)):
        super().__init__()

        self.tam = WIDTH/20.2
        self._dato = dat
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
        

    def get_dato(self):
        return self._dato

    def set_dato(self, dato:int):
        self._dato = dato
 
    def printc(self):
        print(self._dato, end= " ") #imprime el número y sigue en la misma linea

    def draw(self, surface): #Método para mostrar el sprint en pantalla
                             # surface = pantalla
        surface.blit(self.image, self.rect)

    def put_number(self, position, number):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            if(number == 1):
                one = Numbers_casillas(pygame.image.load('Imagenes/1.png').convert_alpha(), self.pos_x, self.pos_y, "1")
                one.draw(screen)
            if(number == 2):
                two = Numbers_casillas(pygame.image.load('Imagenes/2.png').convert_alpha(), self.pos_x, self.pos_y, "2")
                two.draw(screen)
            if(number == 3):
                three = Numbers_casillas(pygame.image.load('Imagenes/3.png').convert_alpha(), self.pos_x, self.pos_y, "3")
                three.draw(screen)
            if(number == 4):
                four = Numbers_casillas(pygame.image.load('Imagenes/4.png').convert_alpha(), self.pos_x, self.pos_y, "4")
                four.draw(screen)
            if(number == 5):
                five = Numbers_casillas(pygame.image.load('Imagenes/5.png').convert_alpha(), self.pos_x, self.pos_y, "5")
                five.draw(screen)
            if(number == 6):
                six = Numbers_casillas(pygame.image.load('Imagenes/6.png').convert_alpha(), self.pos_x, self.pos_y, "6")
                six.draw(screen)
            if(number == 7):
                seven = Numbers_casillas(pygame.image.load('Imagenes/7.png').convert_alpha(), self.pos_x, self.pos_y, "7")
                seven.draw(screen)
            if(number == 8):
                eight = Numbers_casillas(pygame.image.load('Imagenes/8.png').convert_alpha(), self.pos_x, self.pos_y, "8")
                eight.draw(screen)
            if(number == 9):
                nine = Numbers_casillas(pygame.image.load('Imagenes/9.png').convert_alpha(), self.pos_x, self.pos_y, "9")
                nine.draw(screen)

#class subcuadricula--------------------------------------------------
class Subcuadricula(pygame.sprite.Sprite):
    def __init__(self, fila=3, columna=3, pos:tuple = (0, 0, 0, 0, 0, 0)):
        super().__init__()
        # 220Numbers
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
        self.matriz[x][y].set_dato(num)
      

    def insert(self, fila, columna, num):
        c = self.matriz[fila][columna]
        c.setCasilla(num)
       
    def revisar_sub(self, num):
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz[i][j].getCasilla()==num:
                    return False
        return True
    
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

        self.tam = WIDTH/2.4
        self.picture = 'Imagenes/Cuadricula.png' # localización de la imagen a ser usada para la clase
        self.image = functions.load_image(self.picture, self.tam, self.tam, True) # convertir la imagen en un formato aceptado por pygame para ser tratado
        self.rect = self.image.get_rect()

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
        self.matriz[x][y].set_dato(num, xs, ys)

    def fill_sudoku(self):
        random_pos = (random.choice([x for x in range(self.filas)]), random.choice([y for y in range(self.columnas)]))

        self.set_dato(random.choice([d for d in range(1, 10)]), random_pos[0], random_pos[1], random_pos[1], random_pos[1])
        print(self.get_dato(random_pos[0], random_pos[1], random_pos[0], random_pos[1])) 

    def draw(self, surface): #Método para mostrar el sprint en pantalla
                             # surface = pantalla

        surface.blit(self.image, self.rect)
        for i in range(self.filas):
            for j in range(self.columnas):
                (self.matriz[i][j]).draw(surface)
                
    def revisar_fila (self, pos_cua, pos_sub, num):
        for i in range(3):
            sub_cuadricula=self.matriz[pos_cua][i]
            for j in range(3):
                
                if sub_cuadricula.get_dato(pos_sub, j) == num:
                    return False
        return True
    
    def revisar_columna(self, pos_cua, pos_sub, num):
        for i in range(3):
            sub_cuadricula=self.matriz[i][pos_cua]
            for j in range(3):
            
                if sub_cuadricula.get_dato(j, pos_sub) == num:
                    return False
        return True
                
    def revisar_sub_cua(self, posx, posy, num):
        return self.matriz[posx][posy].revisar_sub(num)

    def fill_fila(self, pos_cuax, pos_subx):
        lista = [1,2,3,4,5,6,7,8,9]
        for i in range(self.columnas):
            sub_cuadricula=self.matriz[pos_cuax][i]
            for j in range(self.columnas):
                num = lista.pop(0)
                while not revisar_columna(i, j, num) and not revisar_sub_cua(pos_cuax, i):
                    lista.append(num)
                    num = lista.pop(0)
                    
                sub_cuadricula.set_dato(num, pos_subx, j)
                
    
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
