class Pessoa:
    def __init__(self, cpf: str, nome: str, dataNascimento, endereco: object):
        self.__cpf = cpf
        self.__nome = nome
        self.__idade = dataNascimento
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def endereco(self):
        return self.__endereco
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

        