from limite.tela_padrao import TelaPadrao

class TelaRelatorio(TelaPadrao):
    def abreTela(self):
        print('\n'*100 + '--------------------EMITIR RELATÓRIO--------------------')
        print('\n 1- Listar Vacinas Aplicadas')
        print(' 2- Listar Doações')
        print(' 3- Listar Adoções')
        print('\n'*2 + ' Digite X para retornar ao menu inicial.')
        print('--------------------------------------------')