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
        valores = self.tela.cadastroPessoa()
        if valores[0] == 'Retornar': return

        if valores[1]['cpf'] != '12345678900':
            for pessoa in dadosGlobais.pessoas:
                if pessoa.cpf == valores[1]['cpf'][:3] + '.' + valores[1]['cpf'][3:6] + '.' + valores[1]['cpf'][6:9] + '-' + valores[1]['cpf'][9:11]: self.tela.pessoaRepetida(); return

        dadosGlobais.saveEndereco(Endereco(valores[1]['cep'][:5] + '-' + valores[1]['cep'][5:9], valores[1]['numero'], valores[1]['tipo'], valores[1]['tamanho'], int(valores[1]['animais'])))
        dadosGlobais.savePessoa(Pessoa(valores[1]['cpf'][:3] + '.' + valores[1]['cpf'][3:6] + '.' + valores[1]['cpf'][6:9] + '-' + valores[1]['cpf'][9:11],
                                       valores[1]['nome'], datetime.date(int(valores[1]['ano']), int(valores[1]['mes']), int(valores[1]['dia'])), 
                                       dadosGlobais.enderecos[-1]))

    def gerenciarPessoa(self):
        valores = self.tela.gerenciarPessoa(dadosGlobais.pessoas)
        if valores[0] == 'Retornar': return

        if valores[0] == 'Excluir':
            for key, value in valores[1].items():
                if value == True: dadosGlobais.pessoas.pop(key)

        if valores[0] == 'Alterar':
            for key, value in valores[1].items():
                if value == True: 
                    valores = self.tela.alterarPessoa(dadosGlobais.pessoas[key])
                    if valores[0] == 'Retornar': return

                    dadosGlobais.pessoas[key].nome = valores[1]['nome']
                    dadosGlobais.pessoas[key].dataNascimento = datetime.date(int(valores[1]['ano']), int(valores[1]['mes']), int(valores[1]['dia']))
                    dadosGlobais.pessoas[key].endereco.cep = valores[1]['cep'][:5] + '-' + valores[1]['cep'][5:9]
                    dadosGlobais.pessoas[key].endereco.tipo = valores[1]['tipo']
                    dadosGlobais.pessoas[key].endereco.tamanho = valores[1]['tamanho']
                    dadosGlobais.pessoas[key].endereco.animais = int(valores[1]['animais'])

    def validaAdocao(self, pessoa, cachorroGrande):
        for doacao in dadosGlobais.doacoes:
            if pessoa == doacao.pessoa: return False
        if cachorroGrande and pessoa.endereco.tipo == 'Apartamento' and pessoa.endereco.tamanho == 'Pequeno': return False
        return True




        



                

        




