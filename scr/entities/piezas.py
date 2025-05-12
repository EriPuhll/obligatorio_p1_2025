
class Pieza: 

  # Contador de clase para generar códigos únicos
  _next_id: int = 1
  
  def __init__(self, descripcion: str, costo: float, tam_lote: int, stock_iniical: int):

  # Asigno el siguiente ID disponible
    
        self.codigo = Pieza._next_id  # Pieza._next_id contiene el siguiente valor de id
        Pieza._next_id += 1  # incremento el contador para la próxima instancia

  # Inicializo los atributos de instancia
    
        self.descripcion = descripcion
        self.costo = costo
        self.tam_lote = tam_lote
        self.stock = stock_inicial
