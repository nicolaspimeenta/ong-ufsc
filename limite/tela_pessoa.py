from tela_padrao import TelaPadrao

campos = '''--------------------PESSOAS--------------------
 0- Retornar
 1- Cadastrar uma nova Pessoa
 2- Listar/Alterar/Excluir os cadastros


 Feito por: Nicolas Lazzeri Pimenta
--------------------------------------------'''

class TelaPessoa(TelaPadrao):
    def __init__(self, camposTela: str = campos):
        super().__init__(camposTela)