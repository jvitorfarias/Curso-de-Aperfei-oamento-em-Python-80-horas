# declaração de funcoes

def calcular_equacao_1_grau(a, b):
    # Equação do 1º grau
        calculo = -b / a
        print(f"O resultado da equação do 1º grau é: {calculo}")

def calcular_equacao_2_grau(a, b, c):
        

        # delta
        delta = pow(b, 2) - 4 * a * c
        if delta < 0:
            print("O valor de delta não pode ser menor que 0!")
        elif delta == 0:
            print("O valor de delta não pode ser igual a 0!")
        else:
            x1 = (-b + pow(delta, 0.5)) / (2 * a)
            x2 = (-b - pow(delta, 0.5)) / (2 * a)
            print(f"O resultado da equação do 2º grau é: {x1} e {x2}")