from medicamento import Medicamento
from medico import Medico
from datetime import datetime


class Prontuario:
    def __init__(self):
        self.__minha_lista = []

    def insere_procedimento(self, Medicamento, Posologia, Medico, Data, Hora):
        self.procedimento = {
            'medicamento': Medicamento,
            'posologia': str(Posologia),
            'medico': Medico,
            'data': str(datetime.strptime(Data, '%d-%m-%Y').date()),
            'hora': str(datetime.strptime(Hora, '%H:%M').time())
        }
        self.__minha_lista.append(self.procedimento)

    def exibe_prontuario(self):
        for procedimento in self.__minha_lista:
            print(str(procedimento['medicamento'].nome_medicamento) + ' - ' + procedimento['posologia'] + ' - ' +
                  str(procedimento['medico'].nome_medico) + ' - ' + procedimento['data'] + ' - ' + procedimento['hora'])
