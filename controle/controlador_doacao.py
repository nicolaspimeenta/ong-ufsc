import pickle
import datetime
from entidade.doacao import Doacao
from limite.tela_doacao import TelaDoacao
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_animal import ControladorAnimal

class ControladorDoacao:
    def __init__(self):
        self.controladorPessoa = ControladorPessoa()
        self.controladorAnimal = ControladorAnimal()
        self.tela = TelaDoacao()
        self.dadosGlobais = None
    
    def iniciar(self):
        with open('dados.pkl', 'rb') as arquivo:
            self.dadosGlobais = pickle.load(arquivo)
        while True:
            escolha = int(self.tela.abreTela())
            if escolha == 0: return
            if escolha == 1: self.cadastrarDoacao()
            if escolha == 2: self.gerenciarDoacao()


    def cadastrarDoacao(self):
        valores = self.tela.cadastrarDoacao(self.dadosGlobais.pessoas, self.dadosGlobais.animais)
        if valores[0] == 'Retornar': return

        if valores[0] == 'Cadastrar a Pessoa': self.controladorPessoa.cadastrarPessoa(); return

        if valores[0] == 'Cadastrar o Animal': self.controladorAnimal.cadastrarAnimal(); return

        self.dadosGlobais.saveDoacao(Doacao(valores[0], valores[1], datetime.date(int(valores[3][2]), int(valores[3][1]), int(valores[3][0])), valores[2]))
        valores[1].dono = None
        valores[0].endereco.animais -= 1

        self.tela.salvarDados(self.dadosGlobais)

    def gerenciarDoacao(self):
        valores = self.tela.gerenciarDoacao(self.dadosGlobais.doacoes)
        if valores[0] == 'Retornar': return

        if valores[0] == 'Excluir':
            for key, value in valores[1].items():
                if value == True: 
                    doacaoExcluida = self.dadosGlobais.doacoes.pop(key)
                    doacaoExcluida.animal.dono = doacaoExcluida.pessoa
                    doacaoExcluida.pessoa.endereco.animais += 1

        if valores[0] == 'Alterar':
            for key, value in valores[1].items():
                if value == True: 
                    valores = self.tela.alterarDoacao(self.dadosGlobais.doacoes[key])
                    if valores[0] == 'Retornar': return

                    self.dadosGlobais.doacoes[key].data = datetime.date(int(valores[1]['ano']), int(valores[1]['mes']), int(valores[1]['dia']))
                    self.dadosGlobais.doacoes[key].motivo = valores[1]['motivo']

        self.tela.salvarDados(self.dadosGlobais)

