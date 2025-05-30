from datetime import datetime #importamos libreria
from typing import Optional
from entities.Cliente import Cliente 
from entities.Maquina import Maquina #importamos clase

class Pedido:

  _next_id = 1  #contador de id unico cada vez que se cree un pedido, atributo de clase
  
  def __init__(self, cliente: Cliente, maquina: Maquina, fecha_recibido: datetime, fecha_entregado: Optional[datetime] = None, estado: str = "pendiente", precio: float = 0):

    self.id = Pedido._next_id #asigno id
    Pedido._next_id += 1 #incremento id para el proximo pedido     

    #atributos de asociación
    self.cliente = cliente
    self.maquina = maquina

    #atributos de instancia
    self.fecha_recibido = fecha_recibido
    self.fecha_entregado = fecha_entregado
    self.estado = estado
    self.precio = precio
