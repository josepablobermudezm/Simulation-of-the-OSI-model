class enlace:

    def __init__(self):
        pass

    def tobits(self, mensaje):
        print("CAPA DE ENLACE DE DATOS")
        result = ""
        for c in mensaje:
            bits = bin(ord(c))[2:]
            bits = '00000000'[len(bits):] + bits
            result+=bits
            #result.extend([int(b) for b in bits])
        print("FIN DE CAPA DE ENLACE DE DATOS")
        return result
    def validacionTrama(self, bits,falloTrama):
        print("CAPA DE ENLACE DE DATOS")
        bits+="0000000000000000"
        valor = int(bits, 2)
        residuo = valor%65521
        aux = 65521 - residuo
        suma = valor + aux
        if suma%65521 == 0: 
            print("CORRECTO")
        else:
            print("INCORRECTO")

        if falloTrama==1:
            return "fallo"
        else:
            return "correcto"

