from entidade.doacaoadocao import AbastractDoacaoAdocao

class Doacao(AbastractDoacaoAdocao):
    def __init__(self, pessoa: object, animal: object, data, motivo: str):
        super().__init__(pessoa, animal, data)
        self.__motivo = motivo

    @property
    def motivo(self):
        return self.__motivo
    
    @motivo.setter
    def motivo(self, motivo):
        self.__motivo = motivo
