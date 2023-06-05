class Operacao():
    def __init__(self,nome, resumo, custo, tipo):
        self.__nome = nome
        self.__resumo = resumo
        self.__custo = custo
        self.__tipo = tipo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def resumo(self):
        return self.resumo

    @resumo.setter
    def nome(self, resumo):
            self.resumo = resumo

    @property
    def custo(self):
        return self.custo

    @custo.setter
    def nome(self, custo):
        self.custo = custo

    @property
    def tipo(self):
        return self.tipo

    @tipo.setter
    def nome(self, tipo):
        self.tipo = tipo