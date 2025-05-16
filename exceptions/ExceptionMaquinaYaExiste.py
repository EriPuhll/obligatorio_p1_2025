class ExceptionMaquinaYaExiste(Exception):
    def __init__(self, mensaje="Ya existe una máquina con esa descripción."):
        super().__init__(mensaje)
