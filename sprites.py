import pygame

#Inicializar pygame
pygame.init()

#Parametros
<<<<<<< Updated upstream
size = width, height = 800, 600
=======
size = width, height = 465, 480
>>>>>>> Stashed changes
color = 255, 255, 255

#crear pantalla con ancho y alto
screen = pygame.display.set_mode(size)

#Poner titulo a la ventana e icono
pygame.display.set_caption("Sudoku")
icon = pygame.image.load('sudoku.png')
pygame.display.set_icon(icon)

#Imagenes PNG
<<<<<<< Updated upstream
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
=======
one = pygame.image.load('one.png')
one_X = -390
one_Y = -125

two = pygame.image.load('two.png')
two_X = -250
two_Y = -156

three = pygame.image.load('three.png')
three_X = -95
three_Y = -140

four = pygame.image.load('four.png')
four_X = -405
four_Y = -5

five = pygame.image.load('five.png')
five_X = -280
five_Y = -10

six = pygame.image.load('six.png')
six_X = -100
six_Y = 17

seven = pygame.image.load('seven.png')
seven_X = -405
seven_Y = 135

eight = pygame.image.load('eight.png')
eight_X = -273
eight_Y = 142

nine = pygame.image.load('nine.png')
nine_X = -110
nine_Y = 145

>>>>>>> Stashed changes

#Clase teclado
def keyboard():
    screen.blit(one, (one_X, one_Y))
<<<<<<< Updated upstream

=======
    screen.blit(two, (two_X, two_Y))
    screen.blit(three, (three_X, three_Y))
    screen.blit(four, (four_X, four_Y))
    screen.blit(five, (five_X, five_Y))
    screen.blit(six, (six_X, six_Y))
    screen.blit(seven, (seven_X, seven_Y))
    screen.blit(eight, (eight_X, eight_Y))
    screen.blit(nine, (nine_X, nine_Y))
>>>>>>> Stashed changes
#Bucle de juego
play = True
while play:
    screen.fill(color)  #Poner color a la ventana

    for event in pygame.event.get():  #Detector eventos de la ventana
        if event.type == pygame.QUIT: #Cerrar ventana
            play = False
    
    keyboard()
    pygame.display.update()  #Actualizar la información de la ventana