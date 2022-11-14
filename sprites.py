import pygame

#Inicializar pygame
pygame.init()

#Parametros
size = width, height = 450, 450
color = 255, 255, 255

#crear pantalla con ancho y alto
screen = pygame.display.set_mode(size)

#Poner titulo a la ventana e icono
pygame.display.set_caption("Sudoku")
icon = pygame.image.load('sudoku.png')
pygame.display.set_icon(icon)

#Clase numeros
class numbers():
    def __init__(self, image, x, y, number):
        self.image = pygame.transform.scale(image, (150, 150))
        self.pos_x = x
        self.pos_y = y
        self.number = number
        self.rect = self.image.get_rect()
        self.rect.topleft = ((self.pos_x, self.pos_y))

    def draw(self):
        screen.blit(self.image, self.rect)
    
    def checkForInput(self, position):
	    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
		    print(self.number)

#Objetos Numero
one = numbers(pygame.image.load('Numbers/one.png').convert_alpha(), 0, 0, "1")
two = numbers(pygame.image.load('Numbers/two.png').convert_alpha(), 150, 0, "2")
three = numbers(pygame.image.load('Numbers/three.png').convert_alpha(), 300, 0, "3")
four = numbers(pygame.image.load('Numbers/four.png').convert_alpha(), 0, 150, "4")
five = numbers(pygame.image.load('Numbers/five.png').convert_alpha(), 150, 150, "5")
six = numbers(pygame.image.load('Numbers/six.png').convert_alpha(), 300, 150, "6")
seven = numbers(pygame.image.load('Numbers/seven.png').convert_alpha(), 0, 300, "7")
eight = numbers(pygame.image.load('Numbers/eight.png').convert_alpha(), 150, 300, "8")
nine = numbers(pygame.image.load('Numbers/nine.png').convert_alpha(), 300, 300, "9")

#Bucle de juego
play = True
while play:
    screen.fill("white")  #Poner color a la ventana

    one.draw()
    two.draw()
    three.draw()
    four.draw()
    five.draw()
    six.draw()
    seven.draw()
    eight.draw()
    nine.draw()

    for event in pygame.event.get():  #Detector eventos de la ventana
        if event.type == pygame.QUIT: #Cerrar ventana
            play = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            one.checkForInput(pygame.mouse.get_pos())
            two.checkForInput(pygame.mouse.get_pos())
            three.checkForInput(pygame.mouse.get_pos())
            four.checkForInput(pygame.mouse.get_pos())
            five.checkForInput(pygame.mouse.get_pos())
            six.checkForInput(pygame.mouse.get_pos())
            seven.checkForInput(pygame.mouse.get_pos())
            eight.checkForInput(pygame.mouse.get_pos())
            nine.checkForInput(pygame.mouse.get_pos())

    
    pygame.display.update()  #Actualizar la información de la ventana