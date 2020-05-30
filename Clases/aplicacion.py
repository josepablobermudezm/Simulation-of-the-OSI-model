import msvcrt
import os
import keyboard  # using module keyboard
from .presentacion import presentacion

class aplicacion:

    
    def __init__(self, c):
        self.c = c

    def metodo(self, variable):
        print("Hola " + str(variable))

    def teclapresionada(self):
        palabra=""
        c ="A"
        while ord(c)!=13:
            c = msvcrt.getch()
            os.system ("cls")
            valor = ord(c.upper())
            if (valor>=32 and not keyboard.is_pressed('down arrow') 
            and not keyboard.is_pressed('up arrow') and not keyboard.is_pressed('left arrow') 
            and not keyboard.is_pressed('right arrow')):
                if (valor<47 or valor>59) and valor!=32: #and valor-31!=11:
                    letra = chr(valor)
                    #llama al metodo de la capa de presentacion
                    palabra+=presentacion.switch_demo(None,letra)
                elif valor==32:
                    letra = '...'
                    palabra+=letra    
            elif valor == 8:
                temp = len(palabra)
                cadena = palabra[:temp-3]
                palabra = cadena    
            print (palabra)
        os.system ("cls") 
        #llama a la capa de presentacion
        host="25.101.202.236"
        puerto=44440
        presentacion.iniciarCliente(None,host,puerto,palabra)  