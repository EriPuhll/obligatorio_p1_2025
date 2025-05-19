class Pieza:
    
    _next_id: int = 1 #contador de id unico cada vez que se cree una pieza, atributo de clase

    def __init__(self, descripcion: str, costo: float, tam_lote: int, stock_inicial: int = 0): 
      
        self.id = Pieza._next_id #asigno id
        Pieza._next_id += 1    #incremento id para la proxima pieza 

        #atributos de instancia
        self.descripcion = descripcion
        self.costo = costo
        self.tam_lote = tam_lote
        self.stock = stock_inicial
