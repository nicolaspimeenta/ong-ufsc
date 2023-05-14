class TelaPadrao:
    def validaInput(self, max, msg = 'Digite o número da opção desejada', min = 0):
        while True:
            try:
                escolha = input(f'\n {msg}: ').capitalize()
                if escolha == 'X': return escolha
                escolha = int(escolha)
                if escolha < min or escolha > max: raise ValueError
            except Exception:
                print(f' Valor Inválido, por favor digite um número entre {min} e {max}')
            else: return escolha
 