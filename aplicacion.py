class aplicacion:

    def __init__(self, nombre):
        self.nombre = nombre

    def metodo(self):
        """Imprime un saludo en pantalla."""
        print(f"¡Hola, {self.nombre}!")


presentacion = aplicacion("Pablo")
presentacion.metodo()