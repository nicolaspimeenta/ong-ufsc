import copy
from limite.tela_animal import TelaAnimal
from controle.controlador_pessoa import ControladorPessoa
from entidade.vacina import Vacina
from entidade import dadosGlobais
from entidade.cachorro import Cachorro
from entidade.gato import Gato

class ControladorAnimal:
    def __init__(self):
        self.controladorPessoa = ControladorPessoa()
        self.tela = TelaAnimal()

    def iniciar(self):
        while True:
            self.tela.abreTela()
            escolha = self.tela.validaInput(min=1, max=3)
            if escolha == 'X': return
            if escolha == 1: self.cadastrarAnimal()
            if escolha == 2: self.gerenciarAnimal()
            if escolha == 3: self.aplicarVacina()

    def listarAnimal(self, msg = ' ', adocao = False, cachorroGrande = False):
        if adocao:
            print('\n'*100 + '--------------------LISTA DE ANIMAIS ADOTÁVEIS--------------------')
            print(f' {msg}')
            print(' 0- Cadastrar um novo animal')
            if len(dadosGlobais.animais) == 0: print('\n Não há nenhum animal cadastrado no sistema.')
            else:
                listaAdotaveis = []
                for animal in dadosGlobais.animais:
                    if self.validaAdocao(animal, cachorroGrande): listaAdotaveis.append(animal)
                if len(listaAdotaveis) == 0: print(' Nenhum animal cadastrado na ONG está em condições de ser adotado.')
                for i in range(len(listaAdotaveis)):
                    margem = ' '*(10 - len(listaAdotaveis[i].tipo))
                    print(f' {i+1}- {listaAdotaveis[i].tipo} {margem} | {listaAdotaveis[i].nome}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('---------------------------------------------------------------------')
            return listaAdotaveis
            
        if not adocao:
            print('\n'*100 + '--------------------LISTA DE ANIMAIS CADASTRADOS--------------------')
            print(f' {msg}')
            print(' 0- Cadastrar um novo animal')
            if len(dadosGlobais.animais) == 0: print('\n Não há nenhum animal cadastrado no sistema.') 
            else:
                for i in range(len(dadosGlobais.animais)): 
                    margem = ' '*(10 - len(dadosGlobais.animais[i].tipo))
                    print(f' {i+1}- {dadosGlobais.animais[i].tipo} {margem} | {dadosGlobais.animais[i].nome}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('---------------------------------------------------------------------')

    def cadastrarAnimal(self):
        print('\n'*100 + '--------------------CADASTRO DE ANIMAL--------------------')
        print('\n Espécie | Nome | Raça')
        print('\n 1- Cachorro')
        print(' 2- Gato')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        tipo = self.tela.validaInput(max=2)
        if tipo == 'X': return
        if tipo == 1:
            print('\n'*100 + '--------------------TAMANHO DO CACHORRO--------------------')
            print('\n 1- Pequeno')
            print(' 2- Médio')
            print(' 3- Grande')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('----------------------------------------------------------')
            tamanho = self.tela.validaInput(min=1, max=3, msg='Digite o número da opção referente ao tamanho do cachorro')
            if tamanho == 'X': return
            if tamanho == 1: tamanho = 'Pequeno'
            if tamanho == 2: tamanho = 'Médio'
            if tamanho == 3: tamanho = 'Grande'
            tipo = 'Cachorro'
        if tipo == 2: tipo = 'Gato'

        print('\n'*100 + '--------------------CADASTRO DE ANIMAL--------------------')
        print(f'\n {tipo} | Nome | Raça')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        nome = str(input('\n Digite o Nome: ')).title()
        if nome == 'X': return

        print('\n'*100 + '--------------------CADASTRO DE ANIMAL--------------------')
        print(f'\n {tipo} | {nome} | Raça')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        raca = str(input('\n Digite a Raça: ')).title()
        if raca == 'X': return

        print('\n'*100 + '--------------------CADASTRO DE ANIMAL--------------------')
        print(f'\n {tipo} | {nome} | {raca}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar o cadastro: ')).capitalize()
                if confirma == 'X': return
                if confirma != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break

        if tipo == 'Cachorro': dadosGlobais.saveAnimal(Cachorro(len(dadosGlobais.animais)+1, tipo, nome, raca, None, tamanho))
        if tipo == 'Gato': dadosGlobais.saveAnimal(Gato(len(dadosGlobais.animais)+1, tipo, nome, raca, None))

        print('\n'*100 + '--------------------CADASTRO DE ANIMAL--------------------')
        print(f'\n {tipo} | {nome} | {raca}')
        print('\n'*2 + ' Cadastro realizado com sucesso.')
        print('----------------------------------------------------------')
        input('\n Clique ENTER para retornar: ')


    def gerenciarAnimal(self):
        self.listarAnimal()

        escolha = self.tela.validaInput(max=len(dadosGlobais.animais), msg='Digite o número do cadastro que deseja alterar ou excluir')

        if escolha == 'X': return
        if escolha == 0: self.cadastrarAnimal(); return

        backupAnimal = copy.deepcopy(dadosGlobais.animais[escolha-1])
        print('\n'*100 + '--------------------ALTERAR CADASTRO--------------------')
        print('\n 0- Excluir Cadastro')
        print(f' 1- Nome: {dadosGlobais.animais[escolha-1].nome}')
        print(f' 2- Raça: {dadosGlobais.animais[escolha-1].raca}')
        print(f' 3- Vacinas: {len(dadosGlobais.animais[escolha-1].vacinas)}')
        if dadosGlobais.animais[escolha-1].dono: print(f' 4- Dono: {dadosGlobais.animais[escolha-1].dono.cpf} | {dadosGlobais.animais[escolha-1].dono.nome}')
        if not dadosGlobais.animais[escolha-1].dono: print(f' 4- Dono: Sem dono')
        if dadosGlobais.animais[escolha-1].tipo == 'Cachorro': print(f' 5- Tamanho: {dadosGlobais.animais[escolha-1].tamanho}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('--------------------------------------------------------')
        while True:
            try:
                dado = str(input('\n Digite o número da opção desejada: '))
                if dado.capitalize() == 'X': return
                dado = int(dado)
                if dado < 0 or dado > 5 or (dado == 5 and dadosGlobais.animais[escolha-1].tipo == 'Gato'): raise ValueError
            except Exception: print(' Valor inválido, por favor digite novamente')
            else: break

        if dado == 0:
            print('\n'*100 + '--------------------EXCLUIR CADASTRO--------------------')
            print(f'\n Nome: {dadosGlobais.animais[escolha-1].nome}')
            print(f' Raça: {dadosGlobais.animais[escolha-1].raca}')
            print(f' Vacinas: {len(dadosGlobais.animais[escolha-1].vacinas)}')
            if dadosGlobais.animais[escolha-1].dono: print(f' Dono: {dadosGlobais.animais[escolha-1].dono.cpf} | {dadosGlobais.animais[escolha-1].dono.nome}')
            if not dadosGlobais.animais[escolha-1].dono: print(f' Dono: Sem dono')
            if dadosGlobais.animais[escolha-1].tipo == 'Cachorro': print(f' 5- Tamanho: {dadosGlobais.animais[escolha-1].tamanho}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('--------------------------------------------------------')
            while True:
                try:
                    confirma = str(input('\n Digite S para confirmar a exclusäo: ')).capitalize()
                    if confirma == 'X': return
                    if confirma != 'S': raise ValueError
                except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
                else: dadosGlobais.animais.pop(escolha-1); return

        if dado == 1: 
            novoDado = str(input('\n Digite o Nome: ')).capitalize()
            if novoDado == 'X': return
            dadosGlobais.animais[escolha-1].nome = novoDado

        if dado == 2:
            novoDado = str(input('\n Digite a Raça: ')).capitalize()
            if novoDado == 'X': return
            dadosGlobais.animais[escolha-1].raca = novoDado

        if dado == 3:
            print('\n'*100 + f'--------------------VACINAS DE {dadosGlobais.animais[escolha-1].nome}--------------------')
            print('\n 0- Adicionar Vacina')
            for i in range(len(dadosGlobais.animais[escolha-1].vacinas)): print(f' {i+1}- {dadosGlobais.animais[escolha-1].vacinas[i].tipo} | {dadosGlobais.animais[escolha-1].vacinas[i].data.strftime("%d")}/{dadosGlobais.animais[escolha-1].vacinas[i].data.strftime("%m")}/{dadosGlobais.animais[escolha-1].vacinas[i].data.strftime("%Y")}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('--------------------------------------------------------')
            vacina = self.tela.validaInput(max=len(dadosGlobais.animais[escolha-1].vacinas))
            if vacina == 'X': return 'X'
            
            if vacina == 0: self.aplicarVacina(dadosGlobais.animais[escolha-1].id); return

            print('\n'*100 + f'--------------------VACINAS DE {dadosGlobais.animais[escolha-1].nome}--------------------')
            print(f'\n 1- {dadosGlobais.animais[escolha-1].vacinas[vacina-1].tipo}')
            print(f' 2- {dadosGlobais.animais[escolha-1].vacinas[vacina-1].data.strftime("%d")}/{dadosGlobais.animais[escolha-1].vacinas[vacina-1].data.strftime("%m")}/{dadosGlobais.animais[escolha-1].vacinas[vacina-1].data.strftime("%Y")}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('--------------------------------------------------------')
            dado = self.tela.validaInput(min=1, max=2)

            if dado == 1: 
                novoDado = str(input('\n Digite o tipo da vacina: ')).title()
                if novoDado == 'X': return
                dadosGlobais.animais[escolha-1].vacinas[vacina-1].tipo = novoDado

            if dado == 2:
                novoDado = self.tela.validaData(True)
                if novoDado == 'X': return

                dadosGlobais.animais[escolha-1].vacinas[vacina-1].data = novoDado

        if dado == 4:
            print('\n 1- Ninguém é dono do animal')
            if len(dadosGlobais.pessoas) > 0: print(' 2- Escolher o dono na lista de pessoas cadastradas')
            while True:
                try:
                    novoDado = str(input('\n Digite o número da opção referente ao dono do animal: '))
                    if novoDado.capitalize() == 'X': return
                    novoDado = int(novoDado)
                    if novoDado < 1 or novoDado > 2 or (novoDado == 2 and len(dadosGlobais.pessoas) == 0): raise ValueError
                except Exception: print(' Valor inválido, por favor digite novamente')
                else: break

            if novoDado == 1: novoDado = None

            if novoDado == 2:
                self.controladorPessoa.listarPessoa()
                novoDado = self.tela.validaInput(max=len(dadosGlobais.pessoas))
                if novoDado == 'X': return
                if novoDado == 0: self.controladorPessoa.cadastrarPessoa(); novoDado = dadosGlobais.pessoas[-1]
                novoDado = dadosGlobais.pessoas[novoDado-1]

            dadosGlobais.animais[escolha-1].dono = novoDado

        if dado == 5:
            print('\n'*100 + '--------------------TAMANHO DO CACHORRO--------------------')
            print('\n 1- Pequeno')
            print(' 2- Médio')
            print(' 3- Grande')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('----------------------------------------------------------')
            novoDado = self.tela.validaInput(min=1, max=3, msg='Digite o número da opção referente ao tamanho do cachorro')
            if novoDado == 'X': return
            if novoDado == 1: novoDado = 'Pequeno'
            if novoDado == 2: novoDado = 'Médio'
            if novoDado == 3: novoDado = 'Grande'

            dadosGlobais.animais[escolha-1].tamanho = novoDado


        print('\n'*100 + '--------------------ALTERAR CADASTRO--------------------')
        print(f'\n Nome: {dadosGlobais.animais[escolha-1].nome}')
        print(f' Raça: {dadosGlobais.animais[escolha-1].raca}')
        print(f' Vacinas: {len(dadosGlobais.animais[escolha-1].vacinas)}')
        if dadosGlobais.animais[escolha-1].dono: print(f' Dono: {dadosGlobais.animais[escolha-1].dono.cpf} | {dadosGlobais.animais[escolha-1].dono.nome}')
        if not dadosGlobais.animais[escolha-1].dono: print(f' Dono: Sem Dono')
        if dadosGlobais.animais[escolha-1].tipo == 'Cachorro': print(f' 5- Tamanho: {dadosGlobais.animais[escolha-1].tamanho}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('--------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar: ')).capitalize()
                if confirma == 'X': dadosGlobais.animais[escolha-1] = backupAnimal; return
                if confirma != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break

    def aplicarVacina(self, id = 0):
        if id != 0: animais = [id]
        else:
            animais = []
            while True:
                self.listarAnimal()
                print(f'\n {len(animais)} animal(is) escolhido(s)')
                escolha = self.tela.validaInput(max=len(dadosGlobais.animais), msg='Digite o número do animal para registrar uma vacina')
                if escolha == 'X': return
                if escolha == 0: self.cadastrarAnimal(); return
                if dadosGlobais.animais[escolha-1].id in animais: print(' Você já escolheu este animal, por favor escolha outro.'); continue
                animais.append(next(animal for animal in dadosGlobais.animais if animal.id == dadosGlobais.animais[escolha-1].id))
                if len(animais) == len(dadosGlobais.animais): break
                while True:
                    escolha = str(input(' Digite S para escolher mais um animal, digite * para selecionar todos ou N para finalizar a seleção: ')).capitalize()
                    if escolha != 'S' and escolha != 'N' and escolha != 'X' and escolha != '*': print(' Valor inválido, por favor tente novamente')
                    else: break
                if escolha == 'S': continue
                if escolha == 'N': break
                if escolha == 'X': return
                if escolha == '*': animais.extend(animal for animal in dadosGlobais.animais if animal not in animais); break

        print('\n'*100 + '--------------------APLICAR VACINA--------------------')
        print(f'\n Tipo | 00/00/00 | Aplicação em {len(animais)} Animal(is)')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        tipo = str(input('\n Digite o Tipo da Vacina aplicada: ')).title()
        if tipo == 'X': return

        print('\n'*100 + '--------------------APLICAR VACINA--------------------')
        print(f'\n {tipo} | 00/00/00 | Aplicação em {len(animais)} Animal(is)')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        data = self.tela.validaData(True)
        if data == 'X': return

        print('\n'*100 + '--------------------APLICAR VACINA--------------------')
        print(f'\n {tipo} | {data.strftime("%d")}/{data.strftime("%m")}/{data.strftime("%Y")} | Aplicação em {len(animais)} Animal(is)')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar: ')).capitalize()
                if confirma == 'X': return
                if confirma != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break

        for animalRegistrado in dadosGlobais.animais:
            for vacinado in animais:
                if vacinado == animalRegistrado:
                    dadosGlobais.saveVacina(Vacina(tipo, data, animalRegistrado))
                    animalRegistrado.addVacina(dadosGlobais.vacinas[-1])
        return
            
    def validaAdocao(self, animal, cachorroGrande):
        if cachorroGrande:
            if animal.tipo == 'Cachorro':
                if animal.tamanho == 'Grande': return False
        vacinasEncontradas = []
        for vacinaNecessaria in ['Hepatite Infecciosa', 'Leptospirose', 'Raiva']:
            for vacina in animal.vacinas:
                if vacina.tipo == vacinaNecessaria: vacinasEncontradas.append(vacina.tipo)
        if vacinasEncontradas == ['Hepatite Infecciosa', 'Leptospirose', 'Raiva'] and animal.dono == None: return True
        return False


