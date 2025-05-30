from entities.Pieza import Pieza  #importamos clase

import typing

if typing.TYPE_CHECKING:
    from entities.Maquina import Maquina  # Importamos clase Maquina para evitar problemas de referencia circular

class Requerimiento:
    
    def __init__(self, maquina: "Maquina", pieza: "Pieza", cantidad: int):

        #atributos de instancia
        self.maquina = maquina 
        self.pieza = pieza
        self.cantidad = cantidad
