from limite.tela_doacao import TelaDoacao
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_animal import ControladorAnimal
from entidade.doacao import Doacao
from entidade import dadosGlobais
import datetime

class ControladorDoacao:
    def __init__(self):
        self.controladorPessoa = ControladorPessoa()
        self.controladorAnimal = ControladorAnimal()
        self.tela = TelaDoacao()
    
    def iniciar(self):
        while True:
            escolha = int(self.tela.abreTela())
            if escolha == 0: return
            if escolha == 1: self.cadastrarDoacao()
            if escolha == 2: self.gerenciarDoacao()


    def cadastrarDoacao(self):
        valores = self.tela.cadastrarDoacao(dadosGlobais.pessoas, dadosGlobais.animais)
        if valores[0] == 'Retornar': return

        if valores[0] == 'Cadastrar a Pessoa': self.controladorPessoa.cadastrarPessoa(); return

        if valores[0] == 'Cadastrar o Animal': self.controladorAnimal.cadastrarAnimal(); return

        dadosGlobais.saveDoacao(Doacao(valores[0], valores[1], datetime.date(int(valores[3][2]), int(valores[3][1]), int(valores[3][0])), valores[2]))
        valores[1].dono = None
        valores[0].endereco.animais -= 1

    def gerenciarDoacao(self):
        valores = self.tela.gerenciarDoacao(dadosGlobais.doacoes)
        if valores[0] == 'Retornar': return

        if valores[0] == 'Excluir':
            for key, value in valores[1].items():
                if value == True: 
                    doacaoExcluida = dadosGlobais.doacoes.pop(key)
                    doacaoExcluida.animal.dono = doacaoExcluida.pessoa
                    doacaoExcluida.pessoa.endereco.animais += 1

        if valores[0] == 'Alterar':
            for key, value in valores[1].items():
                if value == True: 
                    valores = self.tela.alterarDoacao(dadosGlobais.doacoes[key])
                    if valores[0] == 'Retornar': return

                    dadosGlobais.doacao[key].data = datetime.date(int(valores[1]['ano']), int(valores[1]['mes']), int(valores[1]['dia']))
                    dadosGlobais.animais[key].motivo = valores[1]['motivo']
