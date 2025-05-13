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

lista = []

try:
    while True:
        usuario = {}
        # exibe o menu
        print("Menu:")
        print("1 - Cadastrar pessoa")
        print("2 - Listar pessoas")
        print("3 - Alterar dados de uma pessoa")
        print("4 - Excluir pessoa")
        print("5 - Sair")

        opcao = input("\nEscolha uma das opções: ")
        match opcao:
            case '1':
                # Pede os dados da pessoa e adiciona ao dicionário usuario
                usuario["nome"] = input("Informe o nome da pessoa: ")
                usuario["cpf"] = input("Informe o CPF da pessoa: ")
                usuario["email"] = input("Informe o email da pessoa: ")
                usuario["telefone"] = input("Informe o telefone da pessoa: ")
                usuario["data_nascimento"] = input("Informe a data de nascimento da pessoa: ")
                usuario["genero"] = input("Informe o gênero da pessoa: ")

                lista.append(usuario)
                os.system('cls')
                print(f"{usuario.get('nome')} cadastrada com sucesso!")
                continue
            case '2':
                os.system('cls')
                # Listar pessoas
                for i in range(len(lista)):
                    print(f"\nPosição {i}:")
                    for chave in lista[i]:
                        print(f"{chave.title()}: {lista[i].get(chave)}")
                print("\n")
                continue
            case '3':
                # Alterar dados
                os.system('cls')
                posicao = int(input("Informe a posição da pessoa que deseja alterar: "))
                if lista[posicao]:
                    for chave in lista[posicao]:
                        print(f"{chave.title()}: {lista[posicao].get(chave)}")
                    print("\n")
                    dado = input("Informe o nome do item que deseja alterar: ")
                    if lista[posicao][dado]:
                        lista[posicao][dado] = input(f"Informe o novo valor de {dado}: ")
                        os.system('cls')
                        print(f"{dado} alterada com sucesso!")
                    else:
                        os.system('cls')
                        print(f"{dado} não existe.")
                else:
                    os.system('cls')
                    print("Essa posição não existe.")
                for i in range(len(lista)):
                    print(f"\nPosição {i}:")
                continue
            case '4':
                # Excluir pessoas
                os.system('cls')
                posicao = int(input("Informe a posição da pessoa que deseja excluir: "))
                if lista[posicao]:
                    del(lista[posicao])
                    os.system('cls')
                    print(f"Pessoa excluída com sucesso!")
                else:
                    os.system('cls')
                    print("Não foi possível excluir a pessoa.")
                continue
            case '5':
                os.system('cls')
                # Sair do programa
                print("Saindo do programa... Até a próxima!")
                break   
            case _:
                os.system('cls')
                print("Opção inválida.")
                continue
except Exception as e:
    print(f"Não foi possível cadastrar pessoa. {e}.")
