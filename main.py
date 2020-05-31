from Clases import aplicacion
import os
import msvcrt
if __name__ == '__main__':
    #llama a la capa de aplicacion
    while True:
        os.system ("cls")
        print("Digita la IP del servidor:")
        IP = input()
        os.system ("cls")
        print("Empieza a escribir...")
        aplicacion.teclapresionada(None, IP)
        msvcrt.getch()
        os.system ("cls")
        print("Oprime una tecla para continuar...")