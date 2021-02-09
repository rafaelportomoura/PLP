from pessoa import Pessoa

class Medico(Pessoa):
  def __init__(self,nome):
    super().__init__(nome)
  def definir_id(self, id):
    if (len(id) > 3):
      print("[ERRO]: identificador tem tamanho maior que 5 caracteres!")
    else: 
      self.id = id
  def nome_medico(self):
    return self.nome