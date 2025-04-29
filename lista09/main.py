# importando biblioteca
import os

# declaração de lista
nomes = ["Sasuke", "Naruto", "Sakura", "Shikamaru", "Ino", "Chouji"]

# tratamento de exceção
try: 
    # loop infinito
    while True:
        # exibe a lista
        for i in range(len(nomes)):
            print(f"Nome de código {i}: {nomes[i]}.")

        opcao = input("Deseja excluir item da lista? (s/n)")
        match opcao:
            case "s":
                posicao = int(input("Informe o código do nome a ser deletado: "))
                del(nomes[posicao])
                os.system("cls")
                print("Item excluído com sucesso!\n")
                continue
            case "n":
                break
            case _:
                print("Opção inválida.")
                continue
except Exception as e:
    print(f"Não foi possível deletar o item da lista. {e}.")