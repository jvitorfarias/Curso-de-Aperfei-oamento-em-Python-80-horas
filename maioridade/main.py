# declarando variaveis

nome = input("Digite seu nome: ")

idade = int(input("Qual sua idade?"))

# estrutura de decisao

if idade >= 18:
    print(f"Parabéns, {nome}! Você pode acessar o nosso site.")
else:
    print(f"Infelizmente, {nome}, devido ter {idade} anos, você não poderá acessar nosso site.")