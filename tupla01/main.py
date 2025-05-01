# tupla
dias_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")

# listando a tupla
for dia in dias_semana:
    print(dia)

try: 
    # tentativa fazer operação de lista
    dias_semana.append("Sétima")

    print("\n")

    for dia in dias_semana:
        print(dia)
except Exception as e:
    print(f"Não foi possível inserir item na tupla. {e}.")

    # diferença de lista para tupla é que a tupla usa () ao invés de [].
    # O () somente é utilizado na declaração da tupla.

    