from pessoa import Pessoa


class Medico(Pessoa):
    def __init__(self, nome):
        self.__nome = nome

    def definir_id(self, id):
        if (len(id) > 3):
            print("[ERRO]: identificador tem tamanho maior que 5 caracteres!")
        else:
            self.__id = id

    @property
    def nome_medico(self):
        return self.__nome
