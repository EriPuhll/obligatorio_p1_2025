from entities.piezas import Pieza
from entities.maquinas import Maquina
from entities.requerimientos import Requerimiento
from entities.clientes import Cliente
from entities.clientes import ClienteParticular, Empresa
from entities.pedidos import Pedido
from entities.reposiciones import Reposicion
from entities.sistemas import Sistema
from datetime import datetime


def menu_principal():
    sistema = Sistema()
    while True:
        print("\n" + "=" * 40)
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
        print(" " + "-" * 40)
        print(" " * 10 + "MENÚ LISTAR")
        print("-" * 40)
        print("1. Listar Clientes")
        print("2. Listar Pedidos")
        print("3. Listar Máquinas")
        print("4. Listar Piezas")
        print("5. Mostrar Contabilidad")
        print("6. Volver al menú principal")
        print("-" * 40)
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
        lote = int(input("Tamaño del lote de reposición: "))
        pieza = Pieza(codigo=0, descripcion=descripcion, costo_unitario=costo,
                      tamano_lote_reposicion=lote, cantidad_disponible=0)
        sistema.registrar_pieza(pieza)
        print("Pieza registrada.")
    except Exception as e:
        print(e)

def registrar_maquina(sistema):
    try:
        descripcion = input("Descripción de la máquina: ")
        requerimientos = []
        while True:
            agregar = input("Agregar pieza (s/n)? ").lower()
            if agregar != 's':
                break
            piezas = sistema.listar_piezas()
            for pieza in piezas:
                print(f"{pieza.codigo}: {pieza.descripcion}")
            codigo = int(input("Código de la pieza: "))
            cantidad = int(input("Cantidad necesaria: "))
            pieza = sistema.piezas.get(codigo)
            if pieza:
                requerimientos.append(Requerimiento(pieza=pieza, cantidad=cantidad))
            else:
                print("Pieza no encontrada.")

        maquina = Maquina(codigo=0, descripcion=descripcion, requerimientos=requerimientos)
        sistema.registrar_maquina(maquina)
        print("Máquina registrada.")
    except Exception as e:
        print(e)

def registrar_cliente(sistema):
    try:
        tipo = input("Tipo cliente (1. Particular, 2. Empresa): ")
        if tipo == "1":
            cedula = input("Cédula: ")
            nombre = input("Nombre completo: ")
            telefono = input("Teléfono: ")
            correo = input("Correo electrónico: ")
            cliente = ClienteParticular(cedula=cedula, nombre_completo=nombre,
                                        telefono=telefono, correo_electronico=correo)
        elif tipo == "2":
            rut = input("RUT: ")
            nombre = input("Nombre empresa: ")
            pagina = input("Página web: ")
            telefono = input("Teléfono: ")
            correo = input("Correo electrónico: ")
            cliente = Empresa(rut=rut, nombre=nombre, pagina_web=pagina,
                              telefono=telefono, correo_electronico=correo)
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
        for cliente in sistema.listar_clientes():
            print(cliente)

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

        pedido = Pedido(cliente=cliente, maquina=maquina, estado="",
                        fecha_recepcion=datetime.now(), fecha_entrega=None, precio_venta=0)
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
        reposicion = Reposicion(pieza=pieza, cantidad_lotes=cantidad_lotes,
                                fecha_reposicion=None)
        sistema.registrar_reposicion(reposicion)
        print("Reposición registrada.")
    except Exception as e:
        print(e)

def listar_clientes(sistema):
    for cliente in sistema.listar_clientes():
        print(cliente)

def listar_pedidos(sistema):
    opcion = input("Filtrar pedidos? (1. Pendientes, 2. Entregados, otro = Todos): ")
    if opcion == "1":
        pedidos = sistema.listar_pedidos(estado="pendiente")
    elif opcion == "2":
        pedidos = sistema.listar_pedidos(estado="entregado")
    else:
        pedidos = sistema.listar_pedidos()
    for pedido in pedidos:
        print(pedido)

def listar_maquinas(sistema):
    for maquina in sistema.listar_maquinas():
        print(maquina)

def listar_piezas(sistema):
    for pieza in sistema.listar_piezas():
        print(pieza)

def mostrar_contabilidad(sistema):
    resumen = sistema.calcular_contabilidad()
    print(f"Costo total: {resumen['costo_total']:.2f} USD")
    print(f"Ingreso total: {resumen['ingreso_total']:.2f} USD")
    print(f"Ganancia bruta: {resumen['ganancia_bruta']:.2f} USD")
    print(f"Impuesto (25%): {resumen['impuesto']:.2f} USD")
    print(f"Ganancia neta: {resumen['ganancia_neta']:.2f} USD")


# ---------------- EJECUCIÓN ----------------
if __name__ == "__main__":
    menu_principal()

