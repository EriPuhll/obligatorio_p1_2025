from datetime import datetime
from typing import Optional
from entities.clientes import Cliente
from entities.maquinas import Maquina

class Pedido:

  _next_id = 1
  
  def __init__(self, cliente: Cliente, maquina: Maquina, fecha_recibido: datetime, fecha_entregado: datetime | None = None, estado: str = "pendiente"):

    self.id = Pedido._next_id #ID único del pedido
    Pedido._next_id += 1 #Incremento el contador de IDs      

    #atributos de asociación
    
    self.cliente = cliente
    self.maquina = maquina

    
    self.fecha_recibido = fecha_recibido
    self.fecha_entregado = fecha_entregado
    self.estado = estado
    pass
