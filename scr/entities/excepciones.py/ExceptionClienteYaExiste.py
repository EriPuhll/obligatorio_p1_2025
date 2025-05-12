
class ExceptionClienteYaExiste(Exception):
    def __init__(self, mensaje="El cliente ya existe."):
        super().__init__(mensaje)

