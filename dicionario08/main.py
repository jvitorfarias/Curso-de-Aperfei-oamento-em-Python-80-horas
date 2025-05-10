pessoas = [
    {
        'nome': 'João Vítor',
        'idade': 28,
        'email': 'joao@vitor.com'
    },
    {
        'nome': 'Maria Clara',
        'idade': 51,
        'email': 'maria@clara.com'
    },
    {
        'nome': 'Pedro Henrique',
        'idade': 68,
        'email': 'pedro@henrique.com'
    }
]

for pessoa in pessoas:
    print(f"\n{'-'*20}\n")
    for chave in pessoa:
        print(f"{chave.title()}: {pessoa.get(chave)}.")