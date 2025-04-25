# declarando variaveis
nome = input("Nome do aluno: ")

nota = float(input("Informe a nota do aluno: "))

# verifica se o aluno foi aprovado ou nao

if nota >= 0 and nota <= 10:
    if nota >= 7:
        print(f"O aluno {nome} está aprovado.")
    elif nota >= 5:
        print(f"O aluno {nome} está de recuperação.")
    else:
        print(f"O aluno {nome} está reprovado.")
else: 
    print("Nota invalida.")