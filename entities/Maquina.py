from entities.Requerimiento import Requerimiento

class Maquina:
    # Contador de clase para códigos de máquina
    _next_codigo: int = 1

    def __init__(self, descripcion: str, requerimientos: list[Requerimiento]):

        self.codigo = Maquina._next_codigo   # Código único de la máquina
        Maquina._next_codigo += 1     # Incremento el contador de código

        # Inicializo atributos de instancia
        self.descripcion = descripcion    # Nombre o modelo de la máquina
        self.requerimientos = requerimientos # Lista de Requerimiento para fabricar
