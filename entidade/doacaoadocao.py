from abc import ABC

class AbastractDoacaoAdocao(ABC):
    def __init__(self, pessoa: object, animal: object, data):
        self.__pessoa = pessoa
        self.__animal = animal
        self.__data = data

    @property
    def pessoa(self):
        return self.__pessoa
    
    @property
    def data(self):
        return self.__data
    
    @property
    def animal(self):
        return self.__animal
    
    @pessoa.setter
    def pessoa(self, pessoa):
        self.__pessoa = pessoa

    @data.setter
    def data(self, data):
        self.__data = data

    @animal.setter
    def animal(self, animal):
        self.__animal = animal