class ExceptionDatoDuplicado (Exception):
    def __init__(self, mensaje = "El dato ingresado ya existe."):
        super.__init__(mensaje)
    pass