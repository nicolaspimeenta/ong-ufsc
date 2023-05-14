from limite.tela_padrao import TelaPadrao

class TelaAdocao(TelaPadrao):
    def abreTela(self):
        print('\n'*100 + '--------------------ADOÇÃO--------------------')
        print('\n 1- Cadastrar uma nova Adoção')
        print(' 2- Gerenciar os cadastros de Adoções')
        print('\n'*2 + ' Digite X para retornar ao menu inicial.')
        print('--------------------------------------------')