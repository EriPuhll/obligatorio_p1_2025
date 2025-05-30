#importo libreria
from datetime import datetime

#importo clases
from entities.Maquina import Maquina
from entities.Pedido import Pedido
from entities.Pieza import Pieza
from entities.Cliente import Cliente
from entities.Reposicion import Reposicion

#importo excepciones
from exceptions.ExceptionClienteYaExiste import ExceptionClienteYaExiste
from exceptions.ExceptionPiezaYaExiste import ExceptionPiezaYaExiste
from exceptions.ExceptionMaquinaYaExiste import ExceptionMaquinaYaExiste


class Sistema():
    def __init__(self):

        #diccionario con su valor de clase
        self.piezas: dict[int, Pieza] = dict() 
        self.maquinas: dict[int, Maquina] = dict()
        self.clientes: dict[int, Cliente] = dict()
        self.pedidos: dict[int, Pedido] = dict()
        #lista que guarda objetos de reposición
        self.reposiciones: list[Reposicion] = list()

  
#__________________Registro__________________________

    def registrar_cliente(self, cliente):
        for c in self.clientes.values():
            if isinstance(cliente, type(c)) and cliente.id_unico == c.id_unico: #compara si el tipo y el id_unico coinciden con alguno que ya existe
               raise ExceptionClienteYaExiste() #en el caso de que exista levantamos la excepción ClienteYaExiste
        self.clientes[cliente.id] = cliente  #si no lo agrega al diccionario con su id


    def registrar_pieza(self, pieza):
      for p in self.piezas.values():  #recorre todas las piezas registradas
        if p.descripcion == pieza.descripcion: #busca por las descripciones
          raise ExceptionPiezaYaExiste() #si hay una igual levanta la excepción PiezaYaExiste 
      self.piezas[pieza.id] = pieza #si no lo agrega al diccionario con su id
    

    def registrar_maquina(self, maquina):
        for m in self.maquinas.values(): #recorre todas las maquinas registradas
            if m.descripcion == maquina.descripcion: #busca por las descripciones
                raise ExceptionMaquinaYaExiste("Ya existe una máquina con esa descripción.") #si hay una igual levanta la excepción PiezaYaExiste 
        self.maquinas[maquina.codigo] = maquina   #si no lo agrega al diccionario con su id


    def registrar_reposicion(self, pieza, lotes):
      reposicion = Reposicion(pieza=pieza, lotes=lotes, fecha_reposicion=datetime.now()) #creamos una nueva reposición para una pieza y cantidad, usamos la fecha actual
      self.actualizar_stock_por_reposicion(reposicion) #modifica el stock con la función actualizar_stock
      self.reposiciones.append(reposicion) #lo agrega a la lista


#______________________________Funcionalidades_______________________________________



    def completar_pedidos_pendientes(self):
        for pedido in self.pedidos.values():
            if pedido.estado == "pendiente" and self.hay_stock_suficiente(pedido.maquina): #si el pedido está pendiente y hay stock suficiente
                pedido.estado = "entregado" #se marca entregado
                pedido.fecha_entrega = datetime.now() #registramos fecha de entrega
                self.actualizar_stock_por_pedido(pedido) #descuenta stock con función
                print(f"Pedido {pedido} ahora está entregado.") #printea el nuevo estado

    def hay_stock_suficiente(self, maquina):
        for req in maquina.requerimientos:
            if req.pieza.cantidad_disponible < req.cantidad: #verifica que todas las piezas que una máquina necesite, tengan suficiente stock
                return False #si no tiene retorna False
        return True #si todas tienen stock retorna True

    def actualizar_stock_por_pedido(self, pedido):
        for req in pedido.maquina.requerimientos:
            req.pieza.cantidad_disponible -= req.cantidad #una vez que se entregado el pedido descuenta del stock de cada pieza
            
#_______________________Listado_______________________________

    #devuelven una lista con todos los objetos registrados en sus diccionarios
    
    def listar_clientes(self):
        return list(self.clientes.values())

    def listar_piezas(self):
        return list(self.piezas.values())

    def listar_maquinas(self):
        return list(self.maquinas.values())

    def listar_reposiciones(self):
        return self.reposiciones  # es una lista, no hace falta convertirlo

    # devuelve todos los pedidos, se puede filtrar pot estado
    def listar_pedidos(self, estado=None):
        pedidos = list(self.pedidos.values())
        if estado:
            pedidos = [p for p in pedidos if p.estado == estado]
        return pedidos
