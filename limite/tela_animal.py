import PySimpleGUI as sg
from limite.tela_padrao import TelaPadrao
import datetime

class TelaAnimal(TelaPadrao):
    def __init__(self):
        self.__window = None
        self.init_layout()

    def init_layout(self):
        sg.ChangeLookAndFeel('TanBlue')
        layout = [
        [sg.Text('Escolha a opção desejada', font=("Arial", 15))],
        [sg.Radio('Cadastrar um novo Animal', "RD1", key='1', font=('Arial', 10))],
        [sg.Radio('Gerenciar os cadastros de Animal', "RD1", key='2', font=('Arial', 10))],
        [sg.Radio('Registrar uma nova Vacina', "RD1", key='3', font=('Arial', 10))],
        [sg.Button('Confirmar', font=('Arial', 10)), sg.Cancel('Retornar', font=('Arial', 10))]
        ]
        self.__window = sg.Window('ONG UFSC', layout, size=(400, 170), font=('Arial', 10))

    def abreTela(self):
        self.init_layout()
        valores = self.__window.Read()
        escolha = 0
        for key, value in valores[1].items():
            if value == True:
                escolha = key
        self.__window.Close()
        if valores[0] == 'Retornar': return 0
        return escolha
    
    def cadastroAnimal(self):
        while True:
            layout = [
            [sg.Text('Dados Gerais:', font=('Arial', 12, 'bold'))],
            [sg.Text('Espécie', size=(20, 1)), sg.InputCombo(('Cachorro Grande', 'Cachorro Médio', 'Cachorro Pequeno', 'Gato'), key='tipo')],
            [sg.Text('Nome', size=(20, 1)), sg.InputText(key='nome')],
            [sg.Text('Raça', size=(20, 1)), sg.InputText(key='raca')],
            [sg.Button('Confirmar', font=('Arial', 10)), sg.Cancel('Retornar', font=('Arial', 10))]
            ]
            self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

            valores = self.window.Read()
            print(valores)

            if valores[0] == 'Retornar':
                self.window.Close()
                return valores

            if valores[0] == 'Confirmar':
                erro = False
                for key, value in valores[1].items():
                    if value == '':
                        sg.Popup('ERRO', f'O campo {key} é obrigatório')
                        self.window.Close()
                        erro = True
                        break
                if erro: continue
            
            self.window.Close()
            return valores
        
    def gerenciarAnimal(self, animais):
        while True:
            layout = [
                [sg.Text('Lista de Animais Cadastrados:', font=('Arial', 12, 'bold'))],
                [sg.Text('Selecione um para exclui-lo ou altera-lo', font=('Arial', 10))],
            ]
            if len(animais) == 0:
                layout.append([sg.Text('Não há nenhum animal cadastrado', font=('Arial', 10, 'bold'))])
            else:
                for animal in animais:
                    layout.append([sg.Radio(f' {animal.nome} | ID: {animal.id}', 'RADIO1')])

            layout.append([sg.Button('Alterar', font=('Arial', 10)), sg.Button('Excluir', font=('Arial', 10), button_color='#B22222'), sg.Cancel('Retornar', font=('Arial', 10))])
            self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

            valores = self.window.Read()
            print(valores)

            if valores[0] == 'Excluir' or valores[0] == 'Alterar':
                for key, value in valores[1].items():
                    if value == True:
                        self.window.Close()
                        return valores
                sg.Popup('ERRO', 'Selecione um animal para altera-lo ou exclui-lo')
                continue

            self.window.Close()
            return valores
        
    def alterarAnimal(self, animal):
        while True:
            dono = 'Sem dono cadastrado'
            if animal.dono: dono = f'{animal.dono.nome} | {animal.dono.cpf}'
            layout = [
            [sg.Text('Dados Gerais:', font=('Arial', 12, 'bold'))],
            [sg.Text('ID', size=(20, 1)), sg.InputText(f'{animal.id}', key='id', size=(14, 1), disabled=True)],
            [sg.Text('Nome', size=(20, 1)), sg.InputText(f'{animal.nome}', key='nome')],
            [sg.Text('Raça', size=(20, 1)), sg.InputText(f'{animal.raca}', key='raca')],
            [sg.Text('Vacinas', size=(20, 1)), sg.Text(f'{len(animal.vacinas)}'), sg.Button('Aplicar Vacina', font=('Arial', 10))],
            [sg.Text('Espécie', size=(20, 1)), sg.InputCombo(('Cachorro Grande', 'Cachorro Médio', 'Cachorro Pequeno', 'Gato'), key='tipo')],
            [sg.Text('Dono', size=(20, 1)), sg.InputText(f'{dono}', key='dono')],
            [sg.Button('Confirmar', font=('Arial', 10)), sg.Cancel('Retornar', font=('Arial', 10))]
            ]
            self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

            valores = self.window.Read()

            if valores[0] == 'Retornar' or valores[0] == 'Aplicar Vacina':
                self.window.Close()
                return valores

            if animal.tipo != valores[1]['tipo'].split(' ')[0]:
                sg.Popup('ERRO', 'Não é possível alterar a espécie do animal (apenas o tamanho)')
                self.window.Close()
                continue

            if valores[0] == 'Confirmar':
                erro = False
                for key, value in valores[1].items():
                    if value == '':
                        sg.Popup('ERRO', f'O campo {key} é obrigatório')
                        self.window.Close()
                        erro = True
                        break
                if erro: continue
            
            self.window.Close()
            return valores
        
    def aplicarVacina(self, animais, escolherAnimal = False, id = 0):
        animaisEscolhidos = []
        if escolherAnimal:
            while True:
                layout = [
                    [sg.Text('Lista de Animais Cadastrados:', font=('Arial', 12, 'bold'))],
                    [sg.Text('Selecione um ou mais para aplicar uma vacina', font=('Arial', 10))],
                ]
                if len(animais) == 0:
                    layout.append([sg.Text('Não há nenhum animal cadastrado', font=('Arial', 10, 'bold'))])
                else:
                    for animal in animais:
                        layout.append([sg.Checkbox(f' {animal.nome} | ID: {animal.id}', key=animal.id)])

                layout.append([sg.Button('Confirmar', font=('Arial', 10)), sg.Cancel('Retornar', font=('Arial', 10))])
                self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

                valores = self.window.Read()

                if valores[0] == 'Retornar':
                    self.window.Close()
                    return valores
                
                if valores[0] == 'Confirmar':
                    for key, value in valores[1].items():
                        if value == True:
                            animaisEscolhidos.append(key)
                    if len(animaisEscolhidos) == 0:
                        sg.Popup('ERRO', 'Selecione pelo menos um animal para aplicar a vacina')
                        continue
                break
        else: animaisEscolhidos.append(id)

        self.window.Close()
        while True:
            layout = [
            [sg.Text(f'Aplicando Vacina em {len(animaisEscolhidos)} animal(is)', font=('Arial', 12, 'bold'))],
            [sg.Text('Tipo da Vacina', size=(20, 1)), sg.InputText(key='tipo')],
            [sg.Text('Data de Nascimento', size=(20, 1)), sg.InputText(f'{datetime.today.strftime("%d")}', key='dia', size=(5, 1)), sg.Text('/'), sg.InputText(f'{datetime.today.strftime("%m")}', key='mes', size=(5, 1)), sg.Text('/'), sg.InputText(f'{datetime.today.strftime("%Y")}', key='ano', size=(5, 1))],
            [sg.Button('Confirmar', font=('Arial', 10)), sg.Cancel('Retornar', font=('Arial', 10))]
            ]
            self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

            valores = self.window.Read()

            if valores[0] == 'Retornar':
                self.window.Close()
                return valores

            if not super().validaData():
                sg.Popup('ERRO', 'Digite uma Data válida')
                self.window.Close()
                continue

            if valores[0] == 'Confirmar':
                erro = False
                for key, value in valores[1].items():
                    if value == '':
                        sg.Popup('ERRO', f'O campo {key} é obrigatório')
                        self.window.Close()
                        erro = True
                        break
                if erro: continue
            
            self.window.Close()
            return valores, animaisEscolhidos


            
        