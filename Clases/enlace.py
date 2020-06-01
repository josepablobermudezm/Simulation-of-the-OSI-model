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
    def validacionTrama(self, bits):
        num = len(bits) + 16
        print("CAPA DE ENLACE DE DATOS")
        bits+="0000000000000000"
        valor = int(bits, 2)
        residuo = valor%65521
        aux = 65521 - residuo
        suma = valor + aux
        binario = ''
        
        while suma // 2 != 0:
            binario = str(suma % 2) + binario
            suma = suma // 2
        if len(str(suma) + binario)!=num:
            aux = num-len(str(suma) + binario)
            cont=0
            b =""
            while(cont<aux):
                b+="0"
                cont+=1
            b+= (str(suma) + binario)
            return b    
        return str(suma) + binario
        
