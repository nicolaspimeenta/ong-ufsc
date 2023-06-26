import pickle
import datetime
from entidade.adocao import Adocao
from limite.tela_adocao import TelaAdocao
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_animal import ControladorAnimal

class ControladorAdocao:
    def __init__(self):
        self.controladorPessoa = ControladorPessoa()
        self.controladorAnimal = ControladorAnimal()
        self.tela = TelaAdocao()
        self.dadosGlobais = None
    
    def iniciar(self):
        with open('dados.pkl', 'rb') as arquivo:
            self.dadosGlobais = pickle.load(arquivo)
        while True:
            escolha = int(self.tela.abreTela())
            if escolha == 0: return
            if escolha == 1: self.cadastrarAdocao()
            if escolha == 2: self.gerenciarAdocao()


    def cadastrarAdocao(self):
        doadores = []
        vacinados = []
        for doacao in self.dadosGlobais.doacoes: doadores.append(doacao.pessoa.cpf)

        for animal in self.dadosGlobais.animais:
            vacinas = []
            for vacina in animal.vacinas:
                if vacina.tipo.lower() == 'raiva' or vacina.tipo.lower() == 'leptospirose' or vacina.tipo.lower() == 'hepatite infecciosa':
                    vacinas.append(vacina.tipo.lower())

            if 'raiva' in vacinas and 'leptospirose' in vacinas and 'hepatite infecciosa' in vacinas: vacinados.append(animal.id)

        valores = self.tela.cadastrarAdocao(self.dadosGlobais.pessoas, self.dadosGlobais.animais, doadores, vacinados)
        if valores[0] == 'Retornar': return

        if valores[0] == 'Cadastrar o Animal': self.controladorAnimal.cadastrarAnimal(); return

        if valores[0] == 'Cadastrar a Pessoa': self.controladorPessoa.cadastrarPessoa(); return

        valores[0].endereco.animais += 1
        valores[1].dono = valores[0]
        self.dadosGlobais.saveAdocao(Adocao(valores[0], valores[1], datetime.date(int(valores[3][2]), int(valores[3][1]), int(valores[3][0])), valores[2]))

        self.tela.salvarDados(self.dadosGlobais)


    def gerenciarAdocao(self):
        valores = self.tela.gerenciarAdocao(self.dadosGlobais.adocoes)
        if valores[0] == 'Retornar': return

        if valores[0] == 'Excluir':
            for key, value in valores[1].items():
                if value == True: 
                    doacaoExcluida = self.dadosGlobais.adocoes.pop(key)
                    doacaoExcluida.animal.dono = None
                    doacaoExcluida.pessoa.endereco.animais -= 1

        if valores[0] == 'Alterar':
            for key, value in valores[1].items():
                if value == True: 
                    valores = self.tela.alterarAdocao(self.dadosGlobais.adocoes[key])
                    if valores[0] == 'Retornar': return

                    self.dadosGlobais.adocoes[key].data = datetime.date(int(valores[1]['ano']), int(valores[1]['mes']), int(valores[1]['dia']))
                    self.dadosGlobais.adocoes[key].motivo = valores[1]['motivo']