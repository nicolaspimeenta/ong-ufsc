from limite.tela_padrao import TelaPadrao

class TelaAnimal(TelaPadrao):
    def abreTela(self):
        print('\n'*100 + '--------------------ANIMAIS--------------------')
        print('\n 1- Gerenciar os cadastros de Animal')
        print(' 2- Registrar uma nova Vacina')
        print('\n'*2 + ' Digite X para retornar ao menu inicial.')
        print('--------------------------------------------')