import copy
from validate_docbr import CPF
from limite.tela_pessoa import TelaPessoa
from entidade import Pessoa, Endereco, dadosGlobais
from datetime import date, datetime

class ControladorPessoa:
    def __init__(self):
        self.__tela = TelaPessoa()

    @property
    def tela(self):
        return self.__tela

    def iniciar(self):
        while True:
            self.tela.abreTela()
            escolha = self.tela.validaInput(3)
            if escolha == 1: return
            if escolha == 2: self.cadastrarPessoa()
            if escolha == 3: self.alterarPessoa()
            dadosGlobais.savePessoa(Pessoa('086.407.259-77', 'Nicolas', ['25', '03', '2004'], Endereco('88052600', 2270, 'Casa', 'Médio', 3)))
            dadosGlobais.savePessoa(Pessoa('762.522.690-50', 'TESTE1', ['20', '02', '2003'], Endereco('88101030', 28, 'Apartamento', 'Pequeno', 0)))
            dadosGlobais.savePessoa(Pessoa('740.168.010-60', 'TESTE2', ['19', '11', '2001'], Endereco('88710210', 9, 'Casa', 'Grande', 1)))
            dadosGlobais.savePessoa(Pessoa('261.618.070-76', 'TESTE3', ['30', '08', '1983'], Endereco('88090222', 38, 'Apartamento', 'Médio', 10)))

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
        nome = str(input('\n Digite o Nome: '))
        if nome.capitalize() == 'X': return

        print('\n'*100 + '--------------------CADASTRO DE PESSOA--------------------')
        print(f'\n {cpf} | {nome} | Endereço | Data de Nascimento')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        pausa = input('\n Clique ENTER para cadastrar o endereço: ')
        if pausa.capitalize() == 'X': return
        endereco = self.validarEndereco()
        if type(endereco) == str and endereco.capitalize() == 'X': return

        print('\n'*100 + '--------------------CADASTRO DE PESSOA--------------------')
        print(f'\n {cpf} | {nome} | CEP: {endereco.cep}, n° {endereco.numero} | Data de Nascimento')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        dataNascimento = self.validarIdade()
        if type(dataNascimento) == str and dataNascimento.capitalize() == 'X': return

        print('\n'*100 + '--------------------CADASTRO DE PESSOA--------------------')
        print(f'\n CPF: {cpf} | Nome: {nome} | CEP: {endereco.cep}, n° {endereco.numero} | Data de Nascimento: {dataNascimento[0]}/{dataNascimento[1]}/{dataNascimento[2]}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar o cadastro: '))
                if confirma.capitalize() == 'X': return
                if confirma.capitalize() != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break

        dadosGlobais.savePessoa(Pessoa(cpf, nome, dataNascimento, endereco))

        print('\n'*100 + '--------------------CADASTRO DE PESSOA--------------------')
        print(f'\n CPF: {cpf} | Nome: {nome} | CEP: {endereco.cep}, n° {endereco.numero} | Data de Nascimento: {dataNascimento[0]}/{dataNascimento[1]}/{dataNascimento[2]}')
        print('\n'*2 + ' Cadastro realizado com sucesso.')
        print('----------------------------------------------------------')
        input('\n Clique ENTER para retornar: ')

    def alterarPessoa(self):
        print('\n'*100 + '--------------------LISTAS DE PESSOAS CADASTRADAS--------------------')
        if len(dadosGlobais.pessoas) == 0: 
            print('\n Não há nenhuma pessoa cadastrada no sistema.' + '') 
            print('---------------------------------------------------------------------')
            input('\n Clique ENTER para retornar: '); return
        
        print('\n 0- Cadastrar uma nova pessoa')
        for i in range(len(dadosGlobais.pessoas)): print(f' {i+1}- {dadosGlobais.pessoas[i].nome} | {dadosGlobais.pessoas[i].cpf}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('---------------------------------------------------------------------')
        while True:
            try:
                escolha = str(input('\n Digite o número do cadastro para alterar ou excluir: '))
                if escolha.capitalize() == 'X': return
                escolha = int(escolha)
                if escolha < 0 or escolha > len(dadosGlobais.pessoas): raise ValueError
                if escolha == 0: self.cadastrarPessoa(); return
            except Exception: print(' Valor inválido, por favor digite novamente')
            else: break

        backupPessoa = copy.deepcopy(dadosGlobais.pessoas[escolha-1])
        print('\n'*100 + '--------------------ALTERAR CADASTRO--------------------')
        print('\n 0- Excluir Cadastro')
        print(f' 1- CPF: {dadosGlobais.pessoas[escolha-1].cpf}')
        print(f' 2- Nome: {dadosGlobais.pessoas[escolha-1].nome}')
        print(f' 3- CEP: {dadosGlobais.pessoas[escolha-1].endereco.cep} | n° {dadosGlobais.pessoas[escolha-1].endereco.numero} | {dadosGlobais.pessoas[escolha-1].endereco.tipo} | {dadosGlobais.pessoas[escolha-1].endereco.tamanho} | {dadosGlobais.pessoas[escolha-1].endereco.animais}')
        print(f' 4- Data de Nascimento: {dadosGlobais.pessoas[escolha-1].dataNascimento[0]}/{dadosGlobais.pessoas[escolha-1].dataNascimento[1]}/{dadosGlobais.pessoas[escolha-1].dataNascimento[2]}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('--------------------------------------------------------')
        while True:
            try:
                dado = str(input('\n Digite o número da opção desejada: '))
                if dado.capitalize() == 'X': return
                dado = int(dado)
                if dado < 0 or dado > 4: raise ValueError
            except Exception: print(' Valor inválido, por favor digite novamente')
            else: break

        if dado == 0:
            print('\n'*100 + '--------------------EXCLUIR CADASTRO--------------------')
            print(f'\n CPF: {dadosGlobais.pessoas[escolha-1].cpf}')
            print(f' Nome: {dadosGlobais.pessoas[escolha-1].nome}')
            print(f' CEP: {dadosGlobais.pessoas[escolha-1].endereco.cep} | n° {dadosGlobais.pessoas[escolha-1].endereco.numero} | {dadosGlobais.pessoas[escolha-1].endereco.tipo} | {dadosGlobais.pessoas[escolha-1].endereco.tamanho} | {dadosGlobais.pessoas[escolha-1].endereco.animais}')
            print(f' Data de Nascimento: {dadosGlobais.pessoas[escolha-1].dataNascimento[0]}/{dadosGlobais.pessoas[escolha-1].dataNascimento[1]}/{dadosGlobais.pessoas[escolha-1].dataNascimento[2]}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('--------------------------------------------------------')
            while True:
                try:
                    confirma = str(input('\n Digite S para confirmar a exclusäo: '))
                    if confirma.capitalize() == 'X': return
                    if confirma.capitalize() != 'S': raise ValueError
                except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
                else: dadosGlobais.pessoas.pop(escolha-1); return

        if dado == 1: 
            novoDADO = self.validarCPF()
            if novoDADO.capitalize() == 'X': return
            dadosGlobais.pessoas[escolha-1].cpf = novoDADO

        if dado == 2: 
            novoDADO = str(input('\n Digite o Nome: '))
            if novoDADO.capitalize() == 'X': return
            dadosGlobais.pessoas[escolha-1].nome = novoDADO

        if dado == 3:
            novoDADO = self.validarEndereco()
            if type(novoDADO) == str and novoDADO.capitalize() == 'X': return
            dadosGlobais.pessoas[escolha-1].endereco = novoDADO

        if dado == 4:
            novoDADO = self.validarIdade()
            if type(novoDADO) == str and novoDADO.capitalize() == 'X': return
            dadosGlobais.pessoas[escolha-1].dataNascimento = novoDADO

        print('\n'*100 + '--------------------ALTERAR CADASTRO--------------------')
        print(f'\n CPF: {dadosGlobais.pessoas[escolha-1].cpf}')
        print(f' Nome: {dadosGlobais.pessoas[escolha-1].nome}')
        print(f' CEP: {dadosGlobais.pessoas[escolha-1].endereco.cep} | n° {dadosGlobais.pessoas[escolha-1].endereco.numero} | {dadosGlobais.pessoas[escolha-1].endereco.tipo} | {dadosGlobais.pessoas[escolha-1].endereco.tamanho} | {dadosGlobais.pessoas[escolha-1].endereco.animais}')
        print(f' Data de Nascimento: {dadosGlobais.pessoas[escolha-1].dataNascimento[0]}/{dadosGlobais.pessoas[escolha-1].dataNascimento[1]}/{dadosGlobais.pessoas[escolha-1].dataNascimento[2]}')
        print('\n'*2 + ' Digite X para cancelar as alterações.')
        print('--------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar: '))
                if confirma.capitalize() == 'X': dadosGlobais.pessoas[escolha-1] = backupPessoa; return
                if confirma.capitalize() != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break

    def validarCPF(self):
        vCpf = CPF()
        while True:
            try:
                cpf = str(input('\n Digite o CPF: '))
                if cpf.capitalize() == 'X': return cpf
                if cpf.capitalize() == 'R': cpf = vCpf.generate()
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
                cep = str(input('\n Digite o CEP: '))
                if cep.capitalize() == 'X': return cep
                if not len(cep) == 8 or not cep.isdigit(): raise ValueError
            except Exception: print(f' O CEP "{cep}" é inválido, por favor digite outro')
            else: cep = cep[:5] + '-' + cep[5:9]; break

        print('\n'*100 + '--------------------ENDEREÇO--------------------')
        print(f'\n {cep} | Número | Tipo | Tamanho | Quantidade de Animais')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('------------------------------------------------')
        while True:
            try:
                num = str(input('\n Digite o número da residência: '))
                if num.capitalize() == 'X': return num
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
        while True:
            try:
                tipo = str(input('\n Digite o número do tipo da residência: '))
                if tipo.capitalize() == 'X': return tipo
                tipo = int(tipo)
                if tipo < 1 or tipo > 2: raise ValueError
            except Exception: print(' Valor inválido, por favor digite 1 ou 2')
            else:
                if tipo == 1: tipo = 'Casa'
                if tipo == 2: tipo = 'Apartamento'
                break

        print('\n'*100 + '--------------------ENDEREÇO--------------------')
        print(f'\n {cep} | {num} | {tipo} | Tamanho | Quantidade de Animais')
        print('\n 1- Pequeno')
        print(' 2- Médio')
        print(' 3- Grande')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('------------------------------------------------')
        while True:
            try:
                tamanho = str(input('\n Digite o número do tamanho da residência: '))
                if tamanho.capitalize() == 'X': return tamanho
                tamanho = int(tamanho)
                if tamanho < 1 or tamanho > 3: raise ValueError
            except Exception: print(' Valor inválido, por favor digite 1, 2 ou 3')
            else:
                if tamanho == 1: tamanho = 'Pequeno'
                if tamanho == 2: tamanho = 'Médio'
                if tamanho == 3: tamanho = 'Grande'
                break

        print('\n'*100 + '--------------------ENDEREÇO--------------------')
        print(f'\n {cep} | {num} | {tipo} | {tamanho} | Quantidade de Animais')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('------------------------------------------------')
        while True:
            try:
                animais = str(input('\n Digite o número de animais na residência: '))
                if animais.capitalize() == 'X': return animais
                animais = int(animais)
                if animais < 1: raise ValueError
            except Exception: print(' Valor inválido, por favor digite novamente')
            else: break

        print('\n'*100 + '--------------------ENDEREÇO--------------------')
        print(f'\n {cep} | {num} | {tipo} | {tamanho} | {animais} animal(is)')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar: '))
                if confirma.capitalize() == 'X': return confirma
                if confirma.capitalize() != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: 
                for obj in dadosGlobais.enderecos:
                    if cep == obj.cep and num == obj.numero: return obj
                return Endereco(cep, num, tipo, tamanho, animais)
            
    def validarIdade(self):
        while True:
            try:
                print('\n'*100 + '--------------------IDADE--------------------')
                print('\n 00 / 00 / 0000')
                print('\n'*2 + ' Digite X para cancelar a operação.')
                print('------------------------------------------------')
                while True:
                    try:
                        dia = str(input('\n Digite o dia da data de nascimento: '))
                        if dia.capitalize() == 'X': return dia
                        if not 0 < int(dia) < 32: raise ValueError
                    except Exception: print(' Valor inválido, por favor digite novamente')
                    else: 
                        if len(dia) == 1: dia = "0" + dia
                        break

                print('\n'*100 + '--------------------IDADE--------------------')
                print(f'\n {dia} / 00 / 0000')
                print('\n'*2 + ' Digite X para cancelar a operação.')
                print('------------------------------------------------')
                while True:
                    try:
                        mes = str(input('\n Digite o mês da data de nascimento: '))
                        if mes.capitalize() == 'X': return mes
                        if not 0 < int(mes) < 13: raise ValueError
                    except Exception: print(' Valor inválido, por favor digite novamente')
                    else:
                        if len(mes) == 1: mes = "0" + mes
                        break

                print('\n'*100 + '--------------------IDADE--------------------')
                print(f'\n {dia} / {mes} / 0000')
                print('\n'*2 + ' Digite X para cancelar a operação.')
                print('------------------------------------------------')
                while True:
                    try:
                        ano = str(input('\n Digite o ano da data de nascimento: '))
                        if ano.capitalize() == 'X': return ano
                        if not ano.isdigit() or len(ano) != 4: raise ValueError
                    except Exception: print(' Valor inválido, por favor digite novamente')
                    else: break

                print('\n'*100 + '--------------------IDADE--------------------')
                print(f'\n {dia} / {mes} / {ano}')
                print('\n'*2 + ' Digite X para cancelar a operação.')
                print('------------------------------------------------')
                
                while True:
                    try:
                        confirma = str(input('\n Digite S para confirmar: '))
                        if confirma.capitalize() == 'X': return confirma
                        if confirma.capitalize() != 'S': raise ValueError
                    except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
                    else: break
                
                data = date(int(ano), int(mes), int(dia))

                if (int(mes) == 2 and int(dia) == 29) and not (data.isocalendar()[1] == 9): raise ValueError

                if datetime.now().year < data.year or (datetime.now().year == data.year and datetime.now().month < data.month) or (datetime.now().year == data.year and datetime.now().month == data.month and datetime.now().day < data.day):
                    raise ValueError

                idade = datetime.now().year - data.year
                if datetime.now().month < data.month or (datetime.now().month == data.month and datetime.now().day < data.day): idade -= 1
                if idade < 18: print(' Não é permitido cadastrar menores de 18 anos.'); raise ValueError

                return [dia, mes, ano]
            
            except Exception: input('\n Data inválida, por favor clique ENTER para tentar novamente ')




        



                

        




