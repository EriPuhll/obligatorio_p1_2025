from entities.Cliente import Cliente, ClienteParticular, Empresa
from entities.Maquina import Maquina
from entities.Pedido import Pedido
from entities.Pieza import Pieza
from entities.Reposicion import Reposicion
from entities.Requerimiento import Requerimiento
from entities.Sistema import Sistema


from exceptions.ExceptionClienteYaExiste import ExceptionClienteYaExiste
from exceptions.ExceptionPiezaYaExiste import ExceptionPiezaYaExiste
from exceptions.ExceptionMaquinaYaExiste import ExceptionMaquinaYaExiste
from exceptions.ExceptionTextoInvalido import ExceptionTextoInvalido
from exceptions.ExceptionNumeroInvalido import ExceptionNumeroInvalido
from exceptions.ExceptionTelefonoInvalido import ExceptionTelefonoInvalido
from exceptions.ExceptionCorreoInvalido import ExceptionCorreoInvalido
from exceptions.ExceptionDatoDuplicado import ExceptionDatoDuplicado


from datetime import datetime

def menu_principal():
    sistema = Sistema()
    while True:
        print("=" * 40)
        print(" " * 10 + "MENÚ PRINCIPAL")
        print("=" * 40)
        print("1. Registrar datos")
        print("2. Listar datos")
        print("3. Salir")
        print("=" * 40)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_registrar(sistema)
        elif opcion == "2":
            menu_listar(sistema)
        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_registrar(sistema):
    while True:
        print("\n" + "-" * 40)
        print(" " * 10 + "MENÚ REGISTRAR")
        print("-" * 40)
        print("1. Registrar Pieza")
        print("2. Registrar Máquina")
        print("3. Registrar Cliente")
        print("4. Registrar Pedido")
        print("5. Registrar Reposición")
        print("6. Volver al menú principal")
        print("-" * 40)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_pieza(sistema)
        elif opcion == "2":
            registrar_maquina(sistema)
        elif opcion == "3":
            registrar_cliente(sistema)
        elif opcion == "4":
            registrar_pedido(sistema)
        elif opcion == "5":
            registrar_reposicion(sistema)
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menu_listar(sistema):
    while True:
        print("_" * 40)
        print(" " * 10 + "MENÚ LISTAR")
        print("_" * 40)
        print("1. Listar Clientes")
        print("2. Listar Pedidos")
        print("3. Listar Máquinas")
        print("4. Listar Piezas")
        print("5. Mostrar Contabilidad")
        print("6. Volver al menú principal")
        print("_" * 40)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_clientes(sistema)
        elif opcion == "2":
            listar_pedidos(sistema)
        elif opcion == "3":
            listar_maquinas(sistema)
        elif opcion == "4":
            listar_piezas(sistema)
        elif opcion == "5":
            mostrar_contabilidad(sistema)
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

# ---------------- FUNCIONES AUXILIARES ----------------

def registrar_pieza(sistema):
    try:
        descripcion = input("Descripción: ")

        costo = float(input("Costo unitario (USD): "))

        lote = input("Tamaño del lote de reposición: ")

        pieza = Pieza(descripcion=descripcion, costo=costo, tam_lote=lote, stock_inicial=0)

        sistema.registrar_pieza(pieza)

        print("Pieza registrada.")

    except Exception as e:
        print(e)

def registrar_maquina(sistema):
    try:
        descripcion = input("Descripción de la máquina: ")
        
        requerimientos = []

        piezas_disponibles = sistema.listar_piezas().copy()

        while True:

            agregar = input("Agregar pieza (Si/No)? ").strip().lower()

            if agregar == "si":

                if not piezas_disponibles:
                    print("No hay más piezas disponibles para agregar.")
                    break

                print("\nPiezas disponibles:")
                for pieza in piezas_disponibles:
                    print(f"{pieza.id}: {pieza.descripcion}")

                codigo = int(input("Código de la pieza: "))

                cantidad = int(input("Cantidad necesaria: "))

                pieza = sistema.piezas.get(codigo)

                if pieza and pieza in piezas_disponibles:
                    requerimientos.append(Requerimiento(pieza=pieza, cantidad=cantidad))
                    piezas_disponibles.remove(pieza)
                else:
                    print("Pieza no encontrada o ya seleccionada.")

            elif agregar == "no":
                break

            else:
                print("Opción no válida. Escriba 'Si' o 'No'.")

        maquina = Maquina(descripcion=descripcion, requerimientos=requerimientos)

        sistema.registrar_maquina(maquina)

        print("Máquina registrada.")

    except Exception as e:
        print(f"Ocurrió un error al registrar la máquina: {e}")



