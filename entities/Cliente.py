from typing import Optional

class Cliente:
    # Contador de clase para IDs automáticos
    _next_id: int = 1

    def __init__(self, nombre: str, telefono: str, correo: str):
        # Asigno id único
        self.id = Cliente._next_id
        Cliente._next_id += 1

        # inicializo atributos
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

class ClienteParticular(Cliente):
    def __init__(self, nombre: str, cedula: str, telefono: str, correo: str):
        super().__init__(nombre, telefono, correo)
        self.id_unico = cedula

class Empresa(Cliente):
    def __init__(self, nombre: str, telefono: str, rut: str, correo: str, pagina_web: Optional[str] = None):
        super().__init__(nombre, telefono, correo)
        self.id_unico = rut
        self.pagina_web = pagina_web
