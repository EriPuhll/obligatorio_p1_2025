from datetime import datetime

from entities.exceptions.ClienteYaExiste import ExceptionClienteYaExiste
from entities.exceptions.PiezaYaExiste import ExceptionPiezaYaExiste
from entities.exceptions.MaquinaYaExiste import ExceptionMaquinaYaExiste

from entities.piezas import Pieza
from entities.maquinas import Maquina
from entities.clientes import Cliente
from entities.pedidos import Pedido
from entities.reposiciones import Reposicion

class Sistema():
    def __init__(self):
      self.piezas: dict[int, Pieza] = dict()
      self.maquinas: dict[int, Maquina] = dict()
      self.clientes: dict[int, Cliente] = dict()
      self.pedidos: dict[int, Pedido] = dict()
      self.reposiciones: list[Reposicion] = list()

  
#__________________Registro__________________________

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
    

    def registrar_maquina(self, descripcion, requerimientos):
      for m in self.maquinas.values():
        if m.descripcion == descripcion:
            raise ExceptionMaquinaYaExiste("Ya existe una máquina con esa descripción.")

      maquina = Maquina(descripcion=descripcion, requerimientos=requerimientos)
      self.maquinas[maquina.codigo] = maquina

    def registrar_reposicion(self, pieza, lotes):
      reposicion = Reposicion(pieza=pieza, lotes=lotes, fecha_reposicion=datetime.now())
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

#_______________________Listado_______________________________

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
