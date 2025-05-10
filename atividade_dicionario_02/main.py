'''
Crie um CRUD, ou seja, um programa que:
- Cadastre
- Liste
- Altere
- Exclua

O programa deverá cadastrar pessoas com os seguintes dados:
Nome, CPF, Emai, Telefone, Data de Nascimento, Gênero.
'''

# o usuário poderá cadastrar quantas pessoas quiser.
# o programa deverá forncecer um menu com as opções: cadastrar, listar, alterar, excluir e sair do programa.

import os

pessoas = []

try:
    while True:
        cadastrar = input("Deseja cadastrar uma nova pessoa? (s/n): ")
        match cadastrar:
            case 's':
                # dicionário pessoa
                pessoa = {}
                
                # Pede os dados da pessoa e adiciona ao dicionário pessoa
                pessoa["nome"] = input("Informe o nome da pessoa: ")
                pessoa["cpf"] = input("Informe o CPF da pessoa: ")
                pessoa["email"] = input("Informe o email da pessoa: ")
                pessoa["Telefone"] = input("Informe o telefone da pessoa: ")
                pessoa["Data de Nascimento"] = input("Informe a data de nascimento da pessoa: ")
                pessoa["Gênero"] = input("Informe o gênero da pessoa: ")

                # Adiciona a pessoa à lista de pessoas
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
        while True:
            # Listar pessoas
            for chave in pessoa:
                print(f"{chave}: {pessoa.get(chave)}")

                # alterar dados
                prosseguir = input("Deseja alterar o dado de alguma pessoa? (s/n)")
                match prosseguir:
                    case "s":
                        alterar = input("Informe o nome do item que deseja alterar: ")
                        if alterar in pessoa:
                            pessoa[alterar] = input("informe o novo valor da chave escolhida:")
                            os.system("cls")
                            continue
                        else:
                            os.system("cls")
                            print(f"{alterar} não existe.")
                        continue
                    case "n":
                        break
                    case _:
                        print("Opção inválida.")
                        continue
            # Excluir pessoas
            excluir = input("Deseja excluir alguma pessoa? (s/n)")
            match excluir:
                case "s":
                    nome = input("Informe o nome da pessoa que deseja excluir: ")
                    for pessoa in pessoas:
                        if pessoa["nome"] == nome:
                            pessoas.pop(pessoa)
                            os.system("cls")
                            print(f"{nome} excluída com sucesso!")
                            break
                        else:
                            print(f"{nome} não existe.")
                            continue
                case "n":
                    break
                case _:
                    print("Opção inválida.")
                    continue

            # Sair do programa
            sair = input("Deseja sair do programa? (s/n)")
            match sair:
                case "s":
                    os.system("cls")
                    print("Saindo do programa... Até a próxima!")
                    break
                case "n":
                    os.system("cls")
                    continue
                case _:
                    print("Opção inválida.")
                    continue
except Exception as e:
    print(f"Não foi possível cadastrar pessoa. {e}.")