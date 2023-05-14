class Vacina:
    def __init__(self, tipo: str, data: object, animal: object):
        self.__tipo = tipo
        self.__data = data
        self.__animal = animal

    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def data(self):
        return self.__data
    
    @property
    def animal(self):
        return self.__animal
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @data.setter
    def data(self, data):
        self.__data = data

    @animal.setter
    def animal(self, animal):
        self.__animal = animal