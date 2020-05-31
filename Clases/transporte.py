import socket, os
class transporte:

    def __init__(self, nombre):
        self.nombre = nombre

    def enviarMensaje(self,c, mensaje):
        print("------------------")
        print("CAPA DE TRANSPORTE")
        print("MENSAJE DIGITADO: "+ mensaje)
        c.send(mensaje.encode('utf8', errors='replace'))
        print("------------------")