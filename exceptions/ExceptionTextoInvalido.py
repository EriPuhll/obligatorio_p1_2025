class ExceptionTextoInvalido(Exception):
    def __init__(self, mensaje="El texto ingresado contiene números, símbolos o está vacío."):
        super().__init__(mensaje)
