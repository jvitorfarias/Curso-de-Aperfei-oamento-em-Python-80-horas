import os

nomes = ["Hashirama", "Tobirama", "Hiruzen", "Minato", "Tsunade", "Kakashi"]

try: 
    for i in range(len(nomes)):
        print(f"Código {i}: {nomes[i]}.")
    posicao = int(input("Informe o código do nome a ser separado: "))
    nome_separado = nomes.pop(posicao)
    os.system('cls')
    print(nome_separado)
    print(nomes)
except Exception as e:
    print(f"Não foi possível separar o item da lista. {e}.")