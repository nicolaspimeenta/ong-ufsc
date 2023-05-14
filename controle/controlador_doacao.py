import copy
from limite.tela_doacao import TelaDoacao
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_animal import ControladorAnimal
from entidade import dadosGlobais
from entidade.doacao import Doacao

class ControladorDoacao:
    def __init__(self):
        self.controladorPessoa = ControladorPessoa()
        self.controladorAnimal = ControladorAnimal()
        self.tela = TelaDoacao()
    
    def iniciar(self):
        while True:
            self.tela.abreTela()
            escolha = self.tela.validaInput(2, 'Digite o número da opção desejada', 1)
            if escolha == 'X': return
            if escolha == 1: self.cadastrarDoacao()
            if escolha == 2: self.gerenciarDoacao()


    def cadastrarDoacao(self):
        print('\n'*100 + '--------------------DOAÇÃO DE ANIMAL--------------------')
        print('\n Doador | Animal | Motivo | Data')
        print('----------------------------------------------------------')
        input('Clique ENTER para registrar o Doador')

        self.controladorPessoa.listarPessoa('Digite o número da pessoa que irá doar o animal. \n')
        escolha = self.tela.validaInput(len(dadosGlobais.pessoas))
        if escolha == 'X': return
        if escolha == 0: 
            tamanhoAnterior = len(dadosGlobais.pessoas)
            self.controladorPessoa.cadastrarPessoa()
            if tamanhoAnterior < len(dadosGlobais.pessoas): escolha = len(dadosGlobais.pessoas)
            else: return
        if dadosGlobais.pessoas[escolha-1].endereco.animais > 0: dadosGlobais.pessoas[escolha-1].endereco.animais -= 1

        print('\n'*100 + '--------------------DOAÇÃO DE ANIMAL--------------------')
        print(f'\n Doador: {dadosGlobais.pessoas[escolha-1].nome} | Animal | Motivo | Data')
        print('----------------------------------------------------------')
        input('Clique ENTER para registrar o Animal')

        tamanhoAnterior = len(dadosGlobais.animais)
        self.controladorAnimal.cadastrarAnimal()
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
        data = self.tela.validaData(True)
        if data == 'X': return

        print('\n'*100 + '--------------------DOAÇÃO DE ANIMAL--------------------')
        print(f'\n Doador: {dadosGlobais.pessoas[escolha-1].nome} | Animal: {dadosGlobais.animais[-1].nome} | Motivo: {motivo} | Data: {data.strftime("%d")}/{data.strftime("%m")}/{data.strftime("%y")}')
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
        print(f'\n Doador: {dadosGlobais.pessoas[escolha-1].nome} | Animal: {dadosGlobais.animais[-1].nome} | Motivo: {motivo} | Data: {data.strftime("%d")}/{data.strftime("%m")}/{data.strftime("%y")}')
        print('\n'*2 + ' Doação realizada com sucesso.')
        print('----------------------------------------------------------')
        input('Clique ENTER para continuar')

        dadosGlobais.saveDoacao(Doacao(dadosGlobais.pessoas[escolha-1], dadosGlobais.animais[-1], data, motivo))

    def gerenciarDoacao(self):
        print('\n'*100 + '--------------------LISTA DE DOAÇÕES--------------------')
        print('\n 0- Cadastrar uma nova doação')
        if len(dadosGlobais.doacoes) == 0: print('\n Não há nenhuma doação cadastrada no sistema.' + '') 
        else:
            for i in range(len(dadosGlobais.doacoes)): print(f' {i+1}- {dadosGlobais.doacoes[i].data.strftime("%d")}/{dadosGlobais.doacoes[i].data.strftime("%m")}/{dadosGlobais.doacoes[i].data.strftime("%y")} {dadosGlobais.doacoes[i].pessoa.nome} ({dadosGlobais.doacoes[i].pessoa.cpf}) doou {dadosGlobais.doacoes[i].animal.nome} ({dadosGlobais.doacoes[i].animal.id})')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('---------------------------------------------------------------------')
        escolha = self.tela.validaInput(len(dadosGlobais.doacoes))

        if escolha == 'X': return
        if escolha == 0: self.cadastrarDoacao(); return

        backupDoacao = copy.deepcopy(dadosGlobais.doacoes[escolha-1])
        print('\n'*100 + '--------------------ALTERAR CADASTRO--------------------')
        print('\n 0- Excluir Cadastro')
        print(f' 1- Doador: {dadosGlobais.doacoes[escolha-1].pessoa.nome} ({dadosGlobais.doacoes[escolha-1].pessoa.cpf})')
        print(f' 2- Animal Doado: {dadosGlobais.doacoes[escolha-1].animal.nome} ({dadosGlobais.doacoes[escolha-1].animal.id})')
        print(f' 3- Motivo: {dadosGlobais.doacoes[escolha-1].motivo}')
        print(f' 4- Data: {dadosGlobais.doacoes[escolha-1].data.strftime("%d")}/{dadosGlobais.doacoes[escolha-1].data.strftime("%m")}/{dadosGlobais.doacoes[escolha-1].data.strftime("%y")}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('--------------------------------------------------------')
        dado = self.tela.validaInput(4)
        if dado == 'X': return

        if dado == 0:
            print('\n'*100 + '--------------------EXCLUIR CADASTRO--------------------')
            print(f'\n Doador: {dadosGlobais.doacoes[escolha-1].pessoa.nome} ({dadosGlobais.doacoes[escolha-1].pessoa.cpf})')
            print(f' Animal Doado: {dadosGlobais.doacoes[escolha-1].animal.nome} ({dadosGlobais.doacoes[escolha-1].animal.id})')
            print(f' Motivo: {dadosGlobais.doacoes[escolha-1].motivo}')
            print(f' Data: {dadosGlobais.doacoes[escolha-1].data.strftime("%d")}/{dadosGlobais.doacoes[escolha-1].data.strftime("%m")}/{dadosGlobais.doacoes[escolha-1].data.strftime("%y")}')
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
            self.controladorPessoa.listarPessoa('Digite o número da pessoa que doou o animal. \n')
            novoDado = self.tela.validaInput(len(dadosGlobais.pessoas))
            if novoDado == 'X': return
            if novoDado == 0:
                tamanhoAnterior = len(dadosGlobais.pessoas)
                self.controladorPessoa.cadastrarPessoa()
                if tamanhoAnterior < len(dadosGlobais.pessoas): novoDado = len(dadosGlobais.pessoas)
                else: return
            dadosGlobais.doacoes[novoDado-1].pessoa.endereco.animais += 1
            dadosGlobais.doacoes[novoDado-1].pessoa = dadosGlobais.pessoas[novoDado-1]

        if dado == 2:
            tamanhoAnterior = len(dadosGlobais.animais)
            self.controladorAnimal.cadastrarAnimal()
            if tamanhoAnterior == len(dadosGlobais.animais): return
            novoDado = dadosGlobais.animais[-1]

            dadosGlobais.doacoes[escolha-1].animal = novoDado

        if dado == 3:
            novoDado = str(input('\n Digite o motivo: ')).capitalize()
            if novoDado == 'X': return
            dadosGlobais.doacoes[escolha-1].motivo = novoDado

        if dado == 4:
            novoDado = self.tela.validaData(True)
            if novoDado == 'X': return

            dadosGlobais.doacoes[escolha-1].data = novoDado

        print('\n'*100 + '--------------------ALTERAR CADASTRO--------------------')
        print(f'\n Doador: {dadosGlobais.doacoes[escolha-1].pessoa.nome} ({dadosGlobais.doacoes[escolha-1].pessoa.cpf})')
        print(f' Animal Doado: {dadosGlobais.doacoes[escolha-1].animal.nome} ({dadosGlobais.doacoes[escolha-1].animal.id})')
        print(f' Motivo: {dadosGlobais.doacoes[escolha-1].motivo}')
        print(f' Data: {dadosGlobais.doacoes[escolha-1].data.strftime("%d")}/{dadosGlobais.doacoes[escolha-1].data.strftime("%m")}/{dadosGlobais.doacoes[escolha-1].data.strftime("%y")}')
        print('\n'*2 + ' Digite X para cancelar as alterações.')
        print('--------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar: ')).capitalize()
                if confirma == 'X': dadosGlobais.doacoes[escolha-1] = backupDoacao; return
                if confirma != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break