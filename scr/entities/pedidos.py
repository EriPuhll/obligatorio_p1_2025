from datetime import datetime
from entities.cliente import Cliente
from entities.maquina import Maquina

class Pedido:

  next_id = 1
  
  def __init__(self, cliente: Cliente, maquina: Maquina, fecha_recibido: datetime, fecha_entregado: datetime, estado: str):

    self.id = Pedido._next_id 
    Pedido.next_id += 1      
    
    self.cliente = cliente
    self.maquina = maquina
    self.fecha_recibido = fecha_recibido
    self.fecha_entregado = fecha_entregado
    self.estado = estado
    
