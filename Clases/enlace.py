class enlace:

    def __init__(self):
        pass

    def tobits(self, mensaje):
        print("CAPA DE ENLACE DE DATOS")
        result = ""
        for c in mensaje:
            bits = bin(ord(c))[2:]
            print("Letra: "+c)
            print("Binario: " + bits)
            bits = '00000000'[len(bits):] + bits
            result+=bits
            #result.extend([int(b) for b in bits])
        return result