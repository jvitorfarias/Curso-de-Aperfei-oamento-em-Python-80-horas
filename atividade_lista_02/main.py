"""
Crie um programa em que o usuário informa varias notas de um aluno de 0 a 10 (quantas ele quiser inserir), e ao final, o programa calcule a média desse aluno e informa se ele está aprovado, de recuperação o reprovado.
Obs: média para aprovação é 7,0. Média para recuperação: entre 5 e 7. Abaixo de 5: reprovado.
"""

import os
notas = []

try:
    while True:
        nota_inserida = float(input("Informe a nota do aluno:").replace(",","."))

        if nota_inserida >= 0 and nota_inserida <= 10:
            notas.append(nota_inserida)
            continue
        else: 
            print("Nota inválida, informe um valor entre 0 e 10.")
            continue
        
    while True:
        media = sum(notas) / len(notas)
        match media:
            case _ if media >= 7:
                print(f"Aluno aprovado com média {media:.2f}.")
            case _ if media >= 5 and media < 7:
                print(f"Aluno de recuperação com média {media:.2f}.")
            case _ if media < 5:
                print(f"Aluno reprovado com média {media:.2f}.")
            case _:
                print("Erro ao calcular a média.")
            
except Exception as e:
    print("Tente novamente.")