import socket, os
from .enlace import enlace
class transporte:

    def __init__(self, nombre):
        self.nombre = nombre

    def enviarMensaje(self,c, mensaje):
        print("------------------")
        print("CAPA DE TRANSPORTE")
        print("MENSAJE DIGITADO: "+ mensaje)
        cont = 0

        if(len(mensaje)%12 == 0):
            cantTramas = (len(mensaje)/12)
        else:
            cantTramas = int((len(mensaje)/12))+1
        #envia la cantidad de tramas 
        c.send(str(cantTramas).encode('utf8', errors='replace'))    
        if len(mensaje) <= 12:
            print("LLAMANDO A LA CAPA DE ENLACE DE DATOS")
            print("ENVIANDO UNICA TRAMA")
            c.send(enlace.tobits(None,mensaje).encode('utf8', errors='replace'))
        else:
            print("LLAMANDO A LA CAPA DE ENLACE DE DATOS")
            indice = 0
            trama=""

            while indice<len(mensaje):
                trama += mensaje[indice]
                if cont == 12:
                    cont = 0
                    print("LLAMANDO A LA CAPA DE ENLACE DE DATOS")
                    c.send(enlace.tobits(None,trama).encode('utf8', errors='replace'))
                    trama=""
                else:
                    if indice+1 == len(mensaje) and cont<12:
                        print("LLAMANDO A LA CAPA DE ENLACE DE DATOS")
                        c.send(enlace.tobits(None,trama).encode('utf8', errors='replace'))    
                    cont+=1
                indice +=1    
        print("------------------")
        print("FIN DE CAPA DE TRANSPORTE")