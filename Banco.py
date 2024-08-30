import textwrap
def menu():
    menu = """

[1] Deposito
[2] Saque
[3] Extrato
[4] Novo Usuário
[5] Nova Conta
[0] Sair
=> """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito:\tR$ {valor:.2f}\n'
        print('Depositado com sucesso.')
    else:
        print("Coloque um valor válido.")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
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
        print("Saque Realizado.")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_user(usuarios):
    cpf = input("Informe o CPF (numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já exite este usuario")
        return
    nome = input("Nome Completo")
    data_nascimento = input("Data Nascimento (dd-mm-aaaa): ")
    endereco = input("endereco (logradouro, nro-bairro-cidade-estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Ususario criado com sucesso")

def filtrar_usuario(cpf, usuarios):
    user_filtrados = [user for user in usuarios if user[cpf]==cpf]
    return user_filtrados[0] if user_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {'agencia': agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuario nao encontrado")


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    contas=[]

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Qual o Valor para depositar em R$: "))

            saldo, extrato = depositar(saldo,valor,extrato)

        elif opcao == "2":
            valor = float(input("Qual o valor do Saque: "))

            saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques = LIMITE_SAQUES)


        elif opcao == "3":
            exibir_extrato()

        elif opcao == '4':
            criar_user(usuarios)
        
        elif opcao == '5':
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                conta.append(conta)


        elif opcao == "0":
            break

        else:
            print("Selecione uma operação válida")