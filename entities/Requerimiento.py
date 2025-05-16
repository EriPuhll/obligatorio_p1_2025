from entities.Pieza import Pieza

class Requerimiento:
    def __init__(self, pieza: "Pieza", cantidad: int):
        self.pieza = pieza
        self.cantidad = cantidad
