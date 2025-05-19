from entities.Pieza import Pieza  #importamos clase
from entities.Maquina import Maquina

class Requerimiento:
    
    def __init__(self, maquina: "Maquina", pieza: "Pieza", cantidad: int):

        #atributos de instancia
        self.maquina = maquina 
        self.pieza = pieza
        self.cantidad = cantidad
