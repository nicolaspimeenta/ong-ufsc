class TelaPadrao:
    def validaInput(self, max):
        while True:
            try:
                escolha = int(input('\n Digite o número da opção desejada: \n'))
                if escolha < 0 or escolha > max: raise ValueError 
            except Exception:
                print(f' Valor Inválido, por favor digite um número entre 0 e {max}')
            else:
                return escolha
 