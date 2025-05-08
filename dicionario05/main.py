chaves = ("nome", "idade", "cpf", "telefone", "email", "profissão")
usuario = {
    chaves[0]: "João Vítor",
    chaves[1]: 28,
    chaves[2]: "123.456.789-00",
    chaves[3]: "(11) 98765-4321",
    chaves[4]: "joao@vitor.com",
    chaves[5]: "Desenvolvedor",
}

for chave in chaves:
    print(f"{chave}: {usuario.get(chave)}")

    