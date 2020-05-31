import socket, os
from .enlace import enlace
class transporte:

    def __init__(self, nombre):
        self.nombre = nombre

    def enviarMensaje(self,c, mensaje):
        print("------------------")
        print("CAPA DE TRANSPORTE")
        print("MENSAJE DIGITADO: "+ mensaje)
        print("LLAMANDO A LA CAPA DE ENLACE DE DATOS")
        c.send(enlace.tobits(None,mensaje).encode('utf8', errors='replace'))
        print("------------------")