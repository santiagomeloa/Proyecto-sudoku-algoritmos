from functions import *
from sprites import *
import pytest

def test_load_images():
    with pytest.raises(FileNotFoundError):
        load_image('one.png')

    with pytest.raises(TypeError):
        load_image("Imagenes/Fondo.png", WIDTH)

def test_coords_clases_numeros():
    pass

def test_logica_sudoku():
    pass
