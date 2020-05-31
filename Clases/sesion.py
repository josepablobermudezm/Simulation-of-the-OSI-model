import socket, os
from .transporte import transporte
class sesion:

    def __init__(self, nombre):
        self.nombre = nombre

    def conectar(self, host, puerto, mensaje):
        print("------------------")
        print("CAPA DE SESION")
        print("CREANDO SESION")
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect((host, puerto))
        #llama a la capa de tranporte
        transporte.enviarMensaje(None,c, mensaje)
        print("CERRANDO SESION")
        print("------------------")
        #cierra la sesion
        c.close()