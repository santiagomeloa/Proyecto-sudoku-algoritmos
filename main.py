import pygame, sys
from pygame.locals import *
import functions

from functions import WIDTH, HEIGHT

FPS = 60


def main():
    screen = pygame.display.set_mode((500, 600))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Sudoku')
    

    #---------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------------------------
    while True:
        clock.tick(FPS)

        #-------------detecting keyboards inputs-------------
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            
        

        pygame.display.flip() #Actualizar contenido en pantalla

if __name__ == '__main__':
    pygame.init()
    main()