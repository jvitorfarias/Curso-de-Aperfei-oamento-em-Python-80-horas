import os

dados = {
    'nome': "João Vítor",
    'idade': 28,
    'cpf': "123.456.789-00"
}

try:
    while True:
        os.system('cls')
        for chave in dados:
            print(f"{chave.title()}: {dados.get(chave)}.")

        # usuario informa se deseja inserir nova chave ou encerrar programa
        prosseguir = input("\nDeseja inserir nova chave? (s/n): ").lower()

        match prosseguir:
            case 's':
                # usuario informa os dados
                nova_chave = input("\nDigite a nova chave: ")
                dados[nova_chave] = input(f"Informe o valor de {nova_chave}: ")
                continue
            case 'n':
                break
            case _:
                print("Opção inválida.")
                continue     
except Exception as e:
    print(f"Não foi possível inserir a nova chave {e}")