import copy
from limite.tela_pessoa import TelaPessoa
from validate_docbr import CPF
from entidade import Pessoa, Endereco, dadosGlobais
from datetime import date, datetime

class ControladorPessoa:
    def __init__(self):
        self.tela = TelaPessoa(self)

    def iniciar(self):
        while True:
            self.tela.abreTela()
            escolha = self.tela.validaInput(2)
            if escolha == 0: return
            if escolha == 1: self.cadastrarPessoa()
            if escolha == 2: self.alterarPessoa()

    def cadastrarPessoa(self):
        print('''--------------------CADASTRO DE PESSOA--------------------

 000.000.000-00 | Nome | Endereco | Data de Nascimento


 Digite X para cancelar a operação.
--------------------CADASTRO DE PESSOA--------------------''')
        while True:
            try:
                cpf = self.validarCPF()
                if cpf.capitalize() == 'X': return
                for obj in dadosGlobais.pessoas:
                    if cpf == obj.cpf: raise ValueError
            except Exception: print(f'O CPF "{cpf}" já foi cadastrado, por favor digite outro')
            else: break

        print(f'''--------------------CADASTRO DE PESSOA--------------------

 {cpf} | Nome | Endereco | Data de Nascimento  


 Digite X para cancelar a operação.
--------------------CADASTRO DE PESSOA--------------------''')
        nome = str(input('Digite o Nome: '))
        if nome.capitalize() == 'X': return

        print(f'''--------------------CADASTRO DE PESSOA--------------------

 {cpf} | {nome} | Endereco | Data de Nascimento 


 Digite X para cancelar a operação.
--------------------CADASTRO DE PESSOA--------------------''')
        endereco = self.validarEndereco()
        if endereco.capitalize() == 'X': return

        print(f'''--------------------CADASTRO DE PESSOA--------------------

 {cpf} | {nome} | CEP: {endereco.cep}, n° {endereco.numero} | Data de Nascimento 


 Digite X para cancelar a operação.
--------------------CADASTRO DE PESSOA--------------------''')
        dataNascimento = self.validarIdade()
        if dataNascimento.capitalize() == 'X': return

        print(f'''--------------------CADASTRO DE PESSOA--------------------

 CPF: {cpf} | Nome: {nome} | CEP: {endereco.cep}, n° {endereco.numero} | Data de Nascimento: {dataNascimento[0]}/{dataNascimento[1]}/{dataNascimento[2]}


 Digite X para cancelar a operação.
--------------------CADASTRO DE PESSOA--------------------''')
        while True:
            try:
                confirma = str(input('Digite S para confirmar o cadastro: '))
                if confirma.capitalize() == 'X': return
                if confirma.capitalize() != 'S': raise ValueError
            except Exception: print('Valor inválido, por favor digite "S" ou "X"')
            else: break

        dadosGlobais.savePessoa(Pessoa(cpf, nome, dataNascimento, endereco))

        print(f'''--------------------CADASTRO DE PESSOA--------------------

 CPF: {cpf} | Nome: {nome} | CEP: {endereco.cep}, n° {endereco.numero} | Data de Nascimento: {dataNascimento[0]}/{dataNascimento[1]}/{dataNascimento[2]}


 Cadastro realizado com sucesso.
--------------------CADASTRO DE PESSOA--------------------''')
        input(' Clique ENTER para retornar: ')

    def alterarPessoa(self):
        print('--------------------LISTAS DE PESSOAS CADASTRADAS--------------------' + '\n')
        if len(dadosGlobais.pessoas) < 0: 
            print(' Não há nenhuma pessoa cadastrada no sistema.' + '\n'*2) 
            print('--------------------LISTAS DE PESSOAS CADASTRADAS--------------------')
            input(' Clique ENTER para retornar: '); return
        
        for i in range(len(dadosGlobais.pessoas)):
            pagina = 0
            totalPaginas = int(len(dadosGlobais.pessoas)/5) + 1
            print(f' {i+1}- {dadosGlobais.pessoas[i].nome} | {dadosGlobais.pessoas[i].cpf}')
            if i%5 == 0 or i == len(dadosGlobais.pessoas):
                pagina += 1
                print('\n'* 2 + ' Digite X para cancelar a operação.' + '\n')
                if i != len(dadosGlobais.pessoas): print(' Digite 0 para acessar a próxima página')
                print(f'--------------------Página {pagina} de {totalPaginas} no total--------------------')
                while True:
                    try:
                        escolha = str(input(' Digite o número do cadastro para alterar ou excluir: '))
                        if escolha.capitalize() == 'X': return
                        escolha = int(escolha)
                        if escolha == 0: break
                        if escolha < 1 or escolha > len(dadosGlobais.pessoas): raise ValueError
                    except Exception: print('Valor inválido, por favor digite novamente')
                    else: break
            if escolha == 0: continue
            break

        backupPessoa = copy.deepcopy(dadosGlobais.pessoas[escolha-1])
        print(f'''--------------------ALTERAR CADASTRO--------------------

 0- Excluir Cadastro
 1- CPF: {dadosGlobais.pessoas[escolha-1].cpf} 
 2- Nome: {dadosGlobais.pessoas[escolha-1].nome} 
 3- CEP: {dadosGlobais.pessoas[escolha-1].endereco.cep} | n° {dadosGlobais.pessoas[escolha-1].endereco.numero} | {dadosGlobais.pessoas[escolha-1].endereco.tipo} | {dadosGlobais.pessoas[escolha-1].endereco.tamanho} | {dadosGlobais.pessoas[escolha-1].endereco.animais}
 4- Data de Nascimento: {dadosGlobais.pessoas[escolha-1].dataNascimento[0]}/{dadosGlobais.pessoas[escolha-1].dataNascimento[1]}/{dadosGlobais.pessoas[escolha-1].dataNascimento[2]}


 Digite X para cancelar a operação.
--------------------ALTERAR CADASTRO--------------------''')
        while True:
            try:
                dado = str(input('Digite o número da opção desejada: '))
                if dado.capitalize() == 'X': return
                dado = int(dado)
                if dado < 1 or dado > 4: raise ValueError
            except Exception: print('Valor inválido, por favor digite novamente')
            else: break

        if dado == 0:
            print(f'''--------------------EXCLUIR CADASTRO--------------------

    CPF: {dadosGlobais.pessoas[escolha-1].cpf} 
    Nome: {dadosGlobais.pessoas[escolha-1].nome} 
    CEP: {dadosGlobais.pessoas[escolha-1].endereco.cep} | n° {dadosGlobais.pessoas[escolha-1].endereco.numero} | {dadosGlobais.pessoas[escolha-1].endereco.tipo} | {dadosGlobais.pessoas[escolha-1].endereco.tamanho} | {dadosGlobais.pessoas[escolha-1].endereco.animais}
    Data de Nascimento: {dadosGlobais.pessoas[escolha-1].dataNascimento[0]}/{dadosGlobais.pessoas[escolha-1].dataNascimento[1]}/{dadosGlobais.pessoas[escolha-1].dataNascimento[2]}


    Digite X para cancelar a operação.
    --------------------EXCLUIR CADASTRO--------------------''')
            while True:
                try:
                    confirma = str(input('Digite S para confirmar a exclusäo: '))
                    if confirma.capitalize() == 'X': return
                    if confirma.capitalize() != 'S': raise ValueError
                except Exception: print('Valor inválido, por favor digite "S" ou "X"')
                else: dadosGlobais.pessoas.pop(escolha-1); return

        if dado == 1: 
            novoDADO = self.validarCPF()
            if novoDADO.capitalize() == 'X': return
            dadosGlobais.pessoas[escolha-1].cpf = novoDADO

        if dado == 2: 
            novoDADO = str(input('Digite o Nome: '))
            if novoDADO.capitalize() == 'X': return
            dadosGlobais.pessoas[escolha-1].nome = novoDADO

        if dado == 3:
            novoDADO = self.validarEndereco()
            if novoDADO.capitalize() == 'X': return
            dadosGlobais.pessoas[escolha-1].endereco = novoDADO

        if dado == 4:
            novoDADO = self.validarIdade()
            if novoDADO.capitalize() == 'X': return
            dadosGlobais.pessoas[escolha-1].dataNascimento = novoDADO

        print(f'''--------------------ALTERAR CADASTRO--------------------

 CPF: {dadosGlobais.pessoas[escolha-1].cpf} 
 Nome: {dadosGlobais.pessoas[escolha-1].nome} 
 CEP: {dadosGlobais.pessoas[escolha-1].endereco.cep} | n° {dadosGlobais.pessoas[escolha-1].endereco.numero} | {dadosGlobais.pessoas[escolha-1].endereco.tipo} | {dadosGlobais.pessoas[escolha-1].endereco.tamanho} | {dadosGlobais.pessoas[escolha-1].endereco.animais}
 Data de Nascimento: {dadosGlobais.pessoas[escolha-1].dataNascimento[0]}/{dadosGlobais.pessoas[escolha-1].dataNascimento[1]}/{dadosGlobais.pessoas[escolha-1].dataNascimento[2]}


 Digite X para cancelar as alterações.
--------------------ALTERAR CADASTRO--------------------''')
        while True:
            try:
                confirma = str(input('Digite S para confirmar: '))
                if confirma.capitalize() == 'X': dadosGlobais.pessoas[escolha-1] = backupPessoa; return
                if confirma.capitalize() != 'S': raise ValueError
            except Exception: print('Valor inválido, por favor digite "S" ou "X"')
            else: break

    def validarCPF(self):
        vCpf = CPF()
        while True:
            try:
                cpf = str(input('Digite o CPF: '))
                if cpf.capitalize() == 'X': return cpf
                if not vCpf.validate(cpf): raise ValueError
            except Exception: print(f'O CPF "{cpf}" é inválido, por favor digite outro')
            else: return cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]

    def validarEndereco(self):
        print('''--------------------ENDEREÇO--------------------

 00000-000 | Número | Tipo | Tamanho | Quantidade de Animais


 Digite X para cancelar a operação.
--------------------ENDEREÇO--------------------''')
        while True:
            try:
                cep = str(input('Digite o CEP: '))
                if cep.capitalize() == 'X': return cep
                if not len(cep) == 8 or not cep.isdigit(): raise ValueError
            except Exception: print(f'O CEP "{cep}" é inválido, por favor digite outro')
            else: cep = cep[:5] + '-' + cep[5:9]; break

        print(f'''--------------------ENDEREÇO--------------------

 {cep} | Número | Tipo | Tamanho | Quantidade de Animais


 Digite X para cancelar a operação.
--------------------ENDEREÇO--------------------''')
        while True:
            try:
                num = str(input('Digite o número da residência: '))
                if num.capitalize() == 'X': return num
                num = int(num)
                if num < 1: raise ValueError
            except Exception: print('Valor inválido, por favor digite um número')
            else: break

        print(f'''--------------------ENDEREÇO--------------------

 {cep} | {num} | Tipo | Tamanho | Quantidade de Animais

 1 - Casa
 2 - Apartamento


 Digite X para cancelar a operação.
--------------------ENDEREÇO--------------------''')
        while True:
            try:
                tipo = str(input('Digite o número do tipo da residência: '))
                if tipo.capitalize() == 'X': return tipo
                tipo = int(tipo)
                if tipo < 1 or tipo > 2: raise ValueError
            except Exception: print('Valor inválido, por favor digite 1 ou 2')
            else:
                if tipo == 1: tipo = 'Casa'
                if tipo == 2: tipo = 'Apartamento'
                break

        print(f'''--------------------ENDEREÇO--------------------

 {cep} | {num} | {tipo} | Tamanho | Quantidade de Animais

 1 - Pequeno
 2 - Médio
 3 - Grande


 Digite X para cancelar a operação.
--------------------ENDEREÇO--------------------''')
        while True:
            try:
                tamanho = str(input('Digite o número do tamanho da residência: '))
                if tamanho.capitalize() == 'X': return tamanho
                tamanho = int(tamanho)
                if tamanho < 1 or tamanho > 3: raise ValueError
            except Exception: print('Valor inválido, por favor digite 1, 2 ou 3')
            else:
                if tamanho == 1: tamanho = 'Pequeno'
                if tamanho == 2: tamanho = 'Médio'
                if tamanho == 3: tamanho = 'Grande'
                break

        print(f'''--------------------ENDEREÇO--------------------

 {cep} | {num} | {tipo} | {tamanho} | Quantidade de Animais



 Digite X para cancelar a operação.
--------------------ENDEREÇO--------------------''')
        while True:
            try:
                animais = str(input('Digite o número de animais na residência: '))
                if animais.capitalize() == 'X': return animais
                animais = int(animais)
                if animais < 1: raise ValueError
            except Exception: print('Valor inválido, por favor digite novamente')
            else: break

        print(f'''--------------------ENDEREÇO--------------------

 {cep} | {num} | {tipo} | {tamanho} | {animais} animal(is)


 Digite X para cancelar a operação.
--------------------ENDEREÇO--------------------''')
        while True:
            try:
                confirma = str(input('Digite S para confirmar: '))
                if confirma.capitalize() == 'X': return confirma
                if confirma.capitalize() != 'S': raise ValueError
            except Exception: print('Valor inválido, por favor digite "S" ou "X"')
            else: 
                for obj in dadosGlobais.enderecos:
                    if cep == obj.cep and num == obj.numero: return obj
                return Endereco(cep, num, tipo, tamanho, animais)
            
    def validarIdade(self):
        while True:
            try:
                print('''--------------------IDADE--------------------

 00 / 00 / 0000


 Digite X para cancelar a operação.
--------------------IDADE--------------------''')
                while True:
                    try:
                        dia = str(input('Digite o dia da data de nascimento: '))
                        if dia.capitalize() == 'X': return dia
                        if not 0 < int(dia) < 32: raise ValueError
                    except Exception: print('Valor inválido, por favor digite novamente')
                    else: 
                        if int(dia) < 10: dia = "0" + dia
                        break

                print(f'''--------------------IDADE--------------------

 {dia} / 00 / 0000


 Digite X para cancelar a operação.
--------------------IDADE--------------------''')
                while True:
                    try:
                        mes = str(input('Digite o mês da data de nascimento: '))
                        if mes.capitalize() == 'X': return mes
                        if not 0 < int(mes) < 12: raise ValueError
                    except Exception: print('Valor inválido, por favor digite novamente')
                    else:
                        if int(mes) < 10: mes = "0" + mes
                        break

                print(f'''--------------------IDADE--------------------

 {dia} / {mes} / 0000


 Digite X para cancelar a operação.
--------------------IDADE--------------------''')
                while True:
                    try:
                        ano = str(input('Digite o ano da data de nascimento: '))
                        if ano.capitalize() == 'X': return ano
                        if not ano.isdigit() or len(ano) != 4: raise ValueError
                    except Exception: print('Valor inválido, por favor digite novamente')
                    else: break

                print(f'''--------------------IDADE--------------------

 {dia} / {mes} / {ano}


 Digite X para cancelar a operação.
--------------------IDADE--------------------''')
                
                while True:
                    try:
                        confirma = str(input('Digite S para confirmar: '))
                        if confirma.capitalize() == 'X': return confirma
                        if confirma.capitalize() != 'S': raise ValueError
                    except Exception: print('Valor inválido, por favor digite "S" ou "X"')
                    else: break
                
                data = date(int(ano), int(mes), int(dia))

                if (int(mes) == 2 and int(dia) == 29) and not (data.isocalendar()[1] == 9): raise ValueError

                idade = datetime.now().year - data.year
                if datetime.now().month < data.month or (datetime.now().month == data.month and datetime.now().day < data.day): idade -= 1
                if idade < 18: print('Não é permitido cadastrar menores de 18 anos.'); raise ValueError

                return [dia, mes, ano]
            
            except Exception: input('Data inválida, por favor digite novamente')




        



                

        




