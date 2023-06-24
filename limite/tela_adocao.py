import PySimpleGUI as sg

class TelaAdocao():
    def __init__(self):
        self.window = None
        self.init_layout()

    def init_layout(self):
        sg.ChangeLookAndFeel('TanBlue')
        layout = [
        [sg.Text('Escolha a opção desejada', font=("Arial", 15))],
        [sg.Radio('Cadastrar uma nova Adoção', "RD1", key='1', font=('Arial', 10))],
        [sg.Radio('Gerenciar os cadastros de Adoções', "RD1", key='2', font=('Arial', 10))],
        [sg.Button('Confirmar', font=('Arial', 10)), sg.Cancel('Retornar', font=('Arial', 10))]
        ]
        self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

    def abreTela(self):
        self.init_layout()
        valores = self.window.read()
        escolha = 0
        for key, value in valores[1].items():
            if value == True:
                escolha = key
        self.window.close()
        if valores[0] == 'Retornar': return 0
        return escolha