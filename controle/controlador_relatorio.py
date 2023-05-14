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
        if escolha == 1: dataMinima = datetime.date.today(); dataMaxima = datetime.date.today() - relativedelta(days=7)
        if escolha == 2: dataMinima = datetime.date.today(); dataMaxima = datetime.date.today() - relativedelta(months=1)
        if escolha == 3: dataMinima = datetime.date.today(); dataMaxima = datetime.date.today() - relativedelta(years=1)
        if escolha == 4:
            while True:
                try:
                    print('\n'*100 + '--------------------INTERVALO ESPECÍFICO--------------------')
                    print('\n Data Mínima: 00 / 00 / 0000')
                    print('\n'*2 + ' Digite X para cancelar a operação.')
                    print('------------------------------------------------------------')
                    dataMinima = self.tela.validaData(True)
                    if dataMinima == 'X': return

                    print('\n'*100 + '--------------------INTERVALO ESPECÍFICO--------------------')
                    print(f'\n Data Mínima: {dataMinima.strftime("%d")} / {dataMinima.strftime("%m")} / {dataMinima.strftime("%y")}')
                    print(' Data Máxima: 00 / 00 / 0000')
                    print('\n'*2 + ' Digite X para cancelar a operação.')
                    print('------------------------------------------------------------')
                    dataMaxima = self.tela.validaData(True)
                    if dataMaxima == 'X': return

                    if dataMinima < dataMaxima: raise ValueError
                    print('\n'*100 + '--------------------INTERVALO ESPECÍFICO--------------------')
                    print(f'\n Data Mínima: {dataMinima.strftime("%d")} / {dataMinima.strftime("%m")} / {dataMinima.strftime("%y")}')
                    print(f' Data Máxima: {dataMaxima.strftime("%d")} / {dataMaxima.strftime("%m")} / {dataMaxima.strftime("%y")}')
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
            dadosFiltrados = [dado for dado in dados if self.filtrarDatas( dataAtual=datetime.date( int(dado.data[2]), int(dado.data[1]), int(dado.data[0]) ), dataMaior=dataMinima, dataMenor=dataMaxima)]
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