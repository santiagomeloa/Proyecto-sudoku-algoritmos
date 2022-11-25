from functions import *
from sprites import *
import pytest

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def test_load_images():
    with pytest.raises(FileNotFoundError):
        load_image('one.png')

    with pytest.raises(TypeError):
        load_image("Imagenes/Fondo.png", WIDTH)
        load_image(3, WIDTH)
        load_image(True, WIDTH)


def test_clases_numeros():
    with pytest.raises(ValueError):
        one = Numbers(pygame.image.load('Imagenes/one.png').convert_alpha(), -200, -(HEIGHT/1.25), 1)
        nine = Numbers(pygame.image.load('Imagenes/nine.png').convert_alpha(), 1080, -(HEIGHT/1.25), 9)
        six = Numbers(pygame.image.load('Imagenes/six.png').convert_alpha(), -750, (HEIGHT/1.25), 6)
        four = Numbers(pygame.image.load('Imagenes/four.png').convert_alpha(), 530, (HEIGHT/1.25), -4)
        two = Numbers(pygame.image.load('Imagenes/two.png').convert_alpha(), 310, (HEIGHT/1.25), 10)

def test_logica_sudoku():
    pass
