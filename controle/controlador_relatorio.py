import pickle
import datetime
from limite.tela_relatorio import TelaRelatorio
from dateutil.relativedelta import relativedelta

class ControladorRelatorio:
    def __init__(self):
        self.tela = TelaRelatorio()
        self.dadosGlobais = None

    def iniciar(self):
        with open('dados.pkl', 'rb') as arquivo:
            self.dadosGlobais = pickle.load(arquivo)
        dadosEscolhidos = []
        valores = self.tela.abreTela()

        if valores[0] == 'Retornar': return

        if valores[1]['vacinas']: dadosEscolhidos.append('vacinas')
        if valores[1]['doacoes']: dadosEscolhidos.append('doacoes')
        if valores[1]['adocoes']: dadosEscolhidos.append('adocoes')

        self.emitirRelatório(dadosEscolhidos, valores[0])

    def emitirRelatório(self, dadosEscolhidos, restricaoData):
        dados = []
        if 'vacinas' in dadosEscolhidos: dados.extend(self.dadosGlobais.vacinas)
        if 'doacoes' in dadosEscolhidos: dados.extend(self.dadosGlobais.doacoes)
        if 'adocoes' in dadosEscolhidos: dados.extend(self.dadosGlobais.adocoes)

        if restricaoData == 'Última semana': dataMaxima = datetime.date.today(); dataMinima = datetime.date.today() - relativedelta(days=7)
        if restricaoData == 'Último mês': dataMaxima = datetime.date.today(); dataMinima = datetime.date.today() - relativedelta(months=1)
        if restricaoData == 'Último ano': dataMaxima = datetime.date.today(); dataMinima = datetime.date.today() - relativedelta(years=1)
        if restricaoData == 'Intervalo específico':
            valores = self.tela.escolherIntervalo()

            dataMinima = datetime.date(int(valores[1]['anoMin']), int(valores[1]['mesMin']), int(valores[1]['diaMin']))
            dataMaxima = datetime.date(int(valores[1]['anoMax']), int(valores[1]['mesMax']), int(valores[1]['diaMax']))

        if restricaoData == 'Sem restrição de data': dados = sorted(dados, key=lambda obj: obj.data)
        if restricaoData != 'Sem restrição de data':
            dadosFiltrados = [dado for dado in dados if self.filtrarDatas(data=dado.data, dataMaior=dataMaxima, dataMenor=dataMinima)]
            dados = sorted(dadosFiltrados, key=lambda obj: obj.data)
        
        self.tela.mostrarRelatorio(dados)

    def filtrarDatas(self, data, dataMenor, dataMaior):
        if dataMenor <= data <= dataMaior : return True
        return False