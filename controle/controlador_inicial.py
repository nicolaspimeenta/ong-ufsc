from limite.tela_inicial import TelaInicial
from controlador_pessoa import ControladorPessoa

class ControladorInicial:
    def __init__(self):
        self.tela = TelaInicial(self)
        self.controladorPessoa = ControladorPessoa(self)

    def iniciar(self):
        while True:
            self.tela.abreTela()
            escolha = self.tela.validaInput(3)
            if escolha == 1: pass
            if escolha == 2: self.menuPessoa()
            if escolha == 3: pass
        

    def menuPessoa(self):
        self.ConstroladorPessoa.iniciar()
        return
