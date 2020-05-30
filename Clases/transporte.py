import socket, os
class transporte:

    def __init__(self, nombre):
        self.nombre = nombre

    def metodo(self):
        """Imprime un saludo en pantalla."""
        print(f"¡Hola, {self.nombre}!")
    def enviarMensaje(self,c, mensaje):
        mensaje = c.recv(1024)
        print()
        print (mensaje.decode('utf8'))
        c.send(mensaje.encode('ascii', errors='replace'))