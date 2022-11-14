import subprocess, pygame, platform, ctypes
from pygame.locals import *

WHITE = (255, 255, 255)

sistema = platform.system() #Obtiene el sistema operativo del pc desde donde se esté ejecutando

def screen_size(): # Obtine la resolución de la pantalla dependiendo del sistema operativo
    if sistema == 'Linux':
        size = (None, None)
        args = ["xrandr", "-q", "-d", ":0"]
        proc = subprocess.Popen(args,stdout=subprocess.PIPE)
        for line in proc.stdout:
            if isinstance(line, bytes):
                line = line.decode("utf-8")
                if "Screen" in line:
                    size = (int(line.split()[7]),  int(line.split()[9][:-1]))
        return size
    else:
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        WIDTH, HEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        return WIDTH, HEIGHT


#-------Tamaño de la pantalla------
WIDTH = screen_size()[0]
HEIGHT = screen_size()[1]


def load_image(filename, width=None, height=None, transparent=False):   #covierte las imagenes a el formato aceptado por pygame y le da las dimenciones deceadas,
                                                                        #ademas de poder quitar el fondo
    try: imagen = pygame.image.load(filename)
    except pygame.error:
        raise SystemExit

    if width != None or height != None:     #Si width o height son diferentes de "None", redefine el tamaño de la imagen con los parametros dados
        imagen = pygame.transform.scale(imagen, (width, height))
    imagen = imagen.convert()

    if transparent:     #Si transparent es igaul a True, entonces se le quita el fondo a la imagen
        color = pygame.PixelArray(imagen)
        imagen.set_colorkey(color[0, 0], RLEACCEL)

    return imagen