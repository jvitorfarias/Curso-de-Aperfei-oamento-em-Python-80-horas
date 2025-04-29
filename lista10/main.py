# NOTE: o JOIN é um comando que pega os valores de uma lista e junta em uma única variável.

# lista
dias = [
    "Domingo", 
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado"
]

# juntando os nomes em um único valor
separador = " | " # delimitador

semana = separador.join(dias) # junta os valores da lista em uma única variável

print(semana) # imprime a variável