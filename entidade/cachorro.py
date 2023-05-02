from entidade.animal import Animal

class Cachorro(Animal):
    def __init__(self, id: int, nome: str, raca: str, vacinas, dono: object, tamanho: str):
        super().__init__(id, nome, raca, vacinas, dono)
        self.__tamanho = tamanho

    @property
    def tamanho(self):
        return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho