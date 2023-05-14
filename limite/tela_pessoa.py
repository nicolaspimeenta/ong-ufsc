from limite.tela_padrao import TelaPadrao

class TelaPessoa(TelaPadrao):
    def abreTela(self):
        print('\n'*100 + '--------------------PESSOAS--------------------')
        print('\n 1- Cadastrar uma nova Pessoa')
        print(' 2- Gerenciar os cadastros de Pessoas')
        print('\n'*2 + ' Digite X para retornar ao menu inicial.')
        print('--------------------------------------------')