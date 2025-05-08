"""
Crie um programa que inicializa um dicionario zerado, e o usuario adiciona e insere os seguintes dados:
Nome, Data de Nascimento, CPF, Email, Genero, Telefone, Altura, Peso, Tipo Sanguineo;
Ao final, o programa exibe os dados do usuário e informa seu IMC. 
"""

import os

dados = {}

try:
    while True:
        os.system('cls')
        for chave in dados:
            print(f"{chave.title()}: {dados.get(chave)}.")

        insere_dado = input(f"Qual dado você deseja inserir?").lower()

        if insere_dado == 'peso':
            dados[insere_dado] = float(input(f"Informe o valor de {insere_dado}: "))
        elif insere_dado == 'altura':
            dados[insere_dado] = float(input(f"Informe o valor de {insere_dado}: "))
        else:
            dados[insere_dado] = input(f"Informe o valor de {insere_dado}: ")

        continuar = input("Deseja inserir mais dados? (s/n): ")

        if continuar == 's':
            continue
        elif continuar == 'n':
            print(dados)
            calculo_imc = dados['peso'] / (dados ['altura'] * dados ['altura'])
            print(f"Seu IMC é: {calculo_imc:,.2f} ")
            break
        else:
            print("Opção inválida.")
            
        calculo_imc = dados['peso'] / (dados ['altura'] * dados ['altura'])
        if calculo_imc < 18.5:
            print("Procure um nutricionista, você está abaixo do peso ideal.")
        elif calculo_imc >= 18.5 and calculo_imc < 24.9:
            print("Parabéns, você está no peso ideal.")
        elif calculo_imc >= 24.9 and calculo_imc <29.9:
            print("Cuidado, você está acima do peso ideal.")
        elif calculo_imc >= 29.9 and calculo_imc < 34.9:
            print("Faça exercícios físicos e uma dieta, você está com obesidade grau 1.")
        elif calculo_imc >= 34.9 and calculo_imc < 39.9:
            print("Procure um médico, você está com obesidade grau 2.")
        else:
            print("Procure um médico, você está com obesidade mórbida ou grau 3.")

except Exception as e:
    print(f"Não foi possível inserir a nova chave {e}")

 