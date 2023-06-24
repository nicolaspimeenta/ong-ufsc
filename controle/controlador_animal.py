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
        valores = self.tela.cadastroAnimal()
        if valores[0] == 'Retornar': return

        if valores[1]['tipo'] == 'Cachorro Grande': dadosGlobais.saveAnimal(Cachorro(len(dadosGlobais.animais)+1, 'Cachorro', valores[1]['nome'], valores[1]['raca'], None, 'Grande'))
        if valores[1]['tipo'] == 'Cachorro Médio': dadosGlobais.saveAnimal(Cachorro(len(dadosGlobais.animais)+1, 'Cachorro', valores[1]['nome'], valores[1]['raca'], None, 'Médio'))
        if valores[1]['tipo'] == 'Cachorro Pequeno': dadosGlobais.saveAnimal(Cachorro(len(dadosGlobais.animais)+1, 'Cachorro', valores[1]['nome'], valores[1]['raca'], None, 'Pequeno'))
        if valores[1]['tipo'] == 'Gato': dadosGlobais.saveAnimal(Gato(len(dadosGlobais.animais)+1, 'Gato', valores[1]['nome'], valores[1]['raca'], None))


    def gerenciarAnimal(self):
        valores = self.tela.gerenciarAnimal(dadosGlobais.animais)
        if valores[0] == 'Retornar': return

        if valores[0] == 'Excluir':
            for key, value in valores[1].items():
                if value == True: 
                    animalExcluido = dadosGlobais.animais.pop(key)
                    for animal in dadosGlobais.animais:
                        if animal.id > animalExcluido.id: animal.id -= 1

        if valores[0] == 'Alterar':
            for key, value in valores[1].items():
                if value == True: 
                    valores = self.tela.alterarAnimal(dadosGlobais.animais[key])
                    if valores[0] == 'Retornar': return
                    if valores[0] == 'Aplicar Vacina': self.aplicarVacina(dadosGlobais.animais[key].id); return
                    if valores[0] == 'Gerenciar Vacinas': self.gerenciarVacinas(dadosGlobais.animais[key]); return

                    dadosGlobais.animais[key].nome = valores[1]['nome']
                    dadosGlobais.animais[key].raca = valores[1]['raca']
                    if valores[1]['tipo'] == 'Cachorro Grande': dadosGlobais.animais[key].tamanho = 'Grande'
                    if valores[1]['tipo'] == 'Cachorro Médio': dadosGlobais.animais[key].tamanho = 'Médio'
                    if valores[1]['tipo'] == 'Cachorro Pequeno': dadosGlobais.animais[key].tamanho = 'Pequeno'

    def aplicarVacina(self, animal = 0):
        if animal == 0:
            valores, animaisEscolhidos = self.tela.aplicarVacina(dadosGlobais.animais, escolherAnimal=True)
        else:
            valores, animaisEscolhidos = self.tela.aplicarVacina(dadosGlobais.animais, escolherAnimal=False, id=animal)
            
        for id in animaisEscolhidos:
            for animal in dadosGlobais.animais:
                if animal.id == id:
                    dadosGlobais.saveVacina(Vacina(valores[1]['tipo'], datetime.date(int(valores[1]['ano']), int(valores[1]['mes']), int(valores[1]['dia'])), animal))
                    animal.addVacina(dadosGlobais.vacinas[-1])
            
    def gerenciarVacinas(self, animal):
        valores = self.tela.gerenciarVacinas(animal.vacinas, animal)

        if valores[0] == 'Retornar': return

        if valores[0] == 'Excluir':
            for key, value in valores[1].items():
                if value == True: 
                    vacinaExcluida = animal.vacinas.pop(key)
                    dadosGlobais.vacinas.remove(vacinaExcluida)

        if valores[0] == 'Alterar':
            for key, value in valores[1].items():
                if value == True: 
                    valores = self.tela.alterarVacina(animal.vacinas[key])
                    if valores[0] == 'Retornar': return

                    for vacina in dadosGlobais.vacinas:
                        if vacina == animal.vacinas[key]:
                            vacina.tipo = valores[1]['tipo']
                            vacina.data = datetime.date(int(valores[1]['ano']), int(valores[1]['mes']), int(valores[1]['dia']))

                    animal.vacinas[key].tipo = valores[1]['tipo']
                    animal.vacinas[key].data = datetime.date(int(valores[1]['ano']), int(valores[1]['mes']), int(valores[1]['dia']))