def registrar_cliente(sistema):
    try:
        tipo = input("Tipo cliente (1. Particular, 2. Empresa): ")

        if tipo not in ("1", "2"):

            raise ExceptionTextoInvalido("Tipo inválido. Debe ser 1 o 2.")
        
        if tipo == "1":

            cedula = input("Cédula: ")
            
            nombre = input("Nombre completo: ")
            
            telefono = input("Teléfono: ")

            correo = input("Correo electrónico: ")

            cliente = ClienteParticular(nombre=nombre, cedula=cedula, telefono=telefono, correo=correo)
            
        elif tipo == "2":

            rut = input("RUT: ")

            nombre = input("Nombre empresa: ")

            pagina = input("Página web: ")

            telefono = input("Teléfono: ")

            correo = input("Correo electrónico: ")
            
            cliente = Empresa( nombre=nombre, telefono=telefono, rut=rut, correo=correo,pagina_web=pagina)

        else:

            print("Tipo inválido.")

            return
        
        sistema.registrar_cliente(cliente)

        print("Cliente registrado.")

    except Exception as e:
        print(e)

def registrar_pedido(sistema):
    try:
        print("Clientes:")

        for cliente in sistema.listar_clientes():       #Con la funcion listar clientes ya deberia de funcionar, creo
            
            print(f"{cliente.id}: {cliente.nombre}")

        id_cliente = int(input("ID del cliente: "))

        cliente = sistema.clientes.get(id_cliente)
        
        if not cliente:
            print("Cliente no encontrado.")
            return

        print("Máquinas disponibles:")
        for maquina in sistema.listar_maquinas():
            print(maquina)

        codigo_maquina = int(input("Código de la máquina: "))

        maquina = sistema.maquinas.get(codigo_maquina)
        if not maquina:
            print("Máquina no encontrada.")
            return


        if sistema.hay_stock_suficiente(maquina):
            estado = "entregado"
            fecha_entrega = fecha_recepcion = datetime.now()
            sistema.actualizar_stock_por_pedido(Pedido(cliente, maquina, estado, fecha_recepcion, fecha_entrega, precio_venta=0))  # para ajustar stock antes
        else:
            estado = "pendiente"
            fecha_entrega = None

        precio_base = maquina.calcular_costo_produccion() * 1.5

        if isinstance(cliente, Empresa):
            precio_venta = precio_base * 0.8
        else:
            precio_venta = precio_base
        
        pedido = Pedido(cliente=cliente, maquina=maquina, estado="", fecha_recepcion=datetime.now(), fecha_entrega=None, precio_venta=0)
        
        sistema.registrar_pedido(pedido)

        print("Pedido registrado.")

    except Exception as e:
        print(e)


def registrar_reposicion(sistema):
    try:

        print("Piezas disponibles:")

        for pieza in sistema.listar_piezas():
            print(pieza)

        codigo = int(input("Código de la pieza: "))

        pieza = sistema.piezas.get(codigo)

        if not pieza:
            print("Pieza no encontrada.")
            return

        cantidad_lotes = int(input("Cantidad de lotes a reponer: "))

        if cantidad_lotes <= 0:
            raise ExceptionNumeroInvalido("La cantidad de lotes debe ser un número positivo.")
        
        reposicion = Reposicion(pieza=pieza, cantidad_lotes=cantidad_lotes, fecha_reposicion=None)

        sistema.registrar_reposicion(reposicion)

        print("Reposición registrada.")

    except Exception as e:
        print(e)

def listar_clientes(sistema):
    cliente = sistema.listar_clientes()
    if not cliente:
        print("No hay clientes registrados.")
    for cliente in cliente:
        print(cliente)
...




"""
FALTA

Revisar registrar pedido y reposicion
Revisar y poner condiciones de formato de ingreso
Ver mas excepciones
Listar pedidos
Listar máquinas
Listar piezas
Listar contabilidad
"""
# ---------------- EJECUCIÓN ----------------
if __name__ == "__main__":
    menu_principal()

