from Clases import aplicacion
import os
import msvcrt
if __name__ == '__main__':
    #llama a la capa de aplicacion
    while True:
        print("Digita la IP del servidor")
        IP = input()
        aplicacion.teclapresionada(None, IP)
        msvcrt.getch()
        os.system ("cls")