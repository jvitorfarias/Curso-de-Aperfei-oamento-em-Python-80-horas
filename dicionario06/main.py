import os

chaves = ("nome", "idade", "cpf", "telefone", "email", "profissão")
usuario = {
    chaves[0]: "João Vítor",
    chaves[1]: 28,
    chaves[2]: "123.456.789-00",
    chaves[3]: "(11) 98765-4321",
    chaves[4]: "joao@vitor.com",
    chaves[5]: "Desenvolvedor",
}
try:
    while True:
        
        for chave in chaves:
            print(f"{chave}: {usuario.get(chave)}")
        prosseguir = input("Deseja alterar o dado de alguma chave? (s/n)")
        match prosseguir:
            case "s":
                chave_escolhida = input("Informe o nome da chave que deseja alterar: ")
                if chave_escolhida in chaves:
                    usuario[chave_escolhida] = input("informe o novo valor da chave escolhida:")
                    os.system("cls")
                    continue
                else:
                    os.system("cls")
                    print(f"{chave_escolhida} não existe.")
                continue
            case "n":
                break
            case _:
                print("Opção inválida.")
                continue
except Exception as e:
    print(f"Não foi possível atualizar os dados. {e}." )
