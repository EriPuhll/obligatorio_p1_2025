from datetime import datetime
from entities.piezas import Pieza
from typing import Optional

class Reposicion:
    # Contador de clase para ids de reposición
    _next_id: int = 1

    def __init__(self, pieza: Pieza, lotes: int, fecha_reposicion: Optional[datetime] = None):
    
      # Asigno el siguiente ID disponible       
        self.id = Reposicion._next_id # ID único de la reposición
                  
        Reposicion._next_id += 1 # Incremento el contador de IDs

        self.pieza = pieza                
        self.lotes = lotes               
        self.fecha_reposicion = fecha_reposicion or datetime.now() # Fecha de la reposición
