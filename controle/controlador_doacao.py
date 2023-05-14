import copy
from limite.tela_doacao import TelaDoacao
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_animal import ControladorAnimal
from entidade import dadosGlobais
from entidade.doacao import Doacao
from datetime import date, datetime

class ControladorDoacao:
    def __init__(self):
        self.__controlador_pessoa = ControladorPessoa()
        self.__controlador_animal = ControladorAnimal()
        self.__tela = TelaDoacao()
    
    def iniciar(self):
        while True:
            self.__tela.abreTela()
            escolha = self.__tela.validaInput(2, 'Digite o número da opção desejada', 1)
            if escolha == 'X': return
            if escolha == 1: self.cadastrarDoacao()
            if escolha == 2: self.gerenciarDoacao()


    def cadastrarDoacao(self):
        print('\n'*100 + '--------------------DOAÇÃO DE ANIMAL--------------------')
        print('\n Doador | Animal | Motivo | Data')
        print('----------------------------------------------------------')
        input('Clique ENTER para registrar o Doador')

        self.__controlador_pessoa.listarPessoa('Digite o número da pessoa que irá doar o animal. \n')
        escolha = self.__tela.validaInput(len(dadosGlobais.pessoas))
        if escolha == 'X': return
        if escolha == 0: 
            tamanhoAnterior = len(dadosGlobais.pessoas)
            self.__controlador_pessoa.cadastrarPessoa()
            if tamanhoAnterior < len(dadosGlobais.pessoas): escolha = len(dadosGlobais.pessoas)
            else: return
        if dadosGlobais.pessoas[escolha-1].endereco.animais > 0: dadosGlobais.pessoas[escolha-1].endereco.animais -= 1

        print('\n'*100 + '--------------------DOAÇÃO DE ANIMAL--------------------')
        print(f'\n Doador: {dadosGlobais.pessoas[escolha-1].nome} | Animal | Motivo | Data')
        print('----------------------------------------------------------')
        input('Clique ENTER para registrar o Animal')

        tamanhoAnterior = len(dadosGlobais.animais)
        self.__controlador_animal.cadastrarAnimal()
        if tamanhoAnterior == len(dadosGlobais.animais): return

        print('\n'*100 + '--------------------DOAÇÃO DE ANIMAL--------------------')
        print(f'\n Doador: {dadosGlobais.pessoas[escolha-1].nome} | Animal: {dadosGlobais.animais[-1].nome} | Motivo | Data')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')

        motivo = str(input('\n Digite o Motivo da doação: ')).capitalize()
        if motivo == 'X': return

        print('\n'*100 + '--------------------DOAÇÃO DE ANIMAL--------------------')
        print(f'\n Doador: {dadosGlobais.pessoas[escolha-1].nome} | Animal: {dadosGlobais.animais[-1].nome} | Motivo: {motivo} | Data')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')

        while True:
            data = str(input('\n Digite S se a doação foi hoje ou N se foi em outro dia: ')).capitalize()
            if data != 'S' and data != 'N' and data != 'X': print(' Valor inválido, por favor tente novamente')
            else: break
        if data == 'X': return
        if data == 'S':
            dia = datetime.now().day
            if dia < 10: dia = '0' + str(dia)
            dia = str(dia)

            mes = datetime.now().month
            if mes < 10: mes = '0' + str(mes)
            mes = str(mes)

            ano = str(datetime.now().year)

        if data == 'N':
            while True:
                try:
                    dia = str(self.__tela.validaInput(min=1, max=31, msg='Digite o dia da aplicação da vacina'))
                    if dia == 'X': return dia
                    if len(dia) == 1: dia = "0" + dia

                    mes = str(self.__tela.validaInput(min=1, max=12, msg='Digite o mês da aplicação da vacina'))
                    if mes == 'X': return mes
                    if len(mes) == 1: mes = "0" + mes

                    while True:
                        try:
                            ano = str(input('\n Digite o ano da aplicação da vacina: '))
                            if ano.capitalize() == 'X': return ano
                            if not ano.isdigit() or len(ano) != 4: raise ValueError
                        except Exception: print(' Valor inválido, por favor digite novamente')
                        else: break
                    
                    data = date(int(ano), int(mes), int(dia))

                    if (int(mes) == 2 and int(dia) == 29) and not (data.isocalendar()[1] == 9): raise ValueError

                    if datetime.now().year < data.year or (datetime.now().year == data.year and datetime.now().month < data.month) or (datetime.now().year == data.year and datetime.now().month == data.month and datetime.now().day < data.day):
                        raise ValueError

                except Exception: input('\n Data inválida, por favor clique ENTER para tentar novamente ')
                else: break

        data = [dia, mes, ano]

        print('\n'*100 + '--------------------DOAÇÃO DE ANIMAL--------------------')
        print(f'\n Doador: {dadosGlobais.pessoas[escolha-1].nome} | Animal: {dadosGlobais.animais[-1].nome} | Motivo: {motivo} | Data: {data[0]}/{data[1]}/{data[2]}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar: ')).capitalize()
                if confirma == 'X': return
                if confirma != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break

        print('\n'*100 + '--------------------DOAÇÃO DE ANIMAL--------------------')
        print(f'\n Doador: {dadosGlobais.pessoas[escolha-1].nome} | Animal: {dadosGlobais.animais[-1].nome} | Motivo: {motivo} | Data: {data[0]}/{data[1]}/{data[2]}')
        print('\n'*2 + ' Doação realizada com sucesso.')
        print('----------------------------------------------------------')
        input('Clique ENTER para continuar')

        dadosGlobais.saveDoacao(Doacao(dadosGlobais.pessoas[escolha-1], dadosGlobais.animais[-1], data, motivo))

    def gerenciarDoacao(self):
        print('\n'*100 + '--------------------LISTA DE DOAÇÕES--------------------')
        print('\n 0- Cadastrar uma nova doação')
        if len(dadosGlobais.doacoes) == 0: print('\n Não há nenhuma doação cadastrada no sistema.' + '') 
        else:
            for i in range(len(dadosGlobais.doacoes)): print(f' {i+1}- {dadosGlobais.doacoes[i].data[0]}/{dadosGlobais.doacoes[i].data[1]}/{dadosGlobais.doacoes[i].data[2]} {dadosGlobais.doacoes[i].pessoa.nome} ({dadosGlobais.doacoes[i].pessoa.cpf}) doou {dadosGlobais.doacoes[i].animal.nome} ({dadosGlobais.doacoes[i].animal.id})')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('---------------------------------------------------------------------')
        escolha = self.__tela.validaInput(len(dadosGlobais.doacoes))

        if escolha == 'X': return
        if escolha == 0: self.cadastrarDoacao(); return

        backupDoacao = copy.deepcopy(dadosGlobais.doacoes[escolha-1])
        print('\n'*100 + '--------------------ALTERAR CADASTRO--------------------')
        print('\n 0- Excluir Cadastro')
        print(f' 1- Doador: {dadosGlobais.doacoes[escolha-1].pessoa.nome} ({dadosGlobais.doacoes[escolha-1].pessoa.cpf})')
        print(f' 2- Animal Doado: {dadosGlobais.doacoes[escolha-1].animal.nome} ({dadosGlobais.doacoes[escolha-1].animal.id})')
        print(f' 3- Motivo: {dadosGlobais.doacoes[escolha-1].motivo}')
        print(f' 4- Data: {dadosGlobais.doacoes[escolha-1].data[0]}/{dadosGlobais.doacoes[escolha-1].data[1]}/{dadosGlobais.doacoes[escolha-1].data[2]}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('--------------------------------------------------------')
        dado = self.__tela.validaInput(4)
        if dado == 'X': return

        if dado == 0:
            print('\n'*100 + '--------------------EXCLUIR CADASTRO--------------------')
            print(f'\n Doador: {dadosGlobais.doacoes[escolha-1].pessoa.nome} ({dadosGlobais.doacoes[escolha-1].pessoa.cpf})')
            print(f' Animal Doado: {dadosGlobais.doacoes[escolha-1].animal.nome} ({dadosGlobais.doacoes[escolha-1].animal.id})')
            print(f' Motivo: {dadosGlobais.doacoes[escolha-1].motivo}')
            print(f' Data: {dadosGlobais.doacoes[escolha-1].data[0]}/{dadosGlobais.doacoes[escolha-1].data[1]}/{dadosGlobais.doacoes[escolha-1].data[2]}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('--------------------------------------------------------')
            while True:
                try:
                    confirma = str(input('\n Digite S para confirmar a exclusäo: ')).capitalize()
                    if confirma == 'X': return
                    if confirma != 'S': raise ValueError
                except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
                else: dadosGlobais.doacoes.pop(escolha-1); return

        if dado == 1:
            self.__controlador_pessoa.listarPessoa('Digite o número da pessoa que doou o animal. \n')
            novoDado = self.__tela.validaInput(len(dadosGlobais.pessoas))
            if novoDado == 'X': return
            if novoDado == 0:
                tamanhoAnterior = len(dadosGlobais.pessoas)
                self.__controlador_pessoa.cadastrarPessoa()
                if tamanhoAnterior < len(dadosGlobais.pessoas): novoDado = len(dadosGlobais.pessoas)
                else: return
            dadosGlobais.doacoes[novoDado-1].pessoa.endereco.animais += 1
            dadosGlobais.doacoes[novoDado-1].pessoa = dadosGlobais.pessoas[novoDado-1]

        if dado == 2:
            tamanhoAnterior = len(dadosGlobais.animais)
            self.__controlador_animal.cadastrarAnimal()
            if tamanhoAnterior == len(dadosGlobais.animais): return
            novoDado = dadosGlobais.animais[-1]

            dadosGlobais.doacoes[escolha-1].animal = novoDado

        if dado == 3:
            novoDado = str(input('\n Digite o motivo: ')).capitalize()
            if novoDado == 'X': return
            dadosGlobais.doacoes[escolha-1].motivo = novoDado

        if dado == 4:
            while True:
                novoDado = str(input('\n Digite S se a doação foi hoje ou N se foi em outro dia: ')).capitalize()
                if novoDado != 'S' and novoDado != 'N' and novoDado != 'X': print(' Valor inválido, por favor tente novamente')
                else: break
            if novoDado == 'X': return
            if novoDado == 'S':
                dia = datetime.now().day
                if dia < 10: dia = '0' + str(dia)
                dia = str(dia)

                mes = datetime.now().month
                if mes < 10: mes = '0' + str(mes)
                mes = str(mes)

                ano = str(datetime.now().year)

            if novoDado == 'N':
                while True:
                    try:
                        dia = str(self.__tela.validaInput(31, 'Digite o dia da aplicação da vacina', 1))
                        if dia == 'X': return dia
                        if len(dia) == 1: dia = "0" + dia

                        mes = str(self.__tela.validaInput(12, 'Digite o mês da aplicação da vacina', 1))
                        if mes == 'X': return mes
                        if len(mes) == 1: mes = "0" + mes

                        while True:
                            try:
                                ano = str(input('\n Digite o ano da aplicação da vacina: '))
                                if ano.capitalize() == 'X': return ano
                                if not ano.isdigit() or len(ano) != 4: raise ValueError
                            except Exception: print(' Valor inválido, por favor digite novamente')
                            else: break
                        
                        data = date(int(ano), int(mes), int(dia))

                        if (int(mes) == 2 and int(dia) == 29) and not (data.isocalendar()[1] == 9): raise ValueError

                        if datetime.now().year < data.year or (datetime.now().year == data.year and datetime.now().month < data.month) or (datetime.now().year == data.year and datetime.now().month == data.month and datetime.now().day < data.day):
                            raise ValueError

                    except Exception: input('\n Data inválida, por favor clique ENTER para tentar novamente ')
                    else: break

            novoDado = [dia, mes, ano]

            dadosGlobais.doacoes[escolha-1].data = novoDado

        print('\n'*100 + '--------------------ALTERAR CADASTRO--------------------')
        print(f'\n Doador: {dadosGlobais.doacoes[escolha-1].pessoa.nome} ({dadosGlobais.doacoes[escolha-1].pessoa.cpf})')
        print(f' Animal Doado: {dadosGlobais.doacoes[escolha-1].animal.nome} ({dadosGlobais.doacoes[escolha-1].animal.id})')
        print(f' Motivo: {dadosGlobais.doacoes[escolha-1].motivo}')
        print(f' Data: {dadosGlobais.doacoes[escolha-1].data[0]}/{dadosGlobais.doacoes[escolha-1].data[1]}/{dadosGlobais.doacoes[escolha-1].data[2]}')
        print('\n'*2 + ' Digite X para cancelar as alterações.')
        print('--------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar: ')).capitalize()
                if confirma == 'X': dadosGlobais.doacoes[escolha-1] = backupDoacao; return
                if confirma != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break