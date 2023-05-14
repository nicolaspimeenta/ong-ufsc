from limite.tela_padrao import TelaPadrao

class TelaInicial(TelaPadrao):
    def abreTela(self):
        print('\n'*100 + '--------------------ONG--------------------')
        print('\n 1- Acessar menu dos Animais')
        print(' 2- Acessar menu das Pessoas')
        print(' 3- Acessar menu das Doações')
        print(' 4- Acessar menu das Adoções')
        print(' 5- Emitir Relatórios')
        print('\n'*2 + ' Feito por: Nicolas Lazzeri Pimenta')
        print('--------------------------------------------')