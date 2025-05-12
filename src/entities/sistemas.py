from exceptions.ExceptionClienteYaExiste import ExceptionClienteYaExiste
from exceptions.ExceptionPiezaYaExiste import ExceptionPiezaYaExiste
from exceptions.ExceptionMaquinaYaExiste import ExceptionMaquinaYaExiste

from entities.pieza import Pieza
from entities.maquina import Maquina
from entities.cliente import Cliente
from entities.pedido import Pedido
from entities.reposicion import Reposicion

class Sistema:
  def __init__(self):
  self.piezas: Dict[int, Pieza] = {}
  self.maquinas: Dict[int, Maquina] = {}
  self.clientes: Dict[int, Cliente] = {}
  self.pedidos: Dict[int, Pedido] = {}
  self.reposiciones: List[Reposicion] = []
#__________________REGISTRO__________________________

   def registrar_cliente(self, cliente):
     for c in self.clientes:
        if isinstance(cliente, type(c)) and cliente.id_unico == c.id_unico:
            raise ExceptionClienteYaExiste()
    cliente.id = self.next_id_cliente
    self.next_id_cliente += 1
    self.clientes.append(cliente)

    def registrar_pieza(self, pieza):
      for p in self.piezas:
        if p.descripcion == pieza.descripcion:
          raise ExceptionPiezaYaExiste()
      pieza.codigo = self.next_codigo_pieza
      self.next_codigo_pieza += 1
      self.piezas.append(pieza)
    

    def registrar_maquina(self, maquina):
      for m in self.maquinas:
        if m.descripcion == descripcion:
          raise Exception("Ya existe una máquina con esa descripción.")
      maquina = Maquina(codigo=self.next_codigo_maquina, descripcion=descripcion, requerimientos=requerimientos)
      maquina.calcular_costo_produccion()
      self.maquinas.append(maquina)
      self.next_codigo_maquina += 1

    def registrar_pedido(self, pedido):
      estado = "entregado"
        if self.hay_stock_suficiente(maquina)
        else "pendiente"
        pedido = Pedido(cliente=cliente, maquina=maquina, estado=estado, fecha_recepcion=datetime.now())
        if estado == "entregado":
          pedido.fecha_entrega = pedido.fecha_recepcion
          self.actualizar_stock_por_pedido(pedido)
        self.pedidos.append(pedido)

    def registrar_reposicion(self, reposicion):
      reposicion = Reposicion(pieza=pieza, cantidad_lotes=cantidad_lotes, fecha_reposicion=datetime.now())
      self.actualizar_stock_por_reposicion(reposicion)
      self.reposiciones.append(reposicion)

#______________________________Funcionalidades_______________________________________


# Ejemplo de método para verificar y completar pedidos pendientes
    def completar_pedidos_pendientes(self):
        for pedido in self.pedidos:
            if pedido.estado == "pendiente" and self.hay_stock_suficiente(pedido.maquina):
                pedido.estado = "entregado"
                pedido.fecha_entrega = datetime.now()
                self.actualizar_stock_por_pedido(pedido)
                print(f"Pedido {pedido} ahora está entregado.")

    # Método para verificar si existe stock suficiente
    def hay_stock_suficiente(self, maquina):
        for req in maquina.requerimientos:
            if req.pieza.cantidad_disponible < req.cantidad:
                return False
        return True

    # Método para descontar piezas tras entregar pedido
    def actualizar_stock_por_pedido(self, pedido):
        for req in pedido.maquina.requerimientos:
            req.pieza.cantidad_disponible -= req.cantidad

#_______________________Listar_______________________________

def listar_clientes(self):
    return list(self.clientes.values())

def listar_piezas(self):
    return list(self.piezas.values())

def listar_maquinas(self):
    return list(self.maquinas.values())

def listar_pedidos(self, estado=None):
    pedidos = list(self.pedidos.values())
    if estado:
        pedidos = [p for p in pedidos if p.estado == estado]
    return pedidos

def listar_reposiciones(self):
    return self.reposiciones  # es una lista, no hace falta convertir

def calcular_contabilidad(self):
    costo_total = 0
    ingreso_total = 0

    for pedido in self.pedidos.values():
        if pedido.estado == "entregado":
            costo_total += pedido.maquina.costo_produccion
            ingreso_total += pedido.precio_venta

    ganancia = ingreso_total - costo_total
    impuesto = ganancia * 0.25 if ganancia > 0 else 0
    ganancia_final = ganancia - impuesto

    return {
        "costo_total": costo_total,
        "ingreso_total": ingreso_total,
        "ganancia_bruta": ganancia,
        "impuesto": impuesto,
        "ganancia_neta": ganancia_final
    }
