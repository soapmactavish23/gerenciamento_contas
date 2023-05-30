class Conta():
    def __init__(self, nome, resumo, valor):
        self.__nome = nome
        self.__resumo = resumo
        self.__valor = valor

    @property
    def nome(self):
        self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def resumo(self):
        self.__resumo

    @resumo.setter
    def resumo(self, resumo):
        self.__resumo = resumo

    @property
    def valor(self):
        self.valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor