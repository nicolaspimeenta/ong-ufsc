class Endereco:
    def __init__(self, cep: str, numero: int, tipo: str, tamanho: str, animais: int):
        self.__cep = cep
        self.__numero = numero
        self.__tipo = tipo
        self.__tamanho = tamanho
        self.__animais = animais

    @property
    def cep(self):
        return self.__cep
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    @property
    def animais(self):
        return self.__animais
    
    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

    @animais.setter
    def animais(self, animais):
        self.__animais = animais