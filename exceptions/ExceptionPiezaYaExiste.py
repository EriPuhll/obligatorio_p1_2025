class ExceptionPiezaYaExiste(Exception):
    def __init__(self, mensaje="Ya existe una pieza con esa descripción."):
        super().__init__(mensaje)
    pass
