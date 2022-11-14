import pygame, sys
from pygame.locals import *

class Botones:
    # Constructor
    def __init__(self, vl = 0):
        self.valor = vl
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480
        self.color = (255,255,255)
    
    # Getters
    def getVal(self):
        return self.valor
    
    # Setters
    def setVal(self, vl):
        self.valor = vl
    
    # Metodo para observar los botones segun el numero que tengan
    def visualizar(self):
        pygame.init()
    
        # creamos la ventana y le indicamos un titulo:
        screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("BOTONES")
        
        # Asigna la imagen segun el numero que tenga establecido
        if self.valor == 1:
            v = pygame.image.load("Imagenes/bt1.png").convert_alpha() # Se carga la imagen del boton
            v_c = pygame.transform.scale(v, (200, 100)) # Se modifica el tamaño de la imagen
        if self.valor == 2:
            v = pygame.image.load("Imagenes/bt2.png").convert_alpha()
            v_c = pygame.transform.scale(v, (200, 100))
        if self.valor == 3:
            v = pygame.image.load("Imagenes/bt3.png").convert_alpha()
            v_c = pygame.transform.scale(v, (200, 100))
        if self.valor == 4:
            v = pygame.image.load("Imagenes/bt4.png").convert_alpha()
            v_c = pygame.transform.scale(v, (200, 100))
        if self.valor == 5:
            v = pygame.image.load("Imagenes/bt5.png").convert_alpha()
            v_c = pygame.transform.scale(v, (200, 100))
        if self.valor == 6:
            v = pygame.image.load("Imagenes/bt6.png").convert_alpha()
            v_c = pygame.transform.scale(v, (200, 100))
        if self.valor == 7:
            v = pygame.image.load("Imagenes/bt7.png").convert_alpha()
            v_c = pygame.transform.scale(v, (200, 100))   
        if self.valor == 8:
            v = pygame.image.load("Imagenes/bt8.png").convert_alpha()
            v_c = pygame.transform.scale(v, (200, 100))
        if self.valor == 9:
            v = pygame.image.load("Imagenes/bt9.png").convert_alpha()
            v_c = pygame.transform.scale(v, (200, 100))
        else:
            pass            
        # Se le asigna un color de fondo y se le indica la posicion de las imagenes sobre la ventana
        screen.fill(self.color)
        screen.blit(v_c, (0, 0))
        
        # se muestran lo cambios en pantalla
        pygame.display.flip()
    
        # el bucle principal del juego
        while True:
            # Posibles entradas del teclado y mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    

b1 = Botones(1)
b1.visualizar()
