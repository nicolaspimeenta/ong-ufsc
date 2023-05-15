repositorio: https://github.com/nicolaspimeenta/ong-ufsc

bibliotecas utilizadas: dateutil e validate-docbr

pip install python-dateutil

pip install validate-docbr

dados para testar:

dadosGlobais.saveEndereco(Endereco('88052600', 2270, 'Casa', 'Médio', 3))
dadosGlobais.saveEndereco(Endereco('88101030', 28, 'Apartamento', 'Pequeno', 0))
dadosGlobais.saveEndereco(Endereco('88710210', 9, 'Casa', 'Grande', 1))
dadosGlobais.saveEndereco(Endereco('88090222', 38, 'Apartamento', 'Médio', 10))

dadosGlobais.savePessoa(Pessoa('086.407.259-77', 'Nicolas', datetime.date(2004, 3, 25), Endereco('88052600', 2270, 'Casa', 'Médio', 3)))
dadosGlobais.savePessoa(Pessoa('762.522.690-50', 'TESTE1', datetime.date(2003, 2, 20), Endereco('88101030', 28, 'Apartamento', 'Pequeno', 0)))
dadosGlobais.savePessoa(Pessoa('740.168.010-60', 'TESTE2', datetime.date(2001, 11, 19), Endereco('88710210', 9, 'Casa', 'Grande', 1)))
dadosGlobais.savePessoa(Pessoa('261.618.070-76', 'TESTE3TESTE3TESTE3TESTE3TESTE3', datetime.date(1983, 8, 30), Endereco('88090222', 38, 'Apartamento', 'Médio', 10)))

dadosGlobais.saveAnimal(Gato(1, 'Gato', 'Pimentinha', 'Espanhola', dadosGlobais.pessoas[0]))
dadosGlobais.saveAnimal(Gato(2, 'Gato', 'TESTE1', 'Siamês', None))
dadosGlobais.saveAnimal(Cachorro(3, 'Cachorro', 'TESTE2', 'Pitbull', None, 'Grande'))
dadosGlobais.saveAnimal(Cachorro(4, 'Cachorro', 'TESTE3', 'Qualquer', None, 'Pequeno'))
dadosGlobais.saveAnimal(Cachorro(5, 'Cachorro', 'TESTE4', 'Qualquer', None, 'Grande'))


dadosGlobais.saveVacina(Vacina('Raiva', datetime.date(2023, 4, 25), dadosGlobais.animais[0]))
dadosGlobais.animais[0].addVacina(dadosGlobais.vacinas[-1])
dadosGlobais.saveVacina(Vacina('Leptospirose', datetime.date(2022, 11, 6), dadosGlobais.animais[0]))
dadosGlobais.animais[0].addVacina(dadosGlobais.vacinas[-1])
dadosGlobais.saveVacina(Vacina('Hepatite Infecciosa', datetime.date(2014, 4, 1), dadosGlobais.animais[0]))
dadosGlobais.animais[0].addVacina(dadosGlobais.vacinas[-1])

dadosGlobais.saveVacina(Vacina('Raiva', datetime.date(2023, 5, 10), dadosGlobais.animais[1]))
dadosGlobais.animais[1].addVacina(dadosGlobais.vacinas[-1])
dadosGlobais.saveVacina(Vacina('Leptospirose', datetime.date(2022, 11, 6), dadosGlobais.animais[1]))
dadosGlobais.animais[1].addVacina(dadosGlobais.vacinas[-1])
dadosGlobais.saveVacina(Vacina('Hepatite Infecciosa', datetime.date(2023, 4, 20), dadosGlobais.animais[1]))
dadosGlobais.animais[1].addVacina(dadosGlobais.vacinas[-1])

dadosGlobais.saveAdocao(Adocao(dadosGlobais.pessoas[0], dadosGlobais.animais[0], datetime.date(2023, 5, 14), True))