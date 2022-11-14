import sys

import pygame
from pygame.locals import *

import functions
from functions import HEIGHT, WHITE, WIDTH
from sprites import Casilla, Cuadricula, Numbers, Subcuadricula

FPS = 60



def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Sudoku')
    background_image = functions.load_image("Imagenes/Fondo.png", WIDTH/2, HEIGHT/2, True)

    #-------------OBJETOS------------

    numbers_group = pygame.sprite.Group()
    
    cuadricula = Cuadricula(3, 3, (WIDTH/2, HEIGHT/2))

    #Objetos Numero
    one = Numbers(pygame.image.load('Imagenes/bt1.png').convert_alpha(), 0, 0, "1")
    two = Numbers(pygame.image.load('Imagenes/bt2.png').convert_alpha(), 150, 0, "2")
    three = Numbers(pygame.image.load('Imagenes/bt3.png').convert_alpha(), 300, 0, "3")
    four = Numbers(pygame.image.load('Imagenes/bt4.png').convert_alpha(), 0, 150, "4")
    five = Numbers(pygame.image.load('Imagenes/bt5.png').convert_alpha(), 150, 150, "5")
    six = Numbers(pygame.image.load('Imagenes/bt6.png').convert_alpha(), 300, 150, "6")
    seven = Numbers(pygame.image.load('Imagenes/bt7.png').convert_alpha(), 0, 300, "7")
    eight = Numbers(pygame.image.load('Imagenes/bt8.png').convert_alpha(), 150, 300, "8")
    nine = Numbers(pygame.image.load('Imagenes/bt9.png').convert_alpha(), 300, 300, "9")

    numbers_group.add(one)
    numbers_group.add(two)
    numbers_group.add(three)
    numbers_group.add(four)
    numbers_group.add(five)
    numbers_group.add(six)
    numbers_group.add(seven)
    numbers_group.add(eight)
    numbers_group.add(nine)

    # c = Casilla(0, (WIDTH/2, None, None, None, None, None))
    # sub = Subcuadricula(3,3,(None, None, None, None, WIDTH/2, HEIGHT/2))


    #---------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------
    while True:
        clock.tick(FPS)
        screen.fill(WHITE)

        screen.blit(background_image, (0, 0))

        cuadricula.draw(screen)
        numbers_group.draw(screen)
        # sub.draw(screen)
        # c.draw(screen)
        #-------------detecting keyboards inputs-------------
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit(0)
            
        


        pygame.display.flip() #Actualizar contenido en pantalla

if __name__ == '__main__':
    pygame.init()
    main()