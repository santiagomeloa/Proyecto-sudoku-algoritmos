import sys

import pygame
from pygame.locals import *

import functions
from functions import HEIGHT, WHITE, WIDTH
from sprites import Cuadricula, Numbers

FPS = 60



def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Sudoku')
    background_image = functions.load_image("Imagenes/Fondo.png", WIDTH, HEIGHT)

    #-------------OBJETOS------------

    numbers_group = pygame.sprite.Group()
    
    cuadricula = Cuadricula(3, 3, (WIDTH/2, HEIGHT/2))
    cuadricula.generador()

    #Objetos Numero
    one = Numbers(pygame.image.load('Imagenes/one.png').convert_alpha(), 500, (HEIGHT/1.134), "1")
    two = Numbers(pygame.image.load('Imagenes/two.png').convert_alpha(), 600, (HEIGHT/1.134), "2")
    three = Numbers(pygame.image.load('Imagenes/three.png').convert_alpha(), 700, (HEIGHT/1.134), "3")
    four = Numbers(pygame.image.load('Imagenes/four.png').convert_alpha(), 800, (HEIGHT/1.134), "4")
    five = Numbers(pygame.image.load('Imagenes/five.png').convert_alpha(), 900, (HEIGHT/1.134), "5")
    six = Numbers(pygame.image.load('Imagenes/six.png').convert_alpha(), 1000, (HEIGHT/1.134), "6")
    seven = Numbers(pygame.image.load('Imagenes/seven.png').convert_alpha(), 1100, (HEIGHT/1.134), "7")
    eight = Numbers(pygame.image.load('Imagenes/eight.png').convert_alpha(), 1200, (HEIGHT/1.134), "8")
    nine = Numbers(pygame.image.load('Imagenes/nine.png').convert_alpha(), 1300, (HEIGHT/1.134), "9")

    numbers_group.add(one)
    numbers_group.add(two)
    numbers_group.add(three)
    numbers_group.add(four)
    numbers_group.add(five)
    numbers_group.add(six)
    numbers_group.add(seven)
    numbers_group.add(eight)
    numbers_group.add(nine)


    #---------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------
    while True:
        clock.tick(FPS)
        screen.fill(WHITE)

        screen.blit(background_image, (0, 0))

        cuadricula.draw(screen)
        numbers_group.draw(screen)


        #-------------detecting keyboards inputs-------------
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:

                num_list = {one, two, three, four, five, six, seven, eight, nine}
                for num in num_list:
                    val = num.checkForInput(pygame.mouse.get_pos())
                    if(val != 0):
                        break

        pygame.display.flip() #Actualizar contenido en pantalla

if __name__ == '__main__':
    pygame.init()
    main()
