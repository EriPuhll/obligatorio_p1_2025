class ExceptionTelefonoInvalido (Exception):
    def __init__(self, mensaje: str = "El número de teléfono es inválido."):
        super().__init__(mensaje)
    pass