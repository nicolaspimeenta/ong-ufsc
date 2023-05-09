from limite.tela_padrao import TelaPadrao

class TelaAnimal(TelaPadrao):
    def abreTela(self):
        print('\n'*100 + '--------------------ANIMAIS--------------------')
        print('\n 1- Retornar')
        print(' 2- Cadastrar um novo Animal')
        print(' 3- Gerenciar os cadastros de Animal')
        print(' 4- Registrar Vacina(s)')
        print(' 5- Gerenciar os cadastros de Vacina')
        print('\n'*2 + ' Feito por: Nicolas Lazzeri Pimenta')
        print('--------------------------------------------')