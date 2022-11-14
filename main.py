import pygame, sys
from pygame.locals import *
import functions, sprites

from functions import WIDTH, HEIGHT

FPS = 60
WHITE = (255, 255, 255)


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Sudoku')
    background_image = functions.load_image("Imagenes/Fondo.png", WIDTH/2, HEIGHT/2, True)
    
    cuadricula = sprites.Cuadricula(3, 3, (WIDTH/2, HEIGHT/2))

    # c = sprites.Casilla(0, (WIDTH/2, None, None, None, None, None))
    # sub = sprites.Subcuadricula(3,3,(None, None, None, None, WIDTH/2, HEIGHT/2))


    #---------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------
    while True:
        clock.tick(FPS)
        screen.fill(WHITE)

        screen.blit(background_image, (0, 0))

        cuadricula.draw(screen)
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