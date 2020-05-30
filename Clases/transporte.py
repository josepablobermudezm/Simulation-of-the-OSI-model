import socket, os
class transporte:

    def __init__(self, nombre):
        self.nombre = nombre

    def metodo(self):
        """Imprime un saludo en pantalla."""
        print(f"¡Hola, {self.nombre}!")
    def enviarMensaje(self,c, mensaje):
        print("Mensaje Enviado: "+ mensaje)
        c.send(mensaje.encode('utf8', errors='replace'))