from typing import Optional

class Cliente:
    
    _next_id: int = 1  #contador de id unico cada vez que se cree un cliente, atributo de clase

    def __init__(self, nombre: str, telefono: str, correo: str):
        # Asigno id único
        self.id = Cliente._next_id 
        Cliente._next_id += 1 #asignamos un nuevo id a cada nuevo cliente, incrementamos el valor para el proximo cliente

        # inicializo atributos de instancia
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

class ClienteParticular(Cliente): #hereda de cliente
    def __init__(self, nombre: str, cedula: str, telefono: str, correo: str):
        super().__init__(nombre, telefono, correo) #llamamos al constructor de la clase padre
        self.id_unico = cedula #plus el nuevo atributo

class Empresa(Cliente): #hereda de cliente
    def __init__(self, nombre: str, telefono: str, rut: str, correo: str, pagina_web: Optional[str] = None):
        super().__init__(nombre, telefono, correo)  #llamamos al constructor de la clase padre
        self.id_unico = rut             #plus nuevos atributos
        self.pagina_web = pagina_web        #guardamos la página web si se ingresa, si no, queda como None.
