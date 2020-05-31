import socket, os
from .enlace import enlace
import time
import random
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
        c.send(str(cantTramas).encode('utf8', errors='replace')) 
        
        #Se define para verificar si el mensaje va a ser interrumpido por un error en el mensaje
        falloTrama = random.randint(0, 1)        
        

        if len(mensaje) <= 12:
            print("LLAMANDO A LA CAPA DE ENLACE DE DATOS")
            print("ENVIANDO UNICA TRAMA")
            #validacion trama en enlace de datos
            bits = enlace.tobits(None,mensaje)
            bits = enlace.validacionTrama(None,bits)
            print("TRAMA ESPERADA: "+ bits)
            if falloTrama==1:
                print("......FALLO EN TRAMA.....")    
                if bits[0] =="1": 
                    aux = bits.replace('1', '0', 1)
                    bits = aux
                else:
                    aux = bits.replace('0', '1', 1)
                    bits = aux
            print("TRAMA ENVIADA "+ bits)
            c.send(bits.encode('utf8', errors='replace'))
        else:
            print("LLAMANDO A LA CAPA DE ENLACE DE DATOS")
            indice = 0
            trama=""

            while indice<len(mensaje):
                if cont == 12:
                    print("TRAMA ESPERADA: "+ enlace.tobits(None,trama))
                    cont = 1
                    print("LLAMANDO A LA CAPA DE ENLACE DE DATOS")
                    time.sleep(1)
                    bits = enlace.tobits(None,trama)
                    bits = enlace.validacionTrama(None,bits)
                    if falloTrama==1:   
                        print("......FALLO EN TRAMA.....") 
                        if bits[0] =="1": 
                            aux = bits.replace('1', '0', 1)
                            bits = aux
                        else:
                            aux = bits.replace('0', '1', 1)
                            bits = aux
                    print("TRAMA ENVIADA "+ bits)
                    c.send(bits.encode('utf8', errors='replace'))
                    trama=""
                    trama += mensaje[indice]
                else:
                    if indice+1 == len(mensaje) and cont<12:
                        trama += mensaje[indice]
                        print(trama)
                        time.sleep(1)   
                        print("TRAMA FINAL ESPERADA: "+ enlace.tobits(None,trama))
                        print("LLAMANDO A LA CAPA DE ENLACE DE DATOS")

                        #validacion trama en enlace de datos
                        bits = enlace.tobits(None,trama)
                        bits = enlace.validacionTrama(None,bits)
                        if falloTrama==1:  
                            print("......FALLO EN TRAMA.....")  
                            if bits[0] =="1": 
                                aux = bits.replace('1', '0', 1)
                                bits = aux
                            else:
                                aux = bits.replace('0', '1', 1)
                                bits = aux
                        c.send(bits.encode('utf8', errors='replace'))        
                        print("TRAMA ENVIADA "+ bits)  
                    else:
                        trama += mensaje[indice]   
                        cont+=1   
                indice +=1    
        print("------------------")
        print("FIN DE CAPA DE TRANSPORTE")