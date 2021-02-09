from medicamento import Medicamento
from medico import Medico
class Prontuario:
  def __init__(self):
    self.__minha_lista = []
  def inseri_procedimento(self,Medicamento,Medico,Posologia,Data,Hora):
    self.procedimento = {
      medicamento: Medicamento,
      posologia: Posologia,
      medico: Medico,
      data: Data,
      hora: Hora
    }
    __minha_lista.push(self.procedimento)
  def exibe_prontuario(self):
    for procedimento in __minha_lista:
      procedimento
    
