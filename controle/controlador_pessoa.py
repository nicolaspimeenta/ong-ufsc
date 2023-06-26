import pickle
import datetime
from entidade.pessoa import Pessoa
from entidade.endereco import Endereco
from limite.tela_pessoa import TelaPessoa

class ControladorPessoa:
    def __init__(self):
        self.tela = TelaPessoa()
        self.dadosGlobais = None

    def iniciar(self):
        with open('dados.pkl', 'rb') as arquivo:
            self.dadosGlobais = pickle.load(arquivo)
        while True:
            escolha = int(self.tela.abreTela())
            if escolha == 0: return
            if escolha == 1: self.cadastrarPessoa()
            if escolha == 2: self.gerenciarPessoa()

    def cadastrarPessoa(self):
        valores = self.tela.cadastroPessoa()
        if valores[0] == 'Retornar': return

        if valores[1]['cpf'] != '12345678900':
            for pessoa in self.dadosGlobais.pessoas:
                if pessoa.cpf == valores[1]['cpf'][:3] + '.' + valores[1]['cpf'][3:6] + '.' + valores[1]['cpf'][6:9] + '-' + valores[1]['cpf'][9:11]: self.tela.pessoaRepetida(); return

        self.dadosGlobais.saveEndereco(Endereco(valores[1]['cep'][:5] + '-' + valores[1]['cep'][5:9], valores[1]['numero'], valores[1]['tipo'], valores[1]['tamanho'], int(valores[1]['animais'])))
        self.dadosGlobais.savePessoa(Pessoa(valores[1]['cpf'][:3] + '.' + valores[1]['cpf'][3:6] + '.' + valores[1]['cpf'][6:9] + '-' + valores[1]['cpf'][9:11],
                                       valores[1]['nome'], datetime.date(int(valores[1]['ano']), int(valores[1]['mes']), int(valores[1]['dia'])), 
                                       self.dadosGlobais.enderecos[-1]))
        
        self.tela.salvarDados(self.dadosGlobais)

    def gerenciarPessoa(self):
        valores = self.tela.gerenciarPessoa(self.dadosGlobais.pessoas)
        if valores[0] == 'Retornar': return

        if valores[0] == 'Excluir':
            for key, value in valores[1].items():
                if value == True: self.dadosGlobais.pessoas.pop(key)

        if valores[0] == 'Alterar':
            for key, value in valores[1].items():
                if value == True: 
                    valores = self.tela.alterarPessoa(self.dadosGlobais.pessoas[key])
                    if valores[0] == 'Retornar': return

                    self.dadosGlobais.pessoas[key].nome = valores[1]['nome']
                    self.dadosGlobais.pessoas[key].dataNascimento = datetime.date(int(valores[1]['ano']), int(valores[1]['mes']), int(valores[1]['dia']))
                    self.dadosGlobais.pessoas[key].endereco.cep = valores[1]['cep'][:5] + '-' + valores[1]['cep'][5:9]
                    self.dadosGlobais.pessoas[key].endereco.tipo = valores[1]['tipo']
                    self.dadosGlobais.pessoas[key].endereco.tamanho = valores[1]['tamanho']
                    self.dadosGlobais.pessoas[key].endereco.animais = int(valores[1]['animais'])

        self.tela.salvarDados(self.dadosGlobais)
        




        



                

        




