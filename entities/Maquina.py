
import typing

if typing.TYPE_CHECKING:
    from entities.Requerimiento import Requerimiento

class Maquina:
    
    _next_codigo: int = 1  #contador de id unico cada vez que se cree un cliente, atributo de clase

    def __init__(self, descripcion: str, requerimientos: "Requerimiento"):

        self.codigo = Maquina._next_codigo   #asigno id unico
        Maquina._next_codigo += 1     #asignamos un nuevo id a cada nueva maquina, incrementamos el valor para la proxima

        # atributos de instancia
        self.descripcion = descripcion    
        self.requerimientos = requerimientos

   
     # calcular costo total de maquina
 
        suma = 0
        for i in range (0, len(requerimientos)):
            suma += requerimientos.pieza.costo
        self.costo = suma
           

