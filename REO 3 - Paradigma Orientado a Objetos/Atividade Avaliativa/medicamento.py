class Medicamento:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome_medicamento(self):
        return self.__nome
