# Dicionário é um tipo de lista em que cada posição da lista é identificada por uma chave ao invés de um número.
# pode ser usar '' ou "", mas o ideal é utilizar ''.
# declaração de dicionario

usuario = {
    'nome': "João Vítor",
    'idade': 28,
    'profissao': "Programador"
}

# Primeira forma de mostrar os dados dentro do dicionario
print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']} anos")
print(f"Profissão: {usuario['profissao']}")
# print(f"CPF: {usuario['cpf']}")

# Segunda forma de mostrar os dados dentro do dicionario
print(f"\nNome: {usuario.get('nome')}")
print(f"Idade: {usuario.get('idade')} anos")
print(f"Profissão: {usuario.get('profissao')}")
print(f"CPF: {usuario.get('cpf')}")