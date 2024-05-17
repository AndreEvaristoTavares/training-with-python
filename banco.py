saldo_total = 0
extrato = []
def deposito(valor):
    global saldo_total
    try:
        if valor < 1:
            print(f"valor {valor} não permitido...")
        else:  
            saldo_total += valor
            extrato.append(f"valor de R$ {valor} depositado \nsaldo atual R$ {saldo_total}")
    except ValueError:
        print("valor inválido...")
def saque(valor):
    global saldo_total
    try:
        if saldo_total >= valor:
            saldo_total -= valor
            extrato.append(f"valor de R$ {valor} sacado, \nsaldo atual R$ {saldo_total}")
        elif valor < 1:
            print(f"valor {valor} não permitido...")
        else:
            print("saldo insuficiente...")
    except ValueError:
        print("valor inválido...")
def exibir_extrato():
    print()
    for e in extrato:
        print(e)
    print()
while True:
    operacao = input('digite a operação que deseja fazer: \nD = deposito, \nS = saque, \nE = extrato, \nX = sair \n')
    if operacao == 'd':
        try:
            deposito(float(input('Digite um valor para depositar: ')))
        except ValueError:
            print("valor invalido")          
        continue
    elif operacao == 's': 
        saque(float(input('Digite um valor para sacar: ')) )
        continue
    elif operacao == 'e':
        exibir_extrato()
        continue
    elif operacao == 'x':
        print("saindo...")
        break
    else:
        print("opção inválida...")
        continue
