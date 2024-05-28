menu = """

[1] Deposito
[2] Saque
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Qual o Valor para depositar em R$: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O deposito deve ser com valores maior que zero")

    elif opcao == "2":
        valor = float(input("Qual o valor do Saque: "))

        excedeu_saldo, excedeu_limite, excedeu_saques = valor > saldo, valor > limite, numero_saques>= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Não há saldo suficiente")

        elif excedeu_limite:
            print("Não há limite de saque")

        elif excedeu_saques:
            print("Saque diário excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Selecione uma operação válida")