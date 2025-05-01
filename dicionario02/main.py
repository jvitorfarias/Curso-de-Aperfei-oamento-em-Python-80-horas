# declarando dicionario

usuario = dict(Nome="João Vítor", Idade = 28, Email = "joao@vitor.com")

# terceira forma de mostrar os dados dentro do dicionario

for chave in usuario:
    print(f"{chave}: {usuario.get(chave)}")