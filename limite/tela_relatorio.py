import datetime
import PySimpleGUI as sg
from limite.tela_padrao import TelaPadrao

class TelaRelatorio(TelaPadrao):
    def __init__(self):
        self.window = None
        self.init_layout()

    def init_layout(self):
        sg.ChangeLookAndFeel('TanBlue')
        layout = [
        [sg.Text('Escolha os dados desejados no relatório e a restrição de data', font=("Arial", 15))],
        [sg.Checkbox('Listar Vacinas Aplicadas', key='vacinas', font=('Arial', 10))],
        [sg.Checkbox('Listar Doações', key='doacoes', font=('Arial', 10))],
        [sg.Checkbox('Listar Adoções', key='adocoes', font=('Arial', 10))],
        [sg.Button('Última semana', font=('Arial', 10)), sg.Button('Último mês', font=('Arial', 10)), sg.Button('Último ano', font=('Arial', 10)), sg.Button('Intervalo específico', font=('Arial', 10)), sg.Button('Sem restrição de data', font=('Arial', 10)), sg.Cancel('Retornar', font=('Arial', 10))]
        ]
        self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

    def abreTela(self):
        while True:
            self.init_layout()
            valores = self.window.read()

            if valores[0] == 'Retornar': 
                self.window.close()
                return valores

            if not valores[1]['vacinas'] and not valores[1]['doacoes'] and not valores[1]['adocoes']:
                sg.popup('ERRO', 'Selecione pelo menos uma opção')
                self.window.close()
                continue

            self.window.close()
            return valores
        
    def escolherIntervalo(self):
        while True:
            sg.ChangeLookAndFeel('TanBlue')
            layout = [
            [sg.Text('Escolha a data mínima e máxima desejada', font=("Arial", 15))],
            [sg.Text('Data mínima', size=(20, 1)), sg.InputText(key='diaMin', size=(5, 1)), sg.Text('/'), sg.InputText(key='mesMin', size=(5, 1)), sg.Text('/'), sg.InputText(key='anoMin', size=(5, 1))],
            [sg.Text('Data máxima', size=(20, 1)), sg.InputText(key='diaMax', size=(5, 1)), sg.Text('/'), sg.InputText(key='mesMax', size=(5, 1)), sg.Text('/'), sg.InputText(key='anoMax', size=(5, 1))],
            [sg.Button('Confirmar', font=('Arial', 10)), sg.Cancel('Retornar', font=('Arial', 10))]
            ]
            self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

            valores = self.window.read()

            if valores[0] == 'Retornar': 
                self.window.close()
                return valores

            if valores[0] == 'Confirmar':
                erro = False
                for key, value in valores[1].items():
                    if value == '':
                        sg.popup('ERRO', f'O campo {key} é obrigatório')
                        self.window.close()
                        erro = True
                        break
                if erro: continue

            if not super().validaData(valores[1]['diaMin'], valores[1]['mesMin'], valores[1]['anoMin']):
                sg.popup('ERRO', 'Digite uma data mínima válida')
                self.window.close()
                continue

            if not super().validaData(valores[1]['diaMax'], valores[1]['mesMax'], valores[1]['anoMax']):
                sg.popup('ERRO', 'Digite uma data máxima válida')
                self.window.close()
                continue

            if datetime.date(int(valores[1]['anoMin']), int(valores[1]['mesMin']), int(valores[1]['diaMin'])) > datetime.date(int(valores[1]['anoMax']), int(valores[1]['mesMax']), int(valores[1]['diaMax'])):
                sg.popup('ERRO', 'A data mínima não pode ser maior que a máxima')
                self.window.close()
                continue

            self.window.close()
            return valores
        
    def mostrarRelatorio(self, dados):
        sg.ChangeLookAndFeel('TanBlue')
        layout = []
        if len(dados) == 0: layout.append([sg.Text('')])
        
        for dado in dados:
            if hasattr(dado, 'tipo'): layout.append([sg.Text(f' {dado.data.strftime("%d")}/{dado.data.strftime("%m")}/{dado.data.strftime("%Y")} - Vacina "{dado.tipo}" foi aplicada em {dado.animal.nome} ({dado.animal.id})')])
            if hasattr(dado, 'motivo'): layout.append([sg.Text(f' {dado.data.strftime("%d")}/{dado.data.strftime("%m")}/{dado.data.strftime("%Y")} - {dado.pessoa.nome} ({dado.pessoa.cpf}) doou {dado.animal.nome} ({dado.animal.id})')])
            if hasattr(dado, 'assinatura'): layout.append([sg.Text(f' {dado.data.strftime("%d")}/{dado.data.strftime("%m")}/{dado.data.strftime("%Y")} - {dado.pessoa.nome} ({dado.pessoa.cpf}) adotou {dado.animal.nome} ({dado.animal.id})')])
        
        layout.append([sg.Cancel('Retornar', font=('Arial', 10))])

        self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

        valores = self.window.read()

        if valores[0] == 'Retornar': 
            self.window.close()
            return
