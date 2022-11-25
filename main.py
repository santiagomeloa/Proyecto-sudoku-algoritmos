import sys

import pygame, random
from pygame.locals import *

import functions
from functions import HEIGHT, WHITE, WIDTH
from sprites import Cuadricula, Numbers, Numbers_casillas

FPS = 60



def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Sudoku')
    background_image = functions.load_image("Imagenes/Fondo.png", WIDTH, HEIGHT)
    load_screen = True

    global set_number 

    set_number = 0

    #-------------OBJETOS------------

    numbers_group = pygame.sprite.Group()
    
    cuadricula = Cuadricula(3, 3, (WIDTH/2, HEIGHT/2))
    cuadricula.generador()

    casillas_group = cuadricula.get_casillas_group()


    # numberrr= Numbers_casillas(WIDTH/2, HEIGHT/2, 5)

    #Objetos Numero
    one = Numbers(pygame.image.load('Imagenes/one.png').convert_alpha(), 200, (HEIGHT/1.25), 1)
    two = Numbers(pygame.image.load('Imagenes/two.png').convert_alpha(), 310, (HEIGHT/1.25), 2)
    three = Numbers(pygame.image.load('Imagenes/three.png').convert_alpha(), 420, (HEIGHT/1.25), 3)
    four = Numbers(pygame.image.load('Imagenes/four.png').convert_alpha(), 530, (HEIGHT/1.25), 4)
    five = Numbers(pygame.image.load('Imagenes/five.png').convert_alpha(), 640, (HEIGHT/1.25), 5)
    six = Numbers(pygame.image.load('Imagenes/six.png').convert_alpha(), 750, (HEIGHT/1.25), 6)
    seven = Numbers(pygame.image.load('Imagenes/seven.png').convert_alpha(), 860, (HEIGHT/1.25), 7)
    eight = Numbers(pygame.image.load('Imagenes/eight.png').convert_alpha(), 970, (HEIGHT/1.25), 8)
    nine = Numbers(pygame.image.load('Imagenes/nine.png').convert_alpha(), 1080, (HEIGHT/1.25), 9)

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
        # numberrr.draw(screen)

        # if load_screen:
        #     load_stage(FPS, clock)
        #     load_screen = False


        #-------------detecting keyboards inputs-------------
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit(0)


            if event.type == MOUSEBUTTONDOWN and event.button == 1:

                for num in numbers_group.sprites():
                    if num.rect.collidepoint(pygame.mouse.get_pos()):
                        set_number = num.get_number()
                        break

                for casilla in casillas_group.sprites():
                    if casilla.rect.collidepoint(pygame.mouse.get_pos()):
                        if set_number != 0:
                            casilla.set_dato(set_number)


        # cuadricula.set_dato(random.randint(1,9), 0, 0, 0, 0)

        cuadricula.update()

        pygame.display.flip() #Actualizar contenido en pantalla

if __name__ == '__main__':
    pygame.init()
    main()
