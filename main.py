from scr.sistema import Sistema
from scr.entities.pieza import Pieza
from scr.entities.maquina import Maquina
from scr.entities.requerimiento import Requerimiento
from scr.entities.cliente import ClienteParticular, Empresa
from scr.entities.pedido import Pedido
from scr.entities.reposicion import Reposicion

def menu_principal():
    sistema = Sistema()
    while True:
        print("___________________________")
        print("\n___ Menú Principal ___")
        print("__________________________")
        print("1. Registrar")
        print("2. Listar")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_registrar(sistema)
        elif opcion == "2":
            menu_listar(sistema)
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("La opción es inválida.")

def menu_registrar(sistema):
    while True:
        print("__________________________")
        print("\n___ Menú Registrar ___")
        print("__________________________")
        print("1. Pieza")
        print("2. Máquina")
        print("3. Cliente")
        print("4. Pedido")
        print("5. Reposición")
        print("6. Salir")
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
            print("La opción es inválida.")

def menu_listar(sistema):
    while True:
        print("__________________________")
        print("\n___ Menú Listar ___")
        print("__________________________")
        print("1. Clientes")
        print("2. Pedidos")
        print("3. Máquinas")
        print("4. Piezas")
        print("5. Contabilidad")
        print("6. Salir")
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
        pieza = Pieza(codigo=0, descripcion=descripcion, costo_unitario=costo, tam_lote_reposicion=lote, cantidad_disponible=0)
        sistema.registrar_pieza(pieza)
        print("Pieza registrada exitosamente.")
    except Exception as e:
        print(e)

def registrar_maquina(sistema):
    print("Registrar máquina (completalo como hiciste en Sistema)")

def registrar_cliente(sistema):
    print("Registrar cliente (completalo como hiciste en Sistema)")

def registrar_pedido(sistema):
    print("Registrar pedido (completalo como hiciste en Sistema)")

def registrar_reposicion(sistema):
    print("Registrar reposición (completalo como hiciste en Sistema)")

def listar_clientes(sistema):
    print("Listado de clientes (acá llamás al método de Sistema)")

def listar_pedidos(sistema):
    print("Listado de pedidos (acá llamás al método de Sistema)")

def listar_maquinas(sistema):
    print("Listado de máquinas (acá llamás al método de Sistema)")

def listar_piezas(sistema):
    print("Listado de piezas (acá llamás al método de Sistema)")

def mostrar_contabilidad(sistema):
    print("Mostrar contabilidad (acá llamás al método de Sistema)")

# ---------------- EJECUCIÓN ----------------
if __name__ == "__main__":
    menu_principal()


