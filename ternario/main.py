# declarando variaveis

nome = input("digite seu nome: ")

idade = int(input("Qual sua idade: "))

# Utilizando operador ternário para decisao

result = "é maior de idade" if idade >= 18 else "é menor de idade"

# exibindo resultado na tela

print(f"{nome} {result}")   