import PySimpleGUI as sg

class TelaInicial():
    def __init__(self):
        self.window = None
        self.init_layout()

    def init_layout(self):
        sg.ChangeLookAndFeel('TanBlue')
        layout = [
        [sg.Text('Escolha o menu que deseja acessar', font=("Arial", 15))],
        [sg.Radio('Animais', "RD1", key='1', font=('Arial', 10))],
        [sg.Radio('Pessoas', "RD1", key='2', font=('Arial', 10))],
        [sg.Radio('Doações', "RD1", key='3', font=('Arial', 10))],
        [sg.Radio('Adoções', "RD1", key='4', font=('Arial', 10))],
        [sg.Radio('Relatórios', "RD1", key='5', font=('Arial', 10))],
        [sg.Button('Confirmar', font=('Arial', 10)), sg.Cancel('Sair', font=('Arial', 10))]
        ]
        self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

    def abreTela(self):
        self.init_layout()
        valores = self.window.Read()
        escolha = 0
        if valores[0] == 'Confirmar':
            for key, value in valores[1].items():
                if value == True:
                    escolha = key
        self.window.Close()
        return escolha