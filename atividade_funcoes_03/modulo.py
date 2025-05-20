def fazer_deposito(saldo, valor_depositado):
    saldo += valor_depositado
    return saldo

def fazer_saque(saldo, valor_saque):
    saldo -= valor_saque
    return saldo

def consultar_dados(titular):
    print(f"{'-'*20} Dados da conta {'-'*20}")
    print(f"Titular: {titular.get('nome')}")
    print(f"CPF: {titular.get('cpf')}")
    print(f"Agência: {titular.get('agencia')}")
    print(f"Número da conta do titular: {titular.get('num_conta')}")
    print(f"Saldo atual: {titular.get('saldo')}")