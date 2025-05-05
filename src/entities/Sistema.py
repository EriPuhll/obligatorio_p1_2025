
from entities.pieza import Pieza
from entities.maquina import Maquina
from entities.cliente import Cliente
from entities.pedido import Pedido
from entities.reposicion import Reposicion

class Sistema:
  def __init__(self):
    self.piezas = Dict [ int, Pieza ] = {}
    self.maquinas = Dict [ int, Maquina ] = {}
    self.clientes = Dict [ int, Cliente ] ={}
    self.pedidos = Dict [ int, Pedido ] = {}
    self.reposiciones = List [ Reposicion ] = []
