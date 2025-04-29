# NOTE: o SPLIT é um comando que pega os valores de uma string e separa em uma lista.

# variável
ano = "Janeiro, Fevereiro, Março, Abril, Maio, Junho, Julho, Agosto, Setembro, Outubro, Novembro, Dezembro"

# algoritmo
try: 
    meses = ano.split(", ")
    for mes in meses:
        print(mes)
except Exception as e:
    print(f"Não foi possível separar os valores. {e}.")