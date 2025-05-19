from entities.Pieza import Pieza  #importamos clase

class Requerimiento:
    
    def __init__(self, pieza: "Pieza", cantidad: int):

        #atributos de instancia
        self.pieza = pieza
        self.cantidad = cantidad
