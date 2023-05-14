from limite.tela_padrao import TelaPadrao

class TelaDoacao(TelaPadrao):
    def abreTela(self):
        print('\n'*100 + '--------------------DOAÇÃO--------------------')
        print('\n 1- Cadastrar uma nova Doação')
        print(' 2- Gerenciar os cadastros de Doações')
        print('\n'*2 + ' Digite X para retornar ao menu inicial.')
        print('--------------------------------------------')