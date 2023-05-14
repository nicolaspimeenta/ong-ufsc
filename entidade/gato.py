from entidade.animal import Animal

class Gato(Animal):
    def __init__(self, id: int, tipo: str, nome: str, raca: str, dono: object):
        super().__init__(id, tipo, nome, raca, dono)