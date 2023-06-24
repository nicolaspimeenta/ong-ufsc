import PySimpleGUI as sg
from validate_docbr import CPF
import datetime
from dateutil.relativedelta import relativedelta
from limite.tela_padrao import TelaPadrao

class TelaPessoa(TelaPadrao):
    def __init__(self):
        self.window = None
        self.init_layout()

    def init_layout(self):
        sg.ChangeLookAndFeel('TanBlue')
        layout = [
        [sg.Text('Escolha a opção desejada', font=("Arial", 15))],
        [sg.Radio('Cadastrar uma nova Pessoa', "RD1", key='1', font=('Arial', 10))],
        [sg.Radio('Gerenciar os cadastros de Pessoas', "RD1", key='2', font=('Arial', 10))],
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

    def cadastroPessoa(self):
        while True:
            layout = [
            [sg.Text('Dados Gerais:', font=('Arial', 12, 'bold'))],
            [sg.Text('Nome', size=(20, 1)), sg.InputText(key='nome')],
            [sg.Text('CPF (Apenas dígitos)', size=(20, 1)), sg.InputText(key='cpf', size=(14, 1))],
            [sg.Text('Data de Nascimento', size=(20, 1)), sg.InputText(key='dia', size=(5, 1)), sg.Text('/'), sg.InputText(key='mes', size=(5, 1)), sg.Text('/'), sg.InputText(key='ano', size=(5, 1))],
            [sg.Text('Endereço:', font=('Arial', 12, 'bold'))],
            [sg.Text('CEP (Apenas dígitos)', size=(20, 1)), sg.InputText(key='cep', size=(9, 1))],
            [sg.Text('Número', size=(20, 1)), sg.InputText(key='numero', size=(6, 1))],
            [sg.Text('Tipo de Residência', size=(20, 1)), sg.InputCombo(('Casa', 'Apartamento'), key='tipo')],
            [sg.Text('Tamanho da Residência', size=(20, 1)), sg.InputCombo(('Grande', 'Médio', 'Pequeno'), key='tamanho')],
            [sg.Text('Quantidade de Animais', size=(20, 1)), sg.InputText(key='animais', size=(4, 1))],
            [sg.Button('Confirmar', font=('Arial', 10)), sg.Cancel('Retornar', font=('Arial', 10))]
            ]
            self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

            valores = self.window.read()

            if valores[0] == 'Retornar':
                self.window.close()
                return valores

            if not self.validarCPF(valores[1]['cpf']):
                sg.popup('ERRO', 'Digite um CPF válido')
                self.window.close()
                continue

            if not (valores[1]['cep'].isdigit() and len(valores[1]['cep']) == 8):
                sg.popup('ERRO', 'Digite um CEP válido')
                self.window.close()
                continue

            if not self.validarIdade(valores[1]['dia'], valores[1]['mes'], valores[1]['ano']):
                sg.popup('ERRO', 'Digite uma Data válida')
                self.window.close()
                continue

            if not valores[1]['numero'].isdigit():
                sg.popup('ERRO', 'Digite um número válido')
                self.window.close()
                continue

            if not valores[1]['animais'].isdigit():
                sg.popup('ERRO', 'Digite um número válido')
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
        
    def gerenciarPessoa(self, pessoas):
        while True:
            layout = [
                [sg.Text('Lista de Pessoas Cadastradas:', font=('Arial', 12, 'bold'))],
                [sg.Text('Selecione uma para exclui-la ou altera-la', font=('Arial', 10))],
            ]
            if len(pessoas) == 0:
                layout.append([sg.Text('Não há nenhuma pessoa cadastrada', font=('Arial', 10, 'bold'))])
            else:
                for pessoa in pessoas:
                    layout.append([sg.Radio(f' {pessoa.nome} | {pessoa.cpf}', 'RADIO1')])

            layout.append([sg.Button('Alterar', font=('Arial', 10)), sg.Button('Excluir', font=('Arial', 10), button_color='#B22222'), sg.Cancel('Retornar', font=('Arial', 10))])
            self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

            valores = self.window.read()

            if valores[0] == 'Excluir' or valores[0] == 'Alterar':
                for key, value in valores[1].items():
                    if value == True:
                        self.window.close()
                        return valores
                sg.popup('ERRO', 'Selecione uma pessoa para altera-la ou exclui-la')
                continue

            self.window.close()
            return valores
        
    def alterarPessoa(self, pessoa):
        while True:
            layout = [
            [sg.Text('Dados Gerais:', font=('Arial', 12, 'bold'))],
            [sg.Text('Nome', size=(20, 1)), sg.InputText(f'{pessoa.nome}', key='nome')],
            [sg.Text('CPF (Apenas dígitos)', size=(20, 1)), sg.InputText(f'{pessoa.cpf}', key='cpf', size=(14, 1), disabled=True)],
            [sg.Text('Data de Nascimento', size=(20, 1)), sg.InputText(f'{pessoa.dataNascimento.strftime("%d")}', key='dia', size=(5, 1)), sg.Text('/'), sg.InputText(f'{pessoa.dataNascimento.strftime("%m")}', key='mes', size=(5, 1)), sg.Text('/'), sg.InputText(f'{pessoa.dataNascimento.strftime("%Y")}', key='ano', size=(5, 1))],
            [sg.Text('Endereço:', font=('Arial', 12, 'bold'))],
            [sg.Text('CEP (Apenas dígitos)', size=(20, 1)), sg.InputText(f'{pessoa.endereco.cep[:5] + pessoa.endereco.cep[6:9]}', key='cep', size=(9, 1))],
            [sg.Text('Número', size=(20, 1)), sg.InputText(f'{pessoa.endereco.numero}', key='numero', size=(6, 1))],
            [sg.Text('Tipo de Residência', size=(20, 1)), sg.InputCombo(('Casa', 'Apartamento'), key='tipo', default_value=pessoa.endereco.tipo)],
            [sg.Text('Tamanho da Residência', size=(20, 1)), sg.InputCombo(('Grande', 'Médio', 'Pequeno'), key='tamanho', default_value=pessoa.endereco.tamanho)],
            [sg.Text('Quantidade de Animais', size=(20, 1)), sg.InputText(f'{pessoa.endereco.animais}', key='animais', size=(4, 1))],
            [sg.Button('Confirmar', font=('Arial', 10)), sg.Cancel('Retornar', font=('Arial', 10))]
            ]
            self.window = sg.Window('ONG UFSC', layout, font=('Arial', 10))

            valores = self.window.read()

            if valores[0] == 'Retornar':
                self.window.close()
                return valores

            if not (valores[1]['cep'].isdigit() and len(valores[1]['cep']) == 8):
                sg.popup('ERRO', 'Digite um CEP válido')
                self.window.close()
                continue

            if not self.validarIdade(valores[1]['dia'], valores[1]['mes'], valores[1]['ano']):
                sg.popup('ERRO', 'Digite uma Data válida')
                self.window.close()
                continue

            if not valores[1]['numero'].isdigit():
                sg.popup('ERRO', 'Digite um número válido')
                self.window.close()
                continue

            if not valores[1]['animais'].isdigit():
                sg.popup('ERRO', 'Digite um número válido')
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
        
    def pessoaRepetida(self):
        sg.popup('ERRO', 'CPF já cadastrado')
        self.window.close()
        return

        
    def validarCPF(self, cpf: str):
        validator = CPF()
        if not cpf.isdigit(): return False
        if cpf == '12345678900': return True
        if not validator.validate(cpf): return False
        return True
    
    def validarIdade(self, dia, mes, ano):
        if super().validaData(dia, mes, ano):
            dataNascimento = datetime.date(int(ano), int(mes), int(dia))
            if dataNascimento > (datetime.date.today() - relativedelta(years=18)): return False
            else: return True
        else:
            return False
