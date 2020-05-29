from Clases import aplicacion
import msvcrt
import os
import keyboard  # using module keyboard

def teclapresionada():
    palabra=""
    c ="A"
    while ord(c)!=13:
        c = msvcrt.getch()
        os.system ("cls")
        valor = ord(c.upper())
        if valor>=32 and not keyboard.is_pressed('down arrow') and not keyboard.is_pressed('up arrow') and not keyboard.is_pressed('left arrow') and not keyboard.is_pressed('right arrow'):
            if (valor<47 or valor>59) and valor!=32 and valor-31!=11:
                valor-=31
                letra = chr(valor)
                palabra+=letra
            elif valor==32:
                letra = chr(126)
                palabra+=letra    
        elif valor == 8:
            temp = len(palabra)
            cadena = palabra[:temp-1]
            palabra = cadena    
        print (palabra)

    os.system ("cls") 
    return palabra


if __name__ == '__main__':
    #aplicacion.metodo(None, "jordi")
    print(teclapresionada())
