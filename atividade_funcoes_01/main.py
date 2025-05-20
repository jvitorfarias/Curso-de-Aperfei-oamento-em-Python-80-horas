# Crie um programa onde o usuário poderá escolher se deseja calcular a equação do 1º grau ou do 2º grau, e o programa retorna o resultado da equação.

# O programa deverá ser executado em loop.

# Escolhendo qual equação deseja calcular.

# importando bibliotecas
import time
import equacao as eq


try:
    opcao = input("Escolha uma das opções: \n1 - Calcular Equação do 1º grau\n2 - Calcular Equação do 2º grau\n3 - Sair do programa\n")


    if opcao == 1:
        # Equação do 1º grau
        a = float(input("Informe o valor de a:"))
        b = float(input("Informe o valor de b:"))
        e_primeiro_grau = eq.calcular_equacao_1_grau(a, b)
        print(f"O resultado da equação do 1º grau é: {e_primeiro_grau}")
    elif opcao == 2:
        # Equação do 2º grau
        a = float(input("Informe o valor de a:"))
        b = float(input("Informe o valor de b:"))
        c = float(input("Informe o valor de c:"))
        e_segundo_grau = eq.calcular_equacao_2_grau(a, b, c)
    elif opcao == 3:
        print("Saindo do programa, até a próxima!")

    else:
        print("Opção inválida! Tente novamente.")



    # Pergunta se o usuário deseja continuar
    continuar = input("Você deseja calcular outra equação? (s/n): ")
    if continuar.upper() == "S":
        print("Então vamos lá!")
        time.sleep(2)

    elif continuar.upper() == "N":
        print("Saindo do programa, até logo!")

    else:
        print("Opção inválida! Tente novamente.")

except Exception as e:
    print(f"Tente novamente{e}")