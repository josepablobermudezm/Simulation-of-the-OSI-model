import socket, os
class transporte:

    def __init__(self, nombre):
        self.nombre = nombre

    def enviarMensaje(self,c, mensaje):
        print("Mensaje Enviado: "+ mensaje)
        c.send(mensaje.encode('utf8', errors='replace'))