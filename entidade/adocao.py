from entidade.doaradotar import AbastractDoacaoAdocao

class Adocao(AbastractDoacaoAdocao):
    def __init__(self, pessoa: object, animal: object, data, assinatura: bool):
        super().__init__(pessoa, animal, data)
        self.__assinatura = assinatura

    @property
    def assinatura(self):
        return self.__assinatura
    
    @assinatura.setter
    def assinatura(self, assinatura):
        self.__assinatura = assinatura
