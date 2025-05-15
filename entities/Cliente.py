from typing import Optional

class Cliente:
    # Contador de clase para IDs automáticos
    _next_id: int = 1

    def __init__(self, nombre: str, email: Optional[str] = None, es_empresa: bool = False):
        # Asigno ID único
        self.id = Cliente._next_id
        Cliente._next_id += 1

        # Inicializo atributos
        self.nombre = nombre
        self.email = email
        self.es_empresa = es_empresa

class ClienteParticular(Cliente):
    def __init__(self, nombre: str, cedula: str, email: Optional[str] = None):
        super().__init__(nombre, email, es_empresa=False)
        self.cedula = cedula

class Empresa(Cliente):
    def __init__(self, nombre: str, rut: str, pagina_web: Optional[str] = None, email: Optional[str] = None):
        super().__init__(nombre, email, es_empresa=True)
        self.rut = rut
        self.pagina_web = pagina_web
