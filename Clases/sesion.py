import socket, os
from .transporte import transporte
class sesion:

    def __init__(self, nombre):
        self.nombre = nombre

    def conectar(self, host, puerto, mensaje):
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect((host, puerto))
        #llama a la capa de tranporte
        transporte.enviarMensaje(None,c, mensaje)
        #cierra la sesion
        c.close()

    def metodo(self):
        """Imprime un saludo en pantalla."""
        print(f"¡Hola, {self.nombre}!")