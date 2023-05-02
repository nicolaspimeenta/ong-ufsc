from tela_padrao import TelaPadrao

campos = ''' --------------------ONG--------------------
1- Acessar menu dos Animais
2- Acessar menu das Pessoas
3- Acessar menu das Doações e Adoções


Feito por: Nicolas Lazzeri Pimenta
--------------------------------------------'''

class TelaInicial(TelaPadrao):
    def __init__(self, camposTela: str = campos):
        super().__init__(camposTela)