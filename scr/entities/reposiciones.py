class Reposicion:
    # Contador de clase para ids de reposición
    _next_id: int = 1

    def __init__(self, pieza: Pieza, lotes: int, fecha_reposicion: datetime | None = None
                ):
        # Asigno el siguiente ID disponible
                  
        self.id = Reposicion._next_id       # ID único de la reposición
                  
        Reposicion._next_id += 1            # Incremento el contador de IDs

        self.pieza = pieza                  # Pieza que se repone
        self.lotes = lotes                  # Cantidad de lotes adquiridos
        self.fecha_reposicion = fecha_reposicion or datetime.now() # Fecha de la reposición
