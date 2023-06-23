import copy
import datetime
from dateutil.relativedelta import relativedelta
from limite.tela_pessoa import TelaPessoa
from entidade.pessoa import Pessoa
from entidade.endereco import Endereco
from entidade import dadosGlobais

class ControladorPessoa:
    def __init__(self):
        self.tela = TelaPessoa()

    def iniciar(self):
        while True:
            escolha = int(self.tela.abreTela())
            if escolha == 0: return
            if escolha == 1: self.cadastrarPessoa()
            if escolha == 2: self.gerenciarPessoa()

    def cadastrarPessoa(self):
        dados = self.tela.cadastroPessoa()
        if dados[0] == 'Retornar': return

        dadosGlobais.saveEndereco(Endereco(dados[1]['cep'][:5] + '-' + dados[1]['cep'][5:9], dados[1]['numero'], dados[1]['tipo'], dados[1]['tamanho'], int(dados[1]['animais'])))
        dadosGlobais.savePessoa(Pessoa(dados[1]['cpf'][:3] + '.' + dados[1]['cpf'][3:6] + '.' + dados[1]['cpf'][6:9] + '-' + dados[1]['cpf'][9:11],
                                       dados[1]['nome'], datetime.date(int(dados[1]['ano']), int(dados[1]['mes']), int(dados[1]['dia'])), 
                                       dadosGlobais.enderecos[-1]))

    def gerenciarPessoa(self):
        dados = self.tela.gerenciarPessoa(dadosGlobais.pessoas)
        if dados[0] == 'Retornar': return

        if dados[0] == 'Excluir':
            for key, value in dados[1].items():
                if value == True: dadosGlobais.pessoas.pop(key)

        if dados[0] == 'Alterar':
            for key, value in dados[1].items():
                if value == True: 
                    dados = self.tela.alterarPessoa(dadosGlobais.pessoas[key])
                    if dados[0] == 'Retornar': return

                    dadosGlobais.pessoas[key].nome = dados[1]['nome']
                    dadosGlobais.pessoas[key].dataNascimento = datetime.date(int(dados[1]['ano']), int(dados[1]['mes']), int(dados[1]['dia']))
                    dadosGlobais.pessoas[key].endereco.cep = dados[1]['cep'][:5] + '-' + dados[1]['cep'][5:9]
                    dadosGlobais.pessoas[key].endereco.tipo = dados[1]['tipo']
                    dadosGlobais.pessoas[key].endereco.tamanho = dados[1]['tamanho']
                    dadosGlobais.pessoas[key].endereco.animais = int(dados[1]['animais'])

    def validaAdocao(self, pessoa, cachorroGrande):
        for doacao in dadosGlobais.doacoes:
            if pessoa == doacao.pessoa: return False
        if cachorroGrande and pessoa.endereco.tipo == 'Apartamento' and pessoa.endereco.tamanho == 'Pequeno': return False
        return True




        



                

        




