import datetime
from limite.tela_relatorio import TelaRelatorio
from dateutil.relativedelta import relativedelta
from entidade import dadosGlobais

class ControladorRelatorio:
    def __init__(self):
        self.tela = TelaRelatorio()

    def iniciar(self):
        opcoes = []
        while True:
            self.tela.abreTela()
            print(f' {len(opcoes)} opção(ões) escolhida(s)')
            escolha = self.tela.validaInput(min=1, max=3)
            if escolha == 'X': return
            if escolha in opcoes: print(' Você já escolheu esta opção, por favor escolha outra.'); continue
            opcoes.append(escolha)
            if len(opcoes) == 3: break
            while True:
                escolha = str(input(' Digite S para escolher mais uma opção, digite * para selecionar todas ou N para finalizar a seleção: ')).capitalize()
                if escolha != 'S' and escolha != 'N' and escolha != 'X' and escolha != '*': print(' Valor inválido, por favor tente novamente')
                else: break
            if escolha == 'S': continue
            if escolha == 'N': break
            if escolha == 'X': return
            if escolha == '*': opcoes = [1, 2, 3]; break
        self.emitirRelatório(opcoes)

    def emitirRelatório(self, opcoes):
        dados = []
        if 1 in opcoes: dados.extend(dadosGlobais.vacinas)
        if 2 in opcoes: dados.extend(dadosGlobais.doacoes)
        if 3 in opcoes: dados.extend(dadosGlobais.adocoes)
        print('\n'*100 + '--------------------EMITIR RELATÓRIO--------------------')
        print('\n 1- Última semana')
        print(' 2- Último mês')
        print(' 3- Último ano')
        print(' 4- Intervalo específico')
        print(' 5- Sem restrição de data')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('--------------------------------------------')
        escolha = self.tela.validaInput(min=1, max=5, msg='Digite o número da restrição de data desejada no relatório')
        if escolha == 'X': return
        if escolha == 1: dataMinima = datetime.date.today(); dataMaxima = datetime.date.today() - datetime.timedelta(days=7)
        if escolha == 2: dataMinima = datetime.date.today(); dataMaxima = datetime.date.today() - relativedelta(months=1)
        if escolha == 3: dataMinima = datetime.date.today(); dataMaxima = datetime.date.today() - datetime.timedelta(days=365)
        if escolha == 4:
            while True:
                try:
                    print('\n'*100 + '--------------------INTERVALO ESPECÍFICO--------------------')
                    print('\n Data Mínima: 00 / 00 / 0000')
                    print(' Data Máxima: 00 / 00 / 0000')
                    print('\n'*2 + ' Digite X para cancelar a operação.')
                    print('------------------------------------------------------------')
                    while True:
                        data = str(input('\n Digite S se a data mínima desejada é hoje ou N se for em outro dia: ')).capitalize()
                        if data != 'S' and data != 'N' and data != 'X': print(' Valor inválido, por favor tente novamente')
                        else: break
                    if data == 'X': return
                    if data == 'S':
                        dia = datetime.date.today().day
                        if dia < 10: dia = '0' + str(dia)
                        dia = str(dia)

                        mes = datetime.date.today().month
                        if mes < 10: mes = '0' + str(mes)
                        mes = str(mes)

                        ano = str(datetime.date.today().year)
                        
                    if data == 'N':
                        print('\n'*100 + '--------------------DATA MÍNIMA--------------------')
                        print('\n 00 / 00 / 0000')
                        print('\n'*2 + ' Digite X para cancelar a operação.')
                        print('------------------------------------------------------------')
                        dia = str(self.tela.validaInput(min=1, max=31, msg='Digite o dia da data mínima'))
                        if dia == 'X': return dia
                        if len(dia) == 1: dia = "0" + dia

                        print('\n'*100 + '--------------------DATA MÍNIMA--------------------')
                        print(f'\n {dia} / 00 / 0000')
                        print('\n'*2 + ' Digite X para cancelar a operação.')
                        print('------------------------------------------------------------')
                        mes = str(self.tela.validaInput(min=1, max=12, msg='Digite o dia da data mínima'))
                        if mes == 'X': return mes
                        if len(mes) == 1: mes = "0" + mes

                        print('\n'*100 + '--------------------DATA MÍNIMA--------------------')
                        print(f'\n {dia} / {mes} / 0000')
                        print('\n'*2 + ' Digite X para cancelar a operação.')
                        print('------------------------------------------------------------')
                        while True:
                            try:
                                ano = str(input('\n Digite o ano data mínima: ')).capitalize()
                                if ano == 'X': return ano
                                if not ano.isdigit() or len(ano) != 4: raise ValueError
                            except Exception: print(' Valor inválido, por favor digite novamente')
                            else: break

                        print('\n'*100 + '--------------------DATA MÍNIMA--------------------')
                        print(f'\n {dia} / {mes} / {ano}')
                        print('\n'*2 + ' Digite X para cancelar a operação.')
                        print('------------------------------------------------------------')
                        
                        while True:
                            try:
                                confirma = str(input('\n Digite S para confirmar: ')).capitalize()
                                if confirma == 'X': return confirma
                                if confirma != 'S': raise ValueError
                            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
                            else: break
                        
                        data = datetime.date(int(ano), int(mes), int(dia))

                        if (int(mes) == 2 and int(dia) == 29) and not (data.isocalendar()[1] == 9): raise ValueError

                        if datetime.now().year < data.year or (datetime.now().year == data.year and datetime.now().month < data.month) or (datetime.now().year == data.year and datetime.now().month == data.month and datetime.now().day < data.day):
                            raise ValueError

                    dataMinima = [dia, mes, ano]

                    print('\n'*100 + '--------------------INTERVALO ESPECÍFICO--------------------')
                    print(f'\n Data Mínima: {dataMinima[0]} / {dataMinima[1]} / {dataMinima[2]}')
                    print(' Data Máxima: 00 / 00 / 0000')
                    print('\n'*2 + ' Digite X para cancelar a operação.')
                    print('------------------------------------------------------------')
                    while True:
                        data = str(input('\n Digite S se a data máxima desejada é hoje ou N se for em outro dia: ')).capitalize()
                        if data != 'S' and data != 'N' and data != 'X': print(' Valor inválido, por favor tente novamente')
                        else: break
                    if data == 'X': return
                    if data == 'S':
                        dia = datetime.date.today().day
                        if dia < 10: dia = '0' + str(dia)
                        dia = str(dia)

                        mes = datetime.date.today().month
                        if mes < 10: mes = '0' + str(mes)
                        mes = str(mes)

                        ano = str(datetime.date.today().year)
                        
                    if data == 'N':
                        print('\n'*100 + '--------------------DATA MÁXIMA--------------------')
                        print('\n 00 / 00 / 0000')
                        print('\n'*2 + ' Digite X para cancelar a operação.')
                        print('------------------------------------------------------------')
                        dia = str(self.tela.validaInput(min=1, max=31, msg='Digite o dia da data mínima'))
                        if dia == 'X': return dia
                        if len(dia) == 1: dia = "0" + dia

                        print('\n'*100 + '--------------------DATA MÁXIMA--------------------')
                        print(f'\n {dia} / 00 / 0000')
                        print('\n'*2 + ' Digite X para cancelar a operação.')
                        print('------------------------------------------------------------')
                        mes = str(self.tela.validaInput(min=1, max=12, msg='Digite o dia da data mínima'))
                        if mes == 'X': return mes
                        if len(mes) == 1: mes = "0" + mes

                        print('\n'*100 + '--------------------DATA MÁXIMA--------------------')
                        print(f'\n {dia} / {mes} / 0000')
                        print('\n'*2 + ' Digite X para cancelar a operação.')
                        print('------------------------------------------------------------')
                        while True:
                            try:
                                ano = str(input('\n Digite o ano data mínima: ')).capitalize()
                                if ano == 'X': return ano
                                if not ano.isdigit() or len(ano) != 4: raise ValueError
                            except Exception: print(' Valor inválido, por favor digite novamente')
                            else: break

                        print('\n'*100 + '--------------------DATA MÁXIMA--------------------')
                        print(f'\n {dia} / {mes} / {ano}')
                        print('\n'*2 + ' Digite X para cancelar a operação.')
                        print('------------------------------------------------------------')
                        while True:
                            try:
                                confirma = str(input('\n Digite S para confirmar: ')).capitalize()
                                if confirma == 'X': return confirma
                                if confirma != 'S': raise ValueError
                            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
                            else: break
                        
                        data = datetime.date(int(ano), int(mes), int(dia))

                        if (int(mes) == 2 and int(dia) == 29) and not (data.isocalendar()[1] == 9): raise ValueError

                        if datetime.now().year < data.year or (datetime.now().year == data.year and datetime.now().month < data.month) or (datetime.now().year == data.year and datetime.now().month == data.month and datetime.now().day < data.day):
                            raise ValueError

                    dataMaxima = [dia, mes, ano]

                    if datetime.date( int(dataMinima[2]), int(dataMinima[1]), int(dataMinima[0]) ) < datetime.date( int(dataMaxima[2]), int(dataMaxima[1]), int(dataMaxima[0]) ): 
                        raise ValueError

                    print('\n'*100 + '--------------------INTERVALO ESPECÍFICO--------------------')
                    print(f'\n Data Mínima: {dataMinima[0]} / {dataMinima[1]} / {dataMinima[2]}')
                    print(f' Data Máxima: {dataMaxima[0]} / {dataMaxima[1]} / {dataMaxima[2]}')
                    print('\n'*2 + ' Digite X para cancelar a operação.')
                    print('------------------------------------------------------------')
                    while True:
                        try:
                            confirma = str(input('\n Digite S para confirmar: ')).capitalize()
                            if confirma == 'X': return confirma
                            if confirma != 'S': raise ValueError
                        except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
                        else: break
                
                except Exception: input('\n Data inválida, por favor clique ENTER para tentar novamente ')
                else: break

        if escolha == 5: dados = sorted(dados, key=lambda obj: datetime.date( int(obj.data[2]), int(obj.data[1]), int(obj.data[0]) ))
        if escolha != 5:
            dadosFiltrados = [dado for dado in dados if self.filtrarDatas( dataAtual=datetime.date( int(dado.data[2]), int(dado.data[1]), int(dado.data[0]) ), dataMaior=datetime.date( int(dataMinima[2]), int(dataMinima[1]), int(dataMinima[0]) ), dataMenor=datetime.date( int(dataMaxima[2]), int(dataMaxima[1]), int(dataMaxima[0]) ))]
            dados = sorted(dadosFiltrados, key=lambda obj: datetime.date( int(obj.data[2]), int(obj.data[1]), int(obj.data[0]) ))
        
        print('\n'*100 + '--------------------RELATÓRIO--------------------')
        for dado in dados:
            if hasattr(dado, 'tipo'): print(f' {dado.data[0]}/{dado.data[1]}/{dado.data[2]} - Vacina "{dado.tipo}" foi aplicada em {dado.animal.nome} ({dado.animal.id})')
            if hasattr(dado, 'motivo'): print(f' {dado.data[0]}/{dado.data[1]}/{dado.data[2]} - {dado.pessoa.nome} ({dado.pessoa.cpf}) doou {dado.animal.nome} ({dado.animal.id})')
            if hasattr(dado, 'assinatura'): print(f' {dado.data[0]}/{dado.data[1]}/{dado.data[2]} - {dado.pessoa.nome} ({dado.pessoa.cpf}) adotou {dado.animal.nome} ({dado.animal.id})')
        print('--------------------------------------------')
        input(' Clique ENTER para retornar.')

    def filtrarDatas(self, dataAtual, dataMenor, dataMaior):
        if dataMenor <= dataAtual <= dataMaior : return True
        return False