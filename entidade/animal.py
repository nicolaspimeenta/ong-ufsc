class Animal:
    def __init__(self, id: int, tipo: str, nome: str, raca: str, dono: object):
        self.__id = id
        self.__tipo = tipo
        self.__nome = nome
        self.__raca = raca
        self.__dono = dono
        self.__vacinas = []

    @property
    def id(self):
        return self.__id
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.__raca
    
    @property
    def vacinas(self):
        return self.__vacinas
    
    @property
    def dono(self):
        return self.__dono
    
    @id.setter
    def id(self, id):
        self.__id = id

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @raca.setter
    def raca(self, raca):
        self.__raca = raca

    @dono.setter
    def dono(self, dono):
        self.__dono = dono

    def addVacina(self, vacina):
        self.__vacinas.append(vacina)