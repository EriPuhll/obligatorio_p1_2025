class ExceptionCorreoInvalido(Exception):
    def __init__(self, mensaje = "El correo electronico ingresado es invalido."):
        super().__init__(mensaje)
    pass