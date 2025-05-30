from entities.Pieza import Pieza #importo clase
from typing import Optional 
from datetime import datetime #importo libreria

class Reposicion:
    
    _next_id: int = 1 #contador de id unico cada vez que se cree una reposición, atributo de clase

    def __init__(self, pieza: Pieza, lotes: int, fecha_reposicion: Optional[datetime] = None):
      
        self.id = Reposicion._next_id #asigno id      
        Reposicion._next_id += 1 #incremento id para proxima reposición

        #atributos de instancia
        self.pieza = pieza                
        self.lotes = lotes               
        self.fecha_reposicion = fecha_reposicion or datetime.now()
