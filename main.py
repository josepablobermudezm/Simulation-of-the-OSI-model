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
        if (valor>=32 and not keyboard.is_pressed('down arrow') 
        and not keyboard.is_pressed('up arrow') and not keyboard.is_pressed('left arrow') 
        and not keyboard.is_pressed('right arrow')):
            if (valor<47 or valor>59) and valor!=32: #and valor-31!=11:
                letra = chr(valor)
                print(letra)
                palabra+=switch_demo(letra)
            elif valor==32:
                letra = '...'
                palabra+=letra    
        elif valor == 8:
            temp = len(palabra)
            cadena = palabra[:temp-3]
            palabra = cadena    
        print (palabra)

    os.system ("cls") 
    return palabra

def switch_demo(letra):
    switcher = {
        'A': "!_#",
        'B': '@_(',
        'C': '#_$',
        'D': '$_*',
        'E': '%_%',
        'F': '^_-',
        'G': '=_!',
        'H': '~_&',
        'I': '~_~',
        'J': '-_-',
        'K': '!_!',
        'L': '$_^',
        'M': '?_@',
        'N': '/_/',
        'Ñ': '___',
        'O': '{_{',
        'P': '}_}',
        'Q': ':_:',
        'R': '¿_?',
        'S': ';_;',
        'T': '&_!',
        'U': '#_#',
        'V': '*_*',
        'W': '|_|',
        'X': '°_°',
        'Y': 'ü_ü',
        'Z': '._.',
    }
    return switcher.get(letra, "Invalid caracter")

def desencriptar(palabra):
    palabraAux = palabra

    switcher = {
        "!_#":'A',
        '@_(':'B',
        '#_$':'C',
        '$_*':'D',
        '%_%':'E',
        '^_-':'F',
        '=_!':'G', 
        '~_&':'H',
        '~_~':'I',
        '-_-':'J',
        '!_!':'K',
        '$_^':'L',
        '?_@':'M',
        '/_/':'N',
        '___':'Ñ',
        '{_{':'O',
        '}_}':'P',
        ':_:':'Q',
        '¿_?':'R',
        ';_;':'S',
        '&_!':'T',
        '#_#':'U',
        '*_*':'V',
        '|_|':'W',
        '°_°':'X',
        'ü_ü':'Y',
        '._.':'Z',
        '...':' '
    }

    indice = 0
    cont = 0
    l=""
    while indice < len(palabra):
        if cont==3:
            palabraAux+= switcher.get(l, "Invalid caracter")
            l=""
            cont=0
        else:
            l+= palabra[indice]
            cont+=1
            indice += 1
            if indice+1 == len(palabra):
                l+= palabra[indice]
                palabraAux+= switcher.get(l, "Invalid caracter")

    return palabraAux


if __name__ == '__main__':
    #aplicacion.metodo(None, "jordi")
    print(desencriptar(teclapresionada()))
