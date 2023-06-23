import PySimpleGUI as sg

class TelaRelatorio():
    def __init__(self):
        self.__window = None
        self.init_layout()

    def init_layout(self):
        sg.ChangeLookAndFeel('TanBlue')
        layout = [
        [sg.Text('Escolha a opção desejada', font=("Arial", 15))],
        [sg.Radio('Listar Vacinas Aplicadas', "RD1", key='1', font=('Arial', 10))],
        [sg.Radio('Listar Doações', "RD1", key='2', font=('Arial', 10))],
        [sg.Radio('Listar Adoções', "RD1", key='3', font=('Arial', 10))],
        [sg.Button('Confirmar', font=('Arial', 10)), sg.Cancel('Retornar', font=('Arial', 10))]
        ]
        self.__window = sg.Window('ONG - Adoção e Doação de Animais', layout, size=(400, 200), font=('Arial', 10))

    def abreTela(self):
        self.init_layout()
        valores = self.__window.Read()
        escolha = 0
        for key, value in valores[1].items():
            if value == True:
                escolha = key
        self.close()
        if valores[0] == 'Retornar': return 0
        return escolha

    def close(self):
        self.__window.Close()