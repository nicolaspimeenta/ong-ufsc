from entidade.cachorro import Cachorro
from entidade.gato import Gato
from entidade.vacina import Vacina
from entidade.pessoa import Pessoa
from entidade.endereco import Endereco
from entidade.adocao import Adocao
from entidade.dados import Dados

dadosGlobais = Dados()

# DADOS PARA OTIMIZAR TESTES
dadosGlobais.saveEndereco(Endereco('88052600', 2270, 'Casa', 'Médio', 3))
dadosGlobais.saveEndereco(Endereco('88101030', 28, 'Apartamento', 'Pequeno', 0))
dadosGlobais.saveEndereco(Endereco('88710210', 9, 'Casa', 'Grande', 1))
dadosGlobais.saveEndereco(Endereco('88090222', 38, 'Apartamento', 'Médio', 10))

dadosGlobais.savePessoa(Pessoa('086.407.259-77', 'Nicolas', ['25', '03', '2004'], Endereco('88052600', 2270, 'Casa', 'Médio', 3)))
dadosGlobais.savePessoa(Pessoa('762.522.690-50', 'TESTE1', ['20', '02', '2003'], Endereco('88101030', 28, 'Apartamento', 'Pequeno', 0)))
dadosGlobais.savePessoa(Pessoa('740.168.010-60', 'TESTE2', ['19', '11', '2001'], Endereco('88710210', 9, 'Casa', 'Grande', 1)))
dadosGlobais.savePessoa(Pessoa('261.618.070-76', 'TESTE3', ['30', '08', '1983'], Endereco('88090222', 38, 'Apartamento', 'Médio', 10)))

dadosGlobais.saveAnimal(Gato(1, 'Gato', 'Pimentinha', 'Espanhola', dadosGlobais.pessoas[0]))
dadosGlobais.saveAnimal(Gato(2, 'Gato', 'TESTE1', 'Siamês', None))
dadosGlobais.saveAnimal(Cachorro(3, 'Cachorro', 'TESTE2', 'Pitbull', None, 'Grande'))
dadosGlobais.saveAnimal(Cachorro(4, 'Cachorro', 'TESTE3', 'Qualquer', None, 'Pequeno'))
dadosGlobais.saveAnimal(Cachorro(5, 'Cachorro', 'TESTE4', 'Qualquer', None, 'Grande'))


dadosGlobais.saveVacina(Vacina('Raiva', ['20', '09', '2015'], dadosGlobais.animais[0]))
dadosGlobais.animais[0].addVacina(dadosGlobais.vacinas[-1])
dadosGlobais.saveVacina(Vacina('Leptospirose', ['09', '11', '2015'], dadosGlobais.animais[0]))
dadosGlobais.animais[0].addVacina(dadosGlobais.vacinas[-1])
dadosGlobais.saveVacina(Vacina('Hepatite Infecciosa', ['01', '04', '2014'], dadosGlobais.animais[0]))
dadosGlobais.animais[0].addVacina(dadosGlobais.vacinas[-1])

dadosGlobais.saveAdocao(Adocao(dadosGlobais.pessoas[0], dadosGlobais.animais[0], ['13', '04', '2023'], True))

