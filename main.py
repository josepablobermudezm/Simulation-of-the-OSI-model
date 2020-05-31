from Clases import aplicacion
import os
import msvcrt
if __name__ == '__main__':
    #llama a la capa de aplicacion
    while True:
        aplicacion.teclapresionada(None)
        msvcrt.getch()
        os.system ("cls")
