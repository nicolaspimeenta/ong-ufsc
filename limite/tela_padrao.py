import datetime

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

    def validaData(self, podeSerHoje: bool):
        if podeSerHoje:
            while True:
                data = str(input('\n Digite S se a data desejada é hoje ou N se for outro dia: ')).capitalize()
                if data != 'S' and data != 'N' and data != 'X': print(' Valor inválido, por favor tente novamente')
                else: break
            if data == 'X': return
            if data == 'S': return datetime.date.today()
            if data == 'N': pass
            
        while True:
            try:
                dia = str(self.validaInput(min=1, max=31, msg='Digite o dia'))
                if dia == 'X': return dia

                mes = str(self.validaInput(min=1, max=12, msg='Digite o mês'))
                if mes == 'X': return mes

                while True:
                    try:
                        ano = str(input('\n Digite o ano: ')).capitalize()
                        if ano == 'X': return ano
                        if not ano.isdigit() or len(ano) != 4: raise ValueError
                    except Exception: print(' Valor inválido, por favor digite novamente')
                    else: break
                
                data = datetime.date(int(ano), int(mes), int(dia))

                if (data.month == 2 and data.day == 29) and not (data.isocalendar()[1] == 9): raise ValueError

                if data > datetime.date.today(): raise ValueError

                return data
            
            except Exception: print('\n Data inválida, por favor tente novamente ')
 