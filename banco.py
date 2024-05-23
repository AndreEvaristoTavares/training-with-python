import random
saldo_total = 0
conta = {}
titular = {}
extrato = []

def recebe_dados(cpf, nome, endereco, conta):
    titular[cpf] = {'nome': nome, 'endereco': endereco, 'conta':conta}


def deposito(valor):
    global saldo_total
    try:
        if valor < 1:
            print(f"valor {format(valor, '.2f')} não permitido...")
        else:  
            saldo_total += valor
            extrato.append(f"valor de R$ {format(valor, '.2f')} depositado \nsaldo atual R$ {format(saldo_total, '.2f')}")
    except ValueError:
        print("valor inválido...")
def saque(valor):
    global saldo_total
    try:
        if saldo_total >= valor:
            saldo_total -= valor
            extrato.append(f"valor de R$ {format(valor, '.2f')} sacado, \nsaldo atual R$ {format(saldo_total, '.2f')}")
        elif valor < 1:
            print(f"valor {format(valor, '.2f')} não permitido...")
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
    opcao = int(input("cadastro de titular aperte 1 - continuar, aperte 0 - sair:  "))
    if opcao == 1:
        conta = random.randint(1000, 9999)
        recebe_dados(
            input("digite o cpf: "),
            input("digite o nome: "),
            input("digite o endereço completo: "), 
            conta
            )
        continue
    elif opcao == 0:
        print("adeus...")
        break
    else:
        print('opcao invalida')
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
