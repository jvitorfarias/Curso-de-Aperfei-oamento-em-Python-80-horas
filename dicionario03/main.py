# biblioteca
import os

# dicionario

dados = {
    'nome': "João Vítor",
    'idade': 28,
    'cpf': "123.456.789-00"
}

# exibindo os dados do dicionario

for chave in dados:
    print(f"{chave.title()}: {dados.get(chave)}.")

# usuário insere nova chave email
dados['email'] = input("Digite o e-mail do usuário: ")

# limpa terminal e re-exibe a lista
os.system('cls')
for chave in dados:
    print(f"{chave.title()}: {dados.get(chave)}.")