from pessoa import Pessoa
from prontuario import Prontuario


class Paciente(Pessoa):
    __total_pacientes = 0

    def __init__(self, nome):
        super().__init__(nome)
        Paciente.__total_pacientes += 1

    def __del__(self):
        Paciente.__total_pacientes -= 1

    @classmethod
    def pacientes_ativos(cls):
        return cls.__total_pacientes

    def definir_id(self, id):
        if (len(id) > 5):
            print("[ERRO]: identificador tem tamanho maior que 5 caracteres!")
        else:
            self.id = id

    def definir_prontuario(self, Prontuario):
        self.prontuario = Prontuario
