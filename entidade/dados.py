class Dados:
    def __init__(self):
        self.__pessoas = []
        self.__enderecos = []
        self.__animais = []
        self.__vacinas = []
        self.__doacoes = []
        self.__adocoes = []

    @property
    def pessoas(self):
        return self.__pessoas
    
    @property
    def enderecos(self):
        return self.__enderecos
    
    @property
    def animais(self):
        return self.__animais
    
    @property
    def vacinas(self):
        return self.__vacinas
    
    @property
    def doacoes(self):
        return self.__doacoes
    
    @property
    def adocoes(self):
        return self.__adocoes
    
    def savePessoa(self, pessoa):
        self.__pessoas.append(pessoa)

    def saveEndereco(self, endereco):
        self.__enderecos.append(endereco)

    def saveAnimal(self, animal):
        self.__animais.append(animal)

    def saveVacina(self, vacina):
        self.__vacinas.append(vacina)

    def saveDoacao(self, doacao):
        self.__doacoes.append(doacao)

    def saveAdocao(self, adocao):
        self.__adocoes.append(adocao)