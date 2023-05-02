from limite.tela_inicial import TelaInicial
from controle.controlador_pessoa import ControladorPessoa

class ControladorInicial:
    def __init__(self):
        self.__tela = TelaInicial()
        self.__controladorPessoa = ControladorPessoa()

    @property
    def tela(self):
        return self.__tela
    
    @property
    def controladorPessoa(self):
        return self.__controladorPessoa

    def iniciar(self):
        while True:
            self.tela.abreTela()
            escolha = self.tela.validaInput(3)
            if escolha == 1: pass
            if escolha == 2: self.menuPessoa()
            if escolha == 3: pass
        

    def menuPessoa(self):
        self.controladorPessoa.iniciar()
        return
