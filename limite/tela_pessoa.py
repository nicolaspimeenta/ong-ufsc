from limite.tela_padrao import TelaPadrao

class TelaPessoa(TelaPadrao):
    def abreTela(self):
        print('\n'*100 + '''            --------------------PESSOAS--------------------

            1- Retornar
            2- Cadastrar uma nova Pessoa
            3- Listar/Alterar/Excluir os cadastros


            Feito por: Nicolas Lazzeri Pimenta
            --------------------------------------------''')