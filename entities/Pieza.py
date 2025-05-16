class Pieza:
    _next_id: int = 1

    def __init__(self, descripcion: str, costo: float, tam_lote: int, stock_inicial: int = 0): 
      
      self.id = Pieza._next_id
      Pieza._next_id += 1

      self.descripcion = descripcion
      self.costo = costo
      self.tam_lote = tam_lote
      self.stock = stock_inicial
