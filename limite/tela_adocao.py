import PySimpleGUI as sg
import datetime

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

    def cadastrarDoacao(self, pessoas, animais):
        adotante = ''
        animal = ''
        data = ''
        assinatura = False

        while True:
            layout = [
                [sg.Text('Lista de Animais Cadastrados:', font=('Arial', 12, 'bold'))],
                [sg.Text('Selecione o animal que está sendo adotado', font=('Arial', 10))],
            ]
            if len(animais) == 0:
                layout.append([sg.Text('Não há nenhum animal cadastrado', font=('Arial', 10, 'bold'))])
            else:
                for animal in animais:
                    layout.append([sg.Radio(f' {animal.nome} | ID: {animal.id}', 'RADIO1')])

            layout.append([sg.Button('Confirmar', font=('Arial', 10)), sg.Button('Cadastrar o Animal', font=('Arial', 10), button_color='#27AE60'), sg.Cancel('Retornar', font=('Arial', 10))])
            self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

            valores = self.window.read()

            if valores[0] == 'Confirmar':
                for key, value in valores[1].items():
                    if value == True:
                        self.window.close()
                        animal = animais[key]

                if animal: break

                sg.popup('ERRO', 'Selecione algum animal ou cadastre um novo')
                self.window.close()
                continue

            else: 
                self.window.close()
                return valores
            
        self.window.close()

        while True:
            layout = [
                [sg.Text('Lista de Pessoas Cadastradas:', font=('Arial', 12, 'bold'))],
                [sg.Text('Selecione a pessoa que está adotando', font=('Arial', 10))],
            ]
            if len(pessoas) == 0:
                layout.append([sg.Text('Não há nenhuma pessoa cadastrada', font=('Arial', 10, 'bold'))])
            else:
                for pessoa in pessoas:
                    layout.append([sg.Radio(f' {pessoa.nome} | {pessoa.cpf}', 'RADIO1')])

            layout.append([sg.Button('Confirmar', font=('Arial', 10)), sg.Button('Cadastrar a Pessoa', font=('Arial', 10), button_color='#27AE60'), sg.Cancel('Retornar', font=('Arial', 10))])
            self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

            valores = self.window.read()

            if valores[0] == 'Confirmar':
                for key, value in valores[1].items():
                    if value == True:
                        self.window.close()
                        doador = pessoas[key]

                if doador: break

                sg.popup('ERRO', 'Selecione alguma pessoa ou cadastre uma nova')
                self.window.close()
                continue

            else: 
                self.window.close()
                return valores

        self.window.close()
        
        while True:
            layout = [
            [sg.Text(f'Dados Gerais:', font=('Arial', 12, 'bold'))],
            [sg.Text('Motivo da Doação', size=(20, 1)), sg.InputText(key='motivo')],
            [sg.Text('Data da Doação', size=(20, 1)), sg.InputText(f'{datetime.date.today().strftime("%d")}', key='dia', size=(5, 1)), sg.Text('/'), sg.InputText(f'{datetime.date.today().strftime("%m")}', key='mes', size=(5, 1)), sg.Text('/'), sg.InputText(f'{datetime.date.today().strftime("%Y")}', key='ano', size=(5, 1))],
            [sg.Button('Confirmar', font=('Arial', 10)), sg.Cancel('Retornar', font=('Arial', 10))]
            ]
            self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

            valores = self.window.read()

            if valores[0] == 'Retornar':
                self.window.close()
                return valores

            if not super().validaData(valores[1]['dia'], valores[1]['mes'], valores[1]['ano']):
                sg.popup('ERRO', 'Digite uma Data válida')
                self.window.close()
                continue

            if valores[0] == 'Confirmar':
                erro = False
                for key, value in valores[1].items():
                    if value == '':
                        sg.popup('ERRO', f'O campo {key} é obrigatório')
                        self.window.close()
                        erro = True
                        break
                if erro: continue

            self.window.close()
            motivo = valores[1]['motivo']
            data = [valores[1]['dia'], valores[1]['mes'], valores[1]['ano']]
            break

        return [doador, animal, motivo, data]
    
    def gerenciarDoacao(self, doacoes):
        while True:
            layout = [
                [sg.Text('Lista de DoaçÕes Cadastrados:', font=('Arial', 12, 'bold'))],
                [sg.Text('Selecione uma para exclui-la ou altera-la', font=('Arial', 10))],
            ]
            if len(doacoes) == 0:
                layout.append([sg.Text('Não há nenhuma doação cadastrada', font=('Arial', 10, 'bold'))])
            else:
                for doacao in doacoes:
                    layout.append([sg.Radio(f'{doacao.data.strftime("%d")}/{doacao.data.strftime("%m")}/{doacao.data.strftime("%Y")} {doacao.pessoa.nome} doou o {doacao.animal.tipo} {doacao.animal.nome} (ID: {doacao.animal.id})', 'RADIO1')])

            layout.append([sg.Button('Alterar', font=('Arial', 10)), sg.Button('Excluir', font=('Arial', 10), button_color='#B22222'), sg.Cancel('Retornar', font=('Arial', 10))])
            self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

            valores = self.window.read()

            if valores[0] == 'Excluir' or valores[0] == 'Alterar':
                for key, value in valores[1].items():
                    if value == True:
                        self.window.close()
                        return valores
                sg.popup('ERRO', 'Selecione uma doação para altera-la ou exclui-la')
                continue

            self.window.close()
            return valores
        
    def alterarDoacao(self, doacao):
        while True:
            layout = [
            [sg.Text('Dados Gerais:', font=('Arial', 12, 'bold'))],
            [sg.Text('Doador', size=(20, 1)), sg.InputText(f'{doacao.pessoa.nome} | {doacao.pessoa.cpf}', key='pessoa', size=(14, 1), disabled=True)],
            [sg.Text('Animal Doado', size=(20, 1)), sg.InputText(f'{doacao.animal.tipo} {doacao.animal.nome} | ID: {doacao.animail.id}', key='animal', disabled=True)],
            [sg.Text('Data da Doação', size=(20, 1)), sg.InputText(f'{doacao.data.strftime("%d")}', key='dia', size=(5, 1)), sg.Text('/'), sg.InputText(f'{doacao.data.strftime("%m")}', key='mes', size=(5, 1)), sg.Text('/'), sg.InputText(f'{doacao.data.strftime("%Y")}', key='ano', size=(5, 1))],
            [sg.Text('Motivo da Doação', size=(20, 1)), sg.InputText(f'{doacao.motivo}', key='motivo', size=(14, 1))],
            [sg.Button('Confirmar', font=('Arial', 10)), sg.Cancel('Retornar', font=('Arial', 10))]
            ]
            self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

            valores = self.window.read()

            if valores[0] == 'Retornar':
                self.window.close()
                return valores

            if not super().validaData(valores[1]['dia'], valores[1]['mes'], valores[1]['ano']):
                sg.popup('ERRO', 'Digite uma Data válida')
                self.window.close()
                continue

            if valores[0] == 'Confirmar':
                erro = False
                for key, value in valores[1].items():
                    if value == '':
                        sg.popup('ERRO', f'O campo {key} é obrigatório')
                        self.window.close()
                        erro = True
                        break
                if erro: continue
            
            self.window.close()
            return valores