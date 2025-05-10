import os

pessoas = []

try:

    while True:
        cadastrar = input("Deseja cadastrar uma nova pessoa? (s/n): ")
        match cadastrar:
            case 's':
                pessoa = {}

                pessoa["nome"] = input("Informe o nome da pessoa: ")
                pessoa["email"] = input("Informe o email da pessoa: ")
                pessoa["cpf"] = input("Informe o CPF da pessoa: ")

                pessoas.append(pessoa)
                
                os.system('cls')
                print(f"{pessoa.get('nome')} cadastrada com sucesso!")
                for pessoa in pessoas:
                    print(f"\n{'-'*20}\n")
                    for chave in pessoa:
                        print(f"{chave.title()}: {pessoa.get(chave)}.")
            case 'n':
                break
            case _:
                print("Opção inválida.")
                continue
except Exception as e:
    print(f"Não foi possível cadastrar pessoa. {e}.")