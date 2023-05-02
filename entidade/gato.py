from animal import Animal

class Gato(Animal):
    def __init__(self, id: int, nome: str, raca: str, vacinas, dono):
        super().__init__(id, nome, raca, vacinas, dono)