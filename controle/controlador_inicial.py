from limite.tela_inicial import TelaInicial
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_animal import ControladorAnimal
from controle.controlador_doacao import ControladorDoacao
from controle.controlador_adocao import ControladorAdocao
from controle.controlador_relatorio import ControladorRelatorio


class ControladorInicial:
    def __init__(self):
        self.controladorPessoa = ControladorPessoa()
        self.controladorAnimal = ControladorAnimal()
        self.controladorDoacao = ControladorDoacao()
        self.controladorAdocao = ControladorAdocao()
        self.controladorRelatorio = ControladorRelatorio()
        self.tela = TelaInicial()

    def iniciar(self):
        while True:
            escolha = int(self.tela.abreTela())
            if escolha == 0: break
            if escolha == 1: self.controladorAnimal.iniciar()
            if escolha == 2: self.controladorPessoa.iniciar()
            if escolha == 3: self.controladorDoacao.iniciar()
            if escolha == 4: self.controladorAdocao.iniciar()
            if escolha == 5: self.controladorRelatorio.iniciar()
