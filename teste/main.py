# Comentário para testar o programa atividade_automacao_01 completo.

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
    
        for chave in usuario:
            print(f"{chave}: {usuario[chave]}")

        prosseguir = input("Deseja excluir alguma chave? (s/n): ").strip().lower()
        if prosseguir == "s":
            chave_escolhida = input("Informe o nome da chave que deseja excluir: ").strip()
            if chave_escolhida in usuario:
                usuario.pop(chave_escolhida)
                print(f"chave {chave_escolhida} excluída com sucesso.")
            else:
                print(f"A chave '{chave_escolhida}' não existe.")
        elif prosseguir == "n":
            break
        else:
            print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")

except Exception as e:
    print(f"Não foi possível atualizar os dados. Erro: {e}")