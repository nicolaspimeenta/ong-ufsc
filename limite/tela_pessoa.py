from limite.tela_padrao import TelaPadrao

class TelaPessoa(TelaPadrao):
    def abreTela(self):
        print('\n'*100 + '--------------------PESSOAS--------------------')
        print('\n 1- Retornar')
        print(' 2- Cadastrar uma nova Pessoa')
        print(' 3- Listar/Alterar/Excluir os cadastros')
        print('\n'*2 + ' Feito por: Nicolas Lazzeri Pimenta')
        print('--------------------------------------------')