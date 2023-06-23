import copy
import datetime
from limite.tela_animal import TelaAnimal
from controle.controlador_pessoa import ControladorPessoa
from entidade.vacina import Vacina
from entidade.cachorro import Cachorro
from entidade.gato import Gato
from entidade import dadosGlobais

class ControladorAnimal:
    def __init__(self):
        self.controladorPessoa = ControladorPessoa()
        self.tela = TelaAnimal()

    def iniciar(self):
        while True:
            escolha = int(self.tela.abreTela())
            if escolha == 0: return
            if escolha == 1: self.cadastrarAnimal()
            if escolha == 2: self.gerenciarAnimal()
            if escolha == 3: self.aplicarVacina()

    def cadastrarAnimal(self):
        dados = self.tela.cadastroAnimal()
        if dados[0] == 'Retornar': return

        if dados[1]['tipo'] == 'Cachorro Grande': dadosGlobais.saveAnimal(Cachorro(len(dadosGlobais.animais)+1, 'Cachorro', dados[1]['nome'], dados[1]['raca'], None, 'Grande'))
        if dados[1]['tipo'] == 'Cachorro Médio': dadosGlobais.saveAnimal(Cachorro(len(dadosGlobais.animais)+1, 'Cachorro', dados[1]['nome'], dados[1]['raca'], None, 'Médio'))
        if dados[1]['tipo'] == 'Cachorro Pequeno': dadosGlobais.saveAnimal(Cachorro(len(dadosGlobais.animais)+1, 'Cachorro', dados[1]['nome'], dados[1]['raca'], None, 'Pequeno'))
        if dados[1]['tipo'] == 'Gato': dadosGlobais.saveAnimal(Gato(len(dadosGlobais.animais)+1, 'Gato', dados[1]['nome'], dados[1]['raca'], None))


    def gerenciarAnimal(self):
        dados = self.tela.gerenciarAnimal(dadosGlobais.animais)
        if dados[0] == 'Retornar': return

        if dados[0] == 'Excluir':
            for key, value in dados[1].items():
                if value == True: dadosGlobais.animais.pop(key)

        if dados[0] == 'Alterar':
            for key, value in dados[1].items():
                if value == True: 
                    dados = self.tela.alterarAnimal(dadosGlobais.animais[key])
                    if dados[0] == 'Retornar': return
                    if dados[0] == 'Aplicar Vacina': self.aplicarVacina(dadosGlobais.animais[key].id)

                    dadosGlobais.animais[key].nome = dados[1]['nome']
                    dadosGlobais.animais[key].raca = dados[1]['raca']
                    if dados[1]['tipo'] == 'Cachorro Grande': dadosGlobais.animais[key].tamanho = 'Grande'
                    if dados[1]['tipo'] == 'Cachorro Médio': dadosGlobais.animais[key].tamanho = 'Médio'
                    if dados[1]['tipo'] == 'Cachorro Pequeno': dadosGlobais.animais[key].tamanho = 'Pequeno'

    def aplicarVacina(self, animal = 0):
        if animal == 0:
            dados, animaisEscolhidos = self.tela.aplicarVacina(dadosGlobais.animais, escolherAnimal=True)
        else:
            dados, animaisEscolhidos = self.tela.aplicarVacina(dadosGlobais.animais, escolherAnimal=False, id=animal)
            
        for id in animaisEscolhidos:
            for animal in dadosGlobais.animais:
                if animal.id == id:
                    dadosGlobais.saveVacina(dados[1]['tipo'], datetime.date(int(dados[1]['ano']), int(dados[1]['mes']), int(dados[1]['dia'])), animal)
                    animal.addVacina(dadosGlobais.vacinas[-1])
            
    def validaAdocao(self, animal, cachorroGrande):
        if animal.dono: return False
        if cachorroGrande:
            if animal.tipo == 'Cachorro':
                if animal.tamanho == 'Grande': return False
        vacinasEncontradas = []
        for vacinaNecessaria in ['Hepatite Infecciosa', 'Leptospirose', 'Raiva']:
            for vacina in animal.vacinas:
                if vacina.tipo == vacinaNecessaria and not (vacinaNecessaria in vacinasEncontradas): vacinasEncontradas.append(vacina.tipo)
        if vacinasEncontradas == ['Hepatite Infecciosa', 'Leptospirose', 'Raiva'] and animal.dono == None: return True
        return False


