import socket, os
from .enlace import enlace
import time
class transporte:

    def __init__(self, nombre):
        self.nombre = nombre

    def enviarMensaje(self,c, mensaje):
        print("------------------")
        print("CAPA DE TRANSPORTE")
        print("MENSAJE DIGITADO: "+ mensaje)
        cont = 0

        if(len(mensaje)%12 == 0):
            cantTramas = int((len(mensaje)/12))
        else:
            cantTramas = int((len(mensaje)/12))+1
        #envia la cantidad de tramas 
        print("CANTIDAD DE TRAMAAAAAAAAAS "+ str(cantTramas))
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
                if cont == 12:
                    print("TRAMA "+ enlace.tobits(None,trama))
                    cont = 1
                    print("LLAMANDO A LA CAPA DE ENLACE DE DATOS")
                    time.sleep(1)
                    c.send(enlace.tobits(None,trama).encode('utf8', errors='replace'))
                    trama=""
                    trama += mensaje[indice]
                else:
                    if indice+1 == len(mensaje) and cont<12:
                        trama += mensaje[indice]   
                        print("TRAMA FINAL "+ enlace.tobits(None,trama))
                        print("LLAMANDO A LA CAPA DE ENLACE DE DATOS")
                        c.send(enlace.tobits(None,trama).encode('utf8', errors='replace'))  
                    else:
                        trama += mensaje[indice]   
                        cont+=1   
                indice +=1    
        print("------------------")
        print("FIN DE CAPA DE TRANSPORTE")