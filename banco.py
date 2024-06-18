import random
class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.conta = random.randint(1000, 9999)
        self.extrato = []
    def deposito(self, valor):
        try:
            if valor < 1:
                print(f"valor {format(valor, '.2f')} não permitido...")
            else:
                self.saldo += valor
                self.extrato.append(
                    f"valor de R$ {format(valor, '.2f')} depositado \nsaldo atual R$ {format(self.saldo, '.2f')}")
        except ValueError:
            print("valor inválido...")

    def saque(self, valor):
        try:
            if self.saldo >= valor:
                self.saldo -= valor
                self.extrato.append(
                    f"valor de R$ {format(valor, '.2f')} sacado, \nsaldo atual R$ {format(self.saldo, '.2f')}")
            elif valor < 1:
                print(f"valor {format(valor, '.2f')} não permitido...")
            else:
                print("saldo insuficiente...")
        except ValueError:
            print("valor inválido...")

    def exibir_extrato(self):
        print()
        for e in self.extrato:
            print(e)
        print()

class Titular:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco

while True:
    opcao = int(input("cadastro de titular aperte 1 - continuar, aperte 0 - sair:  "))
    if opcao == 1:
        titular = Titular(
            input("digite o cpf: "),
            input("digite o nome: "),
            input("digite o endereço completo: ")
        )
        conta = Conta(titular)
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
            conta.deposito(float(input('Digite um valor para depositar: ')))

        except ValueError:
            print("valor invalido")          
        continue
    elif operacao == 's':
        conta.saque(float(input('Digite um valor para sacar: ')))
        continue
    elif operacao == 'e':
        conta.exibir_extrato()
        continue
    elif operacao == 'x':
        print("saindo...")
        break
    else:
        print("opção inválida...")
        continue