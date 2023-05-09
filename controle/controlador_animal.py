import copy
from limite.tela_animal import TelaAnimal
from entidade import Cachorro, Gato, Vacina, dadosGlobais
from datetime import date, datetime

class ControladorAnimal:
    def __init__(self):
        self.__tela = TelaAnimal()

    @property
    def tela(self):
        return self.__tela

    def iniciar(self):
        while True:
            self.tela.abreTela()
            escolha = self.tela.validaInput(4)
            if escolha == 1: return
            if escolha == 2: self.cadastrarAnimal()
            if escolha == 3: self.alterarAnimal()
            if escolha == 4: self.aplicarVacinas()

    def cadastrarAnimal(self):
        print('\n'*100 + '--------------------CADASTRO DE ANIMAL--------------------')
        print('\n Espécie | Nome | Raça | Dono')
        print('\n 1- Cachorro')
        print(' 2- Gato')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        while True:
            try:
                tipo = str(input('\n Digite o número da opção referente a espécie do animal: '))
                if tipo.capitalize() == 'X': return
                tipo = int(escolha)
                if tipo < 1 or tipo > 2: raise ValueError
            except Exception: print(' Valor inválido, por favor digite novamente')
            else: 
                if tipo == 1: 
                    print('\n'*100 + '--------------------TAMANHO DO CACHORRO--------------------')
                    print('\n 1- Pequeno')
                    print(' 2- Médio')
                    print(' 3- Grande')
                    print('\n'*2 + ' Digite X para cancelar a operação.')
                    print('----------------------------------------------------------')
                    while True:
                        try:
                            tamanho = str(input('\n Digite o número da opção referente ao tamanho do cachorro: '))
                            if tamanho.capitalize() == 'X': return
                            tamanho = int(tamanho)
                            if tamanho < 1 or tamanho > 3: raise ValueError
                        except Exception: print(' Valor inválido, por favor digite novamente')
                        else: 
                            if tamanho == 1: tamanho = 'Pequeno'
                            if tamanho == 2: tamanho = 'Médio'
                            if tamanho == 3: tamanho = 'Grande'
                            break
                    tipo = 'Cachorro'
                if tipo == 2: tipo = 'Gato'
                break

        print('\n'*100 + '--------------------CADASTRO DE ANIMAL--------------------')
        print(f'\n {tipo} | Nome | Raça | Dono')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        nome = str(input('\n Digite o Nome: '))
        if nome.capitalize() == 'X': return

        print('\n'*100 + '--------------------CADASTRO DE ANIMAL--------------------')
        print(f'\n {tipo} | {nome} | Raça | Dono')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        raca = str(input('\n Digite a Raça: '))
        if raca.capitalize() == 'X': return

        print('\n'*100 + '--------------------CADASTRO DE ANIMAL--------------------')
        print(f'\n {tipo} | {nome} | {raca} | Dono')
        print('\n 1- Ninguém é dono do animal')
        if len(dadosGlobais.pessoas) > 0: print(' 2- Escolher o dono na lista de pessoas cadastradas')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        while True:
            try:
                escolha = str(input('\n Digite o número da opção referente ao dono do animal: '))
                if escolha.capitalize() == 'X': return
                escolha = int(escolha)
                if escolha < 1 or escolha > 2 or (escolha == 2 and len(dadosGlobais.pessoas) == 0): raise ValueError
            except Exception: print(' Valor inválido, por favor digite novamente')
            else: break

        if escolha == 1: dono = None

        if escolha == 2:
            print('\n'*100 + '--------------------LISTAS DE PESSOAS CADASTRADAS--------------------')
            for i in range(len(dadosGlobais.pessoas)): print(f' {i+1}- {dadosGlobais.pessoas[i].nome} | {dadosGlobais.pessoas[i].cpf}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('---------------------------------------------------------------------')
            while True:
                try:
                    dono = str(input('\n Digite o número da pessoa que é dono do animal: '))
                    if dono.capitalize() == 'X': return
                    dono = int(escolha)
                    if dono < 1 or dono > len(dadosGlobais.pessoas): raise ValueError
                except Exception: print(' Valor inválido, por favor digite novamente')
                else: dono = dadosGlobais.pessoas[dono-1]; break


        print('\n'*100 + '--------------------CADASTRO DE ANIMAL--------------------')
        if dono: print(f'\n {tipo} | {nome} | {raca} | CPF do dono: {dono.cpf}')
        if not dono: print(f'\n {tipo} | {nome} | {raca} | Sem dono')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar o cadastro: '))
                if confirma.capitalize() == 'X': return
                if confirma.capitalize() != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break

        if tipo == 'Cachorro': dadosGlobais.saveAnimal(Cachorro(len(dadosGlobais.animais)+1, nome, raca, [], dono, tamanho))
        if tipo == 'Gato': dadosGlobais.saveAnimal(Gato(len(dadosGlobais.animais)+1, nome, raca, [], dono))

        print('\n'*100 + '--------------------CADASTRO DE ANIMAL--------------------')
        if dono: print(f'\n {tipo} | {nome} | {raca} | CPF do dono: {dono.cpf}')
        if not dono: print(f'\n {tipo} | {nome} | {raca} | Sem dono')
        print('\n'*2 + ' Cadastro realizado com sucesso.')
        print('----------------------------------------------------------')
        input('\n Clique ENTER para retornar: ')

    def alterarAnimal(self):
        print('\n'*100 + '--------------------LISTAS DE ANIMAIS CADASTRADOS--------------------')
        if len(dadosGlobais.animais) == 0: 
            print('\n Não há nenhum animal cadastrado no sistema.' + '') 
            print('---------------------------------------------------------------------')
            input('\n Clique ENTER para retornar: '); return
        
        print('\n 0- Cadastrar um novo animal')
        for i in range(len(dadosGlobais.animais)): print(f' {i+1}- {dadosGlobais.animais[i].tipo} | {dadosGlobais.animais[i].nome}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('---------------------------------------------------------------------')
        while True:
            try:
                escolha = str(input('\n Digite o número do cadastro para alterar ou excluir: '))
                if escolha.capitalize() == 'X': return
                escolha = int(escolha)
                if escolha < 0 or escolha > len(dadosGlobais.animais): raise ValueError
                if escolha == 0: self.cadastrarAnimal(); return
            except Exception: print(' Valor inválido, por favor digite novamente')
            else: break

        backupAnimal = copy.deepcopy(dadosGlobais.animais[escolha-1])
        print('\n'*100 + '--------------------ALTERAR CADASTRO--------------------')
        print('\n 0- Excluir Cadastro')
        print(f' 1- Nome: {dadosGlobais.animais[escolha-1].nome}')
        print(f' 2- Raça: {dadosGlobais.animais[escolha-1].raca}')
        print(f' 3- Vacinas: {dadosGlobais.animais[escolha-1].vacinas}')
        print(f' 4- Dono: {dadosGlobais.animais[escolha-1].dono.cpf} | {dadosGlobais.animais[escolha-1].dono.nome}')
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
            print(f' Dono: {dadosGlobais.animais[escolha-1].dono.cpf} | {dadosGlobais.animais[escolha-1].dono.nome}')
            if dadosGlobais.animais[escolha-1].tipo == 'Cachorro': print(f' 5- Tamanho: {dadosGlobais.animais[escolha-1].tamanho}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('--------------------------------------------------------')
            while True:
                try:
                    confirma = str(input('\n Digite S para confirmar a exclusäo: '))
                    if confirma.capitalize() == 'X': return
                    if confirma.capitalize() != 'S': raise ValueError
                except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
                else: dadosGlobais.animais.pop(escolha-1); return

        if dado == 1: 
            novoDADO = str(input('\n Digite o Nome: '))
            if novoDADO.capitalize() == 'X': return
            dadosGlobais.animais[escolha-1].nome = novoDADO

        if dado == 2:
            novoDADO = str(input('\n Digite a Raça: '))
            if novoDADO.capitalize() == 'X': return
            dadosGlobais.animais[escolha-1].raca = novoDADO

        if dado == 3:
            print('\n'*100 + f'--------------------VACINAS DE {dadosGlobais.animais[escolha-1].nome.capitalize()}--------------------')
            print('\n 0- Adicionar Vacina')
            for i in range(len(dadosGlobais.vacinas)): print(f' {i+1}- {dadosGlobais.vacinas[i].tipo} | {dadosGlobais.vacinas[i].data[0]}/{dadosGlobais.vacinas[i].data[1]}/{dadosGlobais.vacinas[i].data[2]}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('--------------------------------------------------------')
            while True:
                try:
                    vacina = str(input('\n Digite o número da vacina desejada: '))
                    if vacina.capitalize() == 'X': return
                    vacina = int(vacina)
                    if vacina < 0 or vacina > len(dadosGlobais.vacinas): raise ValueError
                except Exception: print(' Valor inválido, por favor digite novamente')
                else: break
            
            if vacina == 0: self.aplicarVacinas(dadosGlobais.animais[escolha-1].id); return
            # PAREI AQUI TA ERRADO DADOSGLOBAIS.VACINAS
            print('\n'*100 + f'--------------------VACINAS DE {dadosGlobais.animais[escolha-1].nome.capitalize()}--------------------')
            print(f'\n 1- {dadosGlobais.vacinas[vacina-1].tipo}') 
            print(f' 2- {dadosGlobais.vacinas[i].data[0]}/{dadosGlobais.vacinas[i].data[1]}/{dadosGlobais.vacinas[i].data[2]}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('--------------------------------------------------------')
            while True:
                try:
                    dado = str(input('\n Digite o número da opção desejada: '))
                    if dado.capitalize() == 'X': return
                    dado = int(dado)
                    if dado < 1 or dado > 2: raise ValueError
                except Exception: print(' Valor inválido, por favor digite novamente')
                else: break

                if dado == 1: novoDado = str(input('\n Digite o tipo da vacina: '));  

        if dado == 4:
            print('\n 1- Ninguém é dono do animal')
            if len(dadosGlobais.pessoas) > 0: print(' 2- Escolher o dono na lista de pessoas cadastradas')
            while True:
                try:
                    escolha = str(input('\n Digite o número da opção referente ao dono do animal: '))
                    if escolha.capitalize() == 'X': return
                    escolha = int(escolha)
                    if escolha < 1 or escolha > 2 or (escolha == 2 and len(dadosGlobais.pessoas) == 0): raise ValueError
                except Exception: print(' Valor inválido, por favor digite novamente')
                else: break

            if escolha == 1: novoDado = None

            if escolha == 2:
                print('\n'*100 + '--------------------LISTAS DE PESSOAS CADASTRADAS--------------------')
                for i in range(len(dadosGlobais.pessoas)): print(f' {i+1}- {dadosGlobais.pessoas[i].nome} | {dadosGlobais.pessoas[i].cpf}')
                print('\n'*2 + ' Digite X para cancelar a operação.')
                print('---------------------------------------------------------------------')
                while True:
                    try:
                        novoDado = str(input('\n Digite o número da pessoa que é dono do animal: '))
                        if novoDado.capitalize() == 'X': return
                        novoDado = int(escolha)
                        if novoDado < 1 or novoDado > len(dadosGlobais.pessoas): raise ValueError
                    except Exception: print(' Valor inválido, por favor digite novamente')
                    else: novoDado = dadosGlobais.pessoas[novoDado-1]; break

            dadosGlobais.animais[escolha-1].dono = novoDADO

        print('\n'*100 + '--------------------ALTERAR CADASTRO--------------------')
        print(f'\n Nome: {dadosGlobais.animais[escolha-1].nome}')
        print(f' Raça: {dadosGlobais.animais[escolha-1].raca}')
        print(f' Vacinas: {dadosGlobais.animais[escolha-1].vacinas}')
        print(f' Dono: {dadosGlobais.animais[escolha-1].dono.cpf} | {dadosGlobais.animais[escolha-1].dono.nome}')
        if dadosGlobais.animais[escolha-1].tipo == 'Cachorro': print(f' 5- Tamanho: {dadosGlobais.animais[escolha-1].tamanho}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('--------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar: '))
                if confirma.capitalize() == 'X': dadosGlobais.animais[escolha-1] = backupAnimal; return
                if confirma.capitalize() != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break

    def aplicarVacinas(self, id):
        if id == 0:
            animais = []
            print('\n'*100 + '--------------------LISTAS DE ANIMAIS CADASTRADOS--------------------')
            if len(dadosGlobais.animais) == 0:
                print('\n Não há nenhum animal cadastrado no sistema.') 
                print('---------------------------------------------------------------------')
                input('\n Clique ENTER para retornar: '); return
            
            print('\n 0- Cadastrar um novo animal')
            for i in range(len(dadosGlobais.animais)):
                for z in range(len(animais)): 
                    if animais[z] != dadosGlobais.animais[i].id:
                        print(f' {dadosGlobais.animais[i].id}- {dadosGlobais.animais[i].tipo} | {dadosGlobais.animais[i].nome}')
            print('\n'*2 + ' Digite X para cancelar a operação.')
            print('---------------------------------------------------------------------')
            while True:
                try:
                    escolha = str(input('\n Digite o número do animal para registrar uma vacina: '))
                    if escolha.capitalize() == 'X': return
                    escolha = int(escolha)
                    for j in range(len(animais)):
                        if escolha == animais[j]: raise ValueError
                    if escolha < 0 or escolha > len(dadosGlobais.animais): raise ValueError
                    if escolha == 0: self.cadastrarAnimal(); return
                except Exception: print(' Valor inválido, por favor digite novamente')
                else:
                    for n in range(len(dadosGlobais.animais)):
                        if dadosGlobais.animais[n].id == escolha: animais.append(dadosGlobais.animais[n].id)
                    escolha = str(input('\n Digite S para escolher mais um animal, digite * para selecionar todos ou N para finalizar a seleção: '))
                    if escolha.capitalize() == 'S': pass
                    if escolha.capitalize() == 'N': break
                    if escolha.capitalize() == 'X': return
                    if escolha.capitalize() == '*':
                        for i in range(len(dadosGlobais.animais)):
                            for z in range(len(animais)):
                                if animais[z] == dadosGlobais.animais[i].id: continue
                            animais.append(dadosGlobais.animais[i].id)
                        break

        if id != 0: animais = [id]

        print('\n'*100 + '--------------------APLICAR VACINA--------------------')
        print(f'\n Tipo | 00/00/00 | ID do(s) Animal(is): {animais}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        tipo = str(input('\n Digite o Tipo da Vacina aplicada: '))
        if tipo.capitalize() == 'X': return

        print('\n'*100 + '--------------------APLICAR VACINA--------------------')
        print(f'\n {tipo} | 00/00/00 | ID do(s) Animal(is): {animais}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        data = str(input('\n Digite S se a vacina será aplicada hoje ou N se foi aplicada em outro dia: '))
        if data.capitalize() == 'X': return
        if data.capitalize() == 'S':
            dia = datetime.now().day
            if dia < 10: dia = '0' + str(dia)
            dia = str(dia)

            mes = datetime.now().month
            if mes < 10: mes = '0' + str(mes)
            mes = str(mes)

            ano = str(datetime.now().year)

        if data.capitalize() == 'N':
            while True:
                try:
                    while True:
                        try:
                            dia = str(input('\n Digite o dia da aplicação da vacina: '))
                            if dia.capitalize() == 'X': return dia
                            if not 0 < int(dia) < 32: raise ValueError
                        except Exception: print(' Valor inválido, por favor digite novamente')
                        else: 
                            if len(dia) == 1: dia = "0" + dia
                            break

                    while True:
                        try:
                            mes = str(input('\n Digite o mês da aplicação da vacina: '))
                            if mes.capitalize() == 'X': return mes
                            if not 0 < int(mes) < 13: raise ValueError
                        except Exception: print(' Valor inválido, por favor digite novamente')
                        else:
                            if len(mes) == 1: mes = "0" + mes
                            break

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

        print('\n'*100 + '--------------------APLICAR VACINA--------------------')
        print(f'\n {tipo} | {data[0]}/{data[1]}/{data[2]} | ID do(s) Animal(is): {animais}')
        print('\n'*2 + ' Digite X para cancelar a operação.')
        print('----------------------------------------------------------')
        while True:
            try:
                confirma = str(input('\n Digite S para confirmar: '))
                if confirma.capitalize() == 'X': return
                if confirma.capitalize() != 'S': raise ValueError
            except Exception: print(' Valor inválido, por favor digite "S" ou "X"')
            else: break

        for i in range(len(dadosGlobais.animais)):
            for z in range(len(animais)): 
                if animais[z] == dadosGlobais.animais[i].id: dadosGlobais.animais[i].addVacina(Vacina(tipo, data, dadosGlobais.animais[i].id)); return

    def gerenciarVacinas(self): pass
