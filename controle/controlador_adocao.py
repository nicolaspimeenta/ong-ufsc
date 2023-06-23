import copy
from limite.tela_adocao import TelaAdocao
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_animal import ControladorAnimal
from entidade.adocao import Adocao
from entidade import dadosGlobais

class ControladorAdocao:
    def __init__(self):
        self.controladorPessoa = ControladorPessoa()
        self.controladorAnimal = ControladorAnimal()
        self.tela = TelaAdocao()
    
    def iniciar(self):
        while True:
            escolha = int(self.tela.abreTela())
            if escolha == 0: return
            if escolha == 1: self.cadastrarAdocao()
            if escolha == 2: self.gerenciarDoacao()


    def cadastrarAdocao(self):
        print('\n'*100 + '--------------------ADOÇÃO DE ANIMAL--------------------')
        print('\n Animal | Adotante | Assinatura | Data')
        print('----------------------------------------------------------')
        input(' Clique ENTER para registrar o Animal')

        listaAdotaveis = self.controladorAnimal.listarAnimal('Todos animais da lista foram vacinados contra: Raiva, Leptospirose e Hepatite Infecciosa. \n', True)
        escolha = self.tela.validaInput(len(listaAdotaveis), 'Digite o número do animal que será adotado')
        if escolha == 'X': return
        if escolha == 0: self.controladorAnimal.cadastrarAnimal(); return

        animal = listaAdotaveis[escolha-1]

        print('\n'*100 + '--------------------ADOÇÃO DE ANIMAL--------------------')
        print(f'\n Animal: {animal.nome} ({animal.id}) | Adotante | Data')
        print('----------------------------------------------------------')
        input(' Clique ENTER para registrar o Adotante')

        listaAdotantes = self.controladorPessoa.listarPessoa('Todas as pessoas da lista nunca doaram um animal para essa ONG. \n', True)

        if animal.tipo == 'Cachorro' and animal.tamanho == 'Grande':
            listaAdotantes = self.controladorPessoa.listarPessoa('Todas as pessoas da lista nunca doaram um animal para essa ONG. \n', True, True)
        
        escolha = self.tela.validaInput(len(listaAdotantes), 'Digite o número do adotante')
        if escolha == 'X': return
        if escolha == 0: self.controladorPessoa.cadastrarPessoa(); return

        pessoa = listaAdotantes[escolha-1]

        print('\n'*100 + '--------------------ADOÇÃO DE ANIMAL--------------------')
        print(f'\n Animal: {animal.nome} ({animal.id}) | Adotante: {pessoa.nome} ({pessoa.cpf}) | Data')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S se o adotante assinou o termo de responsabilidade: ')).capitalize()
                if confirma == 'X': return
                if confirma != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break

        print('\n'*100 + '--------------------ADOÇÃO DE ANIMAL--------------------')
        print(f'\n Animal: {animal.nome} ({animal.id}) | Adotante: {pessoa.nome} ({pessoa.cpf}) | Data')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        data = self.tela.validaData(True)
        if data == 'X': return

        print('\n'*100 + '--------------------ADOÇÃO DE ANIMAL--------------------')
        print(f'\n Animal: {animal.nome} ({animal.id}) | Adotante: {pessoa.nome} ({pessoa.cpf}) | Data: {data.strftime("%d")}/{data.strftime("%m")}/{data.strftime("%Y")}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar: ')).capitalize()
                if confirma == 'X': return
                if confirma != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break

        print('\n'*100 + '--------------------ADOÇÃO DE ANIMAL--------------------')
        print(f'\n Animal: {animal.nome} ({animal.id}) | Adotante: {pessoa.nome} ({pessoa.cpf}) | Data: {data.strftime("%d")}/{data.strftime("%m")}/{data.strftime("%Y")}')
        print('\n'*2 + ' Adoção realizada com sucesso.')
        print('----------------------------------------------------------')
        input(' Clique ENTER para continuar')

        animal.dono = pessoa
        pessoa.endereco.animais += 1
        dadosGlobais.saveAdocao(Adocao(pessoa, animal, data, True))

    def gerenciarDoacao(self):
        print('\n'*100 + '--------------------LISTA DE ADOÇÕES--------------------')
        print('\n 0- Cadastrar uma nova adoção')
        if len(dadosGlobais.adocoes) == 0: print(' Não há nenhuma adoção cadastrada no sistema.' + '') 
        else:
            for i in range(len(dadosGlobais.adocoes)): print(f' {i+1}- {dadosGlobais.adocoes[i].data.strftime("%d")}/{dadosGlobais.adocoes[i].data.strftime("%m")}/{dadosGlobais.adocoes[i].data.strftime("%Y")} {dadosGlobais.adocoes[i].pessoa.nome} ({dadosGlobais.adocoes[i].pessoa.cpf}) adotou {dadosGlobais.adocoes[i].animal.nome} ({dadosGlobais.adocoes[i].animal.id})')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('---------------------------------------------------------------------')
        escolha = self.tela.validaInput(len(dadosGlobais.adocoes))

        if escolha == 'X': return
        if escolha == 0: self.cadastrarDoacao(); return

        backupAdocao = copy.deepcopy(dadosGlobais.adocoes[escolha-1])
        print('\n'*100 + '--------------------ALTERAR CADASTRO--------------------')
        print('\n 0- Excluir Cadastro')
        print(f' 1- Adotante: {dadosGlobais.adocoes[escolha-1].pessoa.nome} ({dadosGlobais.adocoes[escolha-1].pessoa.cpf})')
        print(f' 2- Animal Adotado: {dadosGlobais.adocoes[escolha-1].animal.nome} ({dadosGlobais.adocoes[escolha-1].animal.id})')
        print(f' 3- Data: {dadosGlobais.adocoes[escolha-1].data.strftime("%d")}/{dadosGlobais.adocoes[escolha-1].data.strftime("%m")}/{dadosGlobais.adocoes[escolha-1].data.strftime("%Y")}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('--------------------------------------------------------')
        dado = self.tela.validaInput(3)
        if dado == 'X': return

        if dado == 0:
            print('\n'*100 + '--------------------EXCLUIR CADASTRO--------------------')
            print(f'\n Adotante: {dadosGlobais.adocoes[escolha-1].pessoa.nome} ({dadosGlobais.adocoes[escolha-1].pessoa.cpf})')
            print(f' Animal Adotado: {dadosGlobais.adocoes[escolha-1].animal.nome} ({dadosGlobais.adocoes[escolha-1].animal.id})')
            print(f' Data: {dadosGlobais.adocoes[escolha-1].data.strftime("%d")}/{dadosGlobais.adocoes[escolha-1].data.strftime("%m")}/{dadosGlobais.adocoes[escolha-1].data.strftime("%Y")}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('--------------------------------------------------------')
            while True:
                try:
                    confirma = str(input('\n Digite S para confirmar a exclusäo: ')).capitalize()
                    if confirma == 'X': return
                    if confirma != 'S': raise ValueError
                except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
                else: 
                    dadosGlobais.adocoes[escolha-1].animal.dono = None
                    dadosGlobais.adocoes[escolha-1].pessoa.endereco.animais -= 1
                    dadosGlobais.adocoes.remove(dadosGlobais.adocoes[escolha-1])
                    return

        if dado == 1:
            dadosGlobais.adocoes[escolha-1].pessoa.endereco.animais -= 1
            listaAdotantes = self.controladorPessoa.listarPessoa('Todas as pessoas da lista nunca doaram um animal para essa ONG. \n', True)

            if dadosGlobais.adocoes[escolha-1].animal.tipo == 'Cachorro' and dadosGlobais.adocoes[escolha-1].animal.tamanho == 'Grande':
                listaAdotantes = self.controladorPessoa.listarPessoa('Todas as pessoas da lista nunca doaram um animal para essa ONG. \n', True, True)
            
            novoDado = self.tela.validaInput(len(listaAdotantes), 'Digite o número do adotante')
            if novoDado == 'X': return
            if novoDado == 0: self.controladorPessoa.cadastrarPessoa(); return

            dadosGlobais.adocoes[escolha-1].pessoa = listaAdotantes[novoDado-1]
            dadosGlobais.adocoes[escolha-1].pessoa.endereco.animais += 1

        if dado == 2: 
            if dadosGlobais.adocoes[escolha-1].pessoa.endereco.tipo == 'Apartamento' and dadosGlobais.adocoes[escolha-1].pessoa.endereco.tamanho == 'Pequeno':
                listaAdotaveis = self.controladorAnimal.listarAnimal('Todos animais da lista foram vacinados contra: Raiva, Leptospirose e Hepatite Infecciosa. \n', True, True)
            novoDado = self.tela.validaInput(len(listaAdotaveis), 'Digite o número do animal que será adotado')
            if novoDado == 'X': return
            if novoDado == 0: self.controladorAnimal.cadastrarAnimal(); return

            dadosGlobais.adocoes[escolha-1].animal = listaAdotaveis[novoDado-1]

        if dado == 3:
            novoDado = self.tela.validaData(True)
            if novoDado == 'X': return

            dadosGlobais.adocoes[escolha-1].data = novoDado

        print('\n'*100 + '--------------------ALTERAR CADASTRO--------------------')
        print(f'\n Adotante: {dadosGlobais.adocoes[escolha-1].pessoa.nome} ({dadosGlobais.adocoes[escolha-1].pessoa.cpf})')
        print(f' Animal Adotado: {dadosGlobais.adocoes[escolha-1].animal.nome} ({dadosGlobais.adocoes[escolha-1].animal.id})')
        print(f' Data: {dadosGlobais.adocoes[escolha-1].data.strftime("%d")}/{dadosGlobais.adocoes[escolha-1].data.strftime("%m")}/{dadosGlobais.adocoes[escolha-1].data.strftime("%Y")}')
        print('\n'*2 + ' Digite X para cancelar as alterações.')
        print('--------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar: ')).capitalize()
                if confirma == 'X': dadosGlobais.adocoes[escolha-1] = backupAdocao; return
                if confirma != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break