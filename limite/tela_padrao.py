class TelaPadrao:
    def __init__(self, camposTela: str):
        self.camposTela = camposTela

    def abreTela(self):
        print(self.camposTela)

    def validaInput(self, max):
        while True:
            try:
                escolha = int(input('Digite o número da opção desejada: '))
                if escolha < 0 or escolha > max: raise ValueError 
            except Exception:
                print(f'Valor Inválido, por favor digite um número entre 0 e {max}')
            else:
                return escolha
 