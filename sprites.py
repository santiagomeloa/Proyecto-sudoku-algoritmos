import pygame

#Inicializar pygame
pygame.init()

#Parametros
size = width, height = 800, 600
color = 255, 255, 255

#crear pantalla con ancho y alto
screen = pygame.display.set_mode(size)

#Poner titulo a la ventana e icono
pygame.display.set_caption("Sudoku")
icon = pygame.image.load('sudoku.png')
pygame.display.set_icon(icon)

#Imagenes PNG
one = pygame.image.load('bt1.png')
one_X = 400
one_Y = 300
two = pygame.image.load('bt2.png')
two_X = 0
two_Y = 0
three = pygame.image.load('bt3.png')
three_X = 0
three_Y = 0
four = pygame.image.load('bt4.png')
four_X = 0
four_Y = 0
five = pygame.image.load('bt5.png')
five_X = 0
five_Y = 0
six = pygame.image.load('bt6.png')
six_X = 0
six_Y = 0
seven = pygame.image.load('bt7.png')
seven_X = 0
seven_Y = 0
eight = pygame.image.load('bt8.png')
eight_X = 0
eight_Y = 0
nine = pygame.image.load('bt9.png')
nine_X = 0
nine_Y = 0

#Clase teclado
def keyboard():
    screen.blit(one, (one_X, one_Y))

#Bucle de juego
play = True
while play:
    screen.fill(color)  #Poner color a la ventana

    for event in pygame.event.get():  #Detector eventos de la ventana
        if event.type == pygame.QUIT: #Cerrar ventana
            play = False
    
    keyboard()
    pygame.display.update()  #Actualizar la información de la ventana