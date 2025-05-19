from entities.Requerimiento import Requerimiento #importamos clase

class Maquina:
    
    _next_codigo: int = 1  #contador de id unico cada vez que se cree un cliente, atributo de clase

    def __init__(self, descripcion: str, requerimientos: list[Requerimiento]):

        self.codigo = Maquina._next_codigo   #asigno id unico
        Maquina._next_codigo += 1     #asignamos un nuevo id a cada nueva maquina, incrementamos el valor para la proxima

        # atributos de instancia
        self.descripcion = descripcion    
        self.requerimientos = requerimientos
