"""
Crie um programa em que o usuário informa varias notas de um aluno de 0 a 10 (quantas ele quiser inserir), e ao final, o programa calcule a média desse aluno e informa se ele está aprovado, de recuperação o reprovado.
Obs: média para aprovação é 7,0. Média para recuperação: entre 5 e 7. Abaixo de 5: reprovado.
"""

import os
notas = []

try:
    while True:
        nota_inserida = float(input("Informe a nota do aluno:").replace(",", "."))

        if nota_inserida >= 0 and nota_inserida <= 10:
            notas.append(nota_inserida)
            print("Nota inserida com sucesso!")
            while True:
                continuar = input("Deseja inserir uma nova nota? (s/n)")
                if continuar == "s" or continuar == "n":
                    os.system("cls")
                    break
                else:
                    print("Opção inválida")
                    continue
            match continuar:
                case "s":
                    continue
                case "n":
                    break
        else: 
            print("Nota inválida, informe um valor entre 0 e 10.")
            continue
    for i in range(len(notas)):
        print(f"Nota: {notas[i]}")

    media = sum(notas)/len(notas)
except Exception as e:
    print(f"Não foi possível inserir as notas e calcular a média. {e}")
finally:
    print(f"Média das notas: {media:,.2f}.")
    if media >= 7:
        print("O aluno está aprovado!")
    elif media >= 5:
        print("O aluno está de recuperação!")
    else:
        print("O aluno está reprovado!")