import copy
import datetime
from validate_docbr import CPF
from dateutil.relativedelta import relativedelta
from limite.tela_pessoa import TelaPessoa
from entidade.pessoa import Pessoa
from entidade.endereco import Endereco
from entidade import dadosGlobais

class ControladorPessoa:
    def __init__(self):
        self.tela = TelaPessoa()

    def iniciar(self):
        while True:
            self.tela.abreTela()
            escolha = self.tela.validaInput(min=1, max=2, msg='Digite o número da opção desejada')
            if escolha == 'X': return
            if escolha == 1: self.cadastrarPessoa()
            if escolha == 2: self.gerenciarPessoa()

    def listarPessoa(self, msg = ' ', adocao = False, cachorroGrande = False):
        if adocao:
            print('\n'*100 + '--------------------LISTA DE PESSOAS CADASTRADAS--------------------')
            print(f' {msg}')
            print(' 0- Cadastrar uma nova pessoa')
            if len(dadosGlobais.pessoas) == 0: print(' Não há nenhuma pessoa cadastrada no sistema.')
            else:
                listaAdotantes = []
                for pessoa in dadosGlobais.pessoas:
                    if self.validaAdocao(pessoa, cachorroGrande): listaAdotantes.append(pessoa)
                for i in range(listaAdotantes): print(f' {i+1}- {listaAdotantes[i].nome} | {listaAdotantes[i].cpf}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('---------------------------------------------------------------------')
            return listaAdotantes

        if not adocao:
            print('\n'*100 + '--------------------LISTA DE PESSOAS CADASTRADAS--------------------')
            print(f' {msg}')
            print(' 0- Cadastrar uma nova pessoa')
            if len(dadosGlobais.pessoas) == 0: print(' Não há nenhuma pessoa cadastrada no sistema.')
            else:
                for i in range(len(dadosGlobais.pessoas)): print(f' {i+1}- {dadosGlobais.pessoas[i].nome} | {dadosGlobais.pessoas[i].cpf}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('---------------------------------------------------------------------')

    def cadastrarPessoa(self):
        print('\n'*100 + '--------------------CADASTRO DE PESSOA--------------------')
        print('\n 000.000.000-00 | Nome | Endereço | Data de Nascimento')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        while True:
            try:
                cpf = self.validarCPF()
                if cpf.capitalize() == 'X': return
                for obj in dadosGlobais.pessoas:
                    if cpf == obj.cpf: raise ValueError
            except Exception: print(f' O CPF "{cpf}" já foi cadastrado, por favor digite outro')
            else: break

        print('\n'*100 + '--------------------CADASTRO DE PESSOA--------------------')
        print(f'\n {cpf} | Nome | Endereço | Data de Nascimento') 
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        nome = str(input('\n Digite o Nome: ')).capitalize()
        if nome == 'X': return

        print('\n'*100 + '--------------------CADASTRO DE PESSOA--------------------')
        print(f'\n {cpf} | {nome} | Endereço | Data de Nascimento')
        print('----------------------------------------------------------')
        pausa = input('\n Clique ENTER para cadastrar o endereço: ')
        if pausa.capitalize() == 'X': return
        endereco = self.validarEndereco()
        if endereco == 'X': return

        print('\n'*100 + '--------------------CADASTRO DE PESSOA--------------------')
        print(f'\n {cpf} | {nome} | CEP: {endereco.cep}, n° {endereco.numero} | Data de Nascimento')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        dataNascimento = self.validarIdade()
        if dataNascimento == 'X': return

        print('\n'*100 + '--------------------CADASTRO DE PESSOA--------------------')
        print(f'\n CPF: {cpf} | Nome: {nome} | CEP: {endereco.cep}, n° {endereco.numero} | Data de Nascimento: {dataNascimento.strftime("%d")}/{dataNascimento.strftime("%m")}/{dataNascimento.strftime("%Y")}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar o cadastro: ')).capitalize()
                if confirma == 'X': return
                if confirma != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break

        dadosGlobais.savePessoa(Pessoa(cpf, nome, dataNascimento, endereco))

        print('\n'*100 + '--------------------CADASTRO DE PESSOA--------------------')
        print(f'\n CPF: {cpf} | Nome: {nome} | CEP: {endereco.cep}, n° {endereco.numero} | Data de Nascimento: {dataNascimento.strftime("%d")}/{dataNascimento.strftime("%m")}/{dataNascimento.strftime("%Y")}')
        print('\n'*2 + ' Cadastro realizado com sucesso.')
        print('----------------------------------------------------------')
        input('\n Clique ENTER para continuar: ')

    def gerenciarPessoa(self):
        self.listarPessoa()

        escolha = self.tela.validaInput(max=len(dadosGlobais.pessoas), msg='Digite o número do cadastro que deseja alterar ou excluir')

        if escolha == 'X': return
        if escolha == 0: self.cadastrarPessoa(); return

        backupPessoa = copy.deepcopy(dadosGlobais.pessoas[escolha-1])
        print('\n'*100 + '--------------------ALTERAR CADASTRO--------------------')
        print('\n 0- Excluir Cadastro')
        print(f' 1- CPF: {dadosGlobais.pessoas[escolha-1].cpf}')
        print(f' 2- Nome: {dadosGlobais.pessoas[escolha-1].nome}')
        print(f' 3- CEP: {dadosGlobais.pessoas[escolha-1].endereco.cep} | n° {dadosGlobais.pessoas[escolha-1].endereco.numero} | {dadosGlobais.pessoas[escolha-1].endereco.tipo} | {dadosGlobais.pessoas[escolha-1].endereco.tamanho} | {dadosGlobais.pessoas[escolha-1].endereco.animais}')
        print(f' 4- Data de Nascimento: {dadosGlobais.pessoas[escolha-1].dataNascimento.strftime("%d")}/{dadosGlobais.pessoas[escolha-1].dataNascimento.strftime("%m")}/{dadosGlobais.pessoas[escolha-1].dataNascimento.strftime("%Y")}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('--------------------------------------------------------')
        dado = self.tela.validaInput(max=4)
        if dado == 'X': return

        if dado == 0:
            print('\n'*100 + '--------------------EXCLUIR CADASTRO--------------------')
            print(f'\n CPF: {dadosGlobais.pessoas[escolha-1].cpf}')
            print(f' Nome: {dadosGlobais.pessoas[escolha-1].nome}')
            print(f' CEP: {dadosGlobais.pessoas[escolha-1].endereco.cep} | n° {dadosGlobais.pessoas[escolha-1].endereco.numero} | {dadosGlobais.pessoas[escolha-1].endereco.tipo} | {dadosGlobais.pessoas[escolha-1].endereco.tamanho} | {dadosGlobais.pessoas[escolha-1].endereco.animais}')
            print(f' Data de Nascimento: {dadosGlobais.pessoas[escolha-1].dataNascimento.strftime("%d")}/{dadosGlobais.pessoas[escolha-1].dataNascimento.strftime("%m")}/{dadosGlobais.pessoas[escolha-1].dataNascimento.strftime("%Y")}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('--------------------------------------------------------')
            while True:
                try:
                    confirma = str(input('\n Digite S para confirmar a exclusäo: ')).capitalize()
                    if confirma == 'X': return
                    if confirma != 'S': raise ValueError
                except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
                else: dadosGlobais.pessoas.pop(escolha-1); return

        if dado == 1: 
            novoDado = self.validarCPF()
            if novoDado.capitalize() == 'X': return
            dadosGlobais.pessoas[escolha-1].cpf = novoDado

        if dado == 2: 
            novoDado = str(input('\n Digite o Nome: ')).capitalize()
            if novoDado == 'X': return
            dadosGlobais.pessoas[escolha-1].nome = novoDado

        if dado == 3:
            novoDado = self.validarEndereco()
            if novoDado == 'X': return
            dadosGlobais.pessoas[escolha-1].endereco = novoDado

        if dado == 4:
            novoDado = self.validarIdade()
            if novoDado == 'X': return
            dadosGlobais.pessoas[escolha-1].dataNascimento = novoDado

        print('\n'*100 + '--------------------ALTERAR CADASTRO--------------------')
        print(f'\n CPF: {dadosGlobais.pessoas[escolha-1].cpf}')
        print(f' Nome: {dadosGlobais.pessoas[escolha-1].nome}')
        print(f' CEP: {dadosGlobais.pessoas[escolha-1].endereco.cep} | n° {dadosGlobais.pessoas[escolha-1].endereco.numero} | {dadosGlobais.pessoas[escolha-1].endereco.tipo} | {dadosGlobais.pessoas[escolha-1].endereco.tamanho} | {dadosGlobais.pessoas[escolha-1].endereco.animais}')
        print(f' Data de Nascimento: {dadosGlobais.pessoas[escolha-1].dataNascimento.strftime("%d")}/{dadosGlobais.pessoas[escolha-1].dataNascimento.strftime("%m")}/{dadosGlobais.pessoas[escolha-1].dataNascimento.strftime("%Y")}')
        print('\n'*2 + ' Digite X para cancelar as alterações.')
        print('--------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar: ')).capitalize()
                if confirma == 'X': dadosGlobais.pessoas[escolha-1] = backupPessoa; return
                if confirma != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break

    def validarCPF(self):
        vCpf = CPF()
        while True:
            try:
                cpf = str(input('\n Digite o CPF: ')).capitalize()
                if cpf == 'X': return cpf
                if cpf == 'R': cpf = vCpf.generate()
                if not vCpf.validate(cpf): raise ValueError
            except Exception: print(f' O CPF "{cpf}" é inválido, por favor digite outro')
            else: return cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]

    def validarEndereco(self):
        print('\n'*100 + '--------------------ENDEREÇO--------------------')
        print('\n 00000-000 | Número | Tipo | Tamanho | Quantidade de Animais')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('------------------------------------------------')
        while True:
            try:
                cep = str(input('\n Digite o CEP: ')).capitalize()
                if cep == 'X': return cep
                if not len(cep) == 8 or not cep.isdigit(): raise ValueError
            except Exception: print(f' O CEP "{cep}" é inválido, por favor digite outro')
            else: cep = cep[:5] + '-' + cep[5:9]; break

        print('\n'*100 + '--------------------ENDEREÇO--------------------')
        print(f'\n {cep} | Número | Tipo | Tamanho | Quantidade de Animais')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('------------------------------------------------')
        while True:
            try:
                num = str(input('\n Digite o número da residência: ')).capitalize()
                if num == 'X': return num
                num = int(num)
                if num < 1: raise ValueError
            except Exception: print(' Valor inválido, por favor digite um número')
            else: break

        print('\n'*100 + '--------------------ENDEREÇO--------------------')
        print(f'\n {cep} | {num} | Tipo | Tamanho | Quantidade de Animais')
        print('\n 1- Casa')
        print(' 2- Apartamento')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('------------------------------------------------')
        tipo = self.tela.validaInput(min=1, max=2, msg='Digite o número do tipo da residência')
        if tipo == 'X': return tipo
        if tipo == 1: tipo = 'Casa'
        if tipo == 2: tipo = 'Apartamento'

        print('\n'*100 + '--------------------ENDEREÇO--------------------')
        print(f'\n {cep} | {num} | {tipo} | Tamanho | Quantidade de Animais')
        print('\n 1- Pequeno')
        print(' 2- Médio')
        print(' 3- Grande')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('------------------------------------------------')
        tamanho = self.tela.validaInput(min=1, max=3, msg='Digite o número do tamanho da residência')
        if tamanho == 'X': return tamanho
        if tamanho == 1: tamanho = 'Pequeno'
        if tamanho == 2: tamanho = 'Médio'
        if tamanho == 3: tamanho = 'Grande'

        print('\n'*100 + '--------------------ENDEREÇO--------------------')
        print(f'\n {cep} | {num} | {tipo} | {tamanho} | Quantidade de Animais')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('------------------------------------------------')
        while True:
            try:
                animais = str(input('\n Digite o número de animais na residência: ')).capitalize()
                if animais == 'X': return animais
                animais = int(animais)
                if animais < 0: raise ValueError
            except Exception: print(' Valor inválido, por favor digite novamente')
            else: break

        print('\n'*100 + '--------------------ENDEREÇO--------------------')
        print(f'\n {cep} | {num} | {tipo} | {tamanho} | {animais} animal(is)')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar: ')).capitalize()
                if confirma == 'X': return confirma
                if confirma != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: 
                for obj in dadosGlobais.enderecos:
                    if cep == obj.cep and num == obj.numero: return obj
                dadosGlobais.saveEndereco(Endereco(cep, num, tipo, tamanho, animais))
                return dadosGlobais.enderecos[-1]
            
    def validarIdade(self):
        while True:
            dataNascimento = self.tela.validaData(False)
            if dataNascimento == 'X': break
            if dataNascimento > (datetime.date.today() - relativedelta(years=18)): print(' Não é permitido cadastrar menores de 18 anos, por favor tente novamente')
            else: break
        return dataNascimento

    def validaAdocao(self, pessoa, cachorroGrande):
        for doacao in dadosGlobais.doacoes:
            if pessoa == doacao.pessoa: return False
        if cachorroGrande and pessoa.endereco.tipo == 'Apartamento' and pessoa.endereco.tamanho == 'Pequeno': return False
        return True




        



                

        




