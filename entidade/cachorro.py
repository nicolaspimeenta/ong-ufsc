from entidade.animal import Animal

class Cachorro(Animal):
    def __init__(self, id: int, tipo: str, nome: str, raca: str, dono: object, tamanho: str):
        super().__init__(id, tipo, nome, raca, dono)
        self.__tamanho = tamanho

    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho