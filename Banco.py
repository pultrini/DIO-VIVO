from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import textwrap

class Client:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def transacoes(self, conta, transacao):
        transacao.registrar(conta)

    def add_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Client):
    def __init__(self, endereco, nome, data_nascimento, cpf):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self.saldo = 0
        slef._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def new_acount(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self):
        return self._cliente

    def sacar(self, valor):
        saldo = self.saldo
        if valor > saldo:
            print("operação falhou, saldo insuficiente")
        elif valor>0:
            self._saldo += valor
            print("Saldo Realizado")
            return True
        else:
            print("operação falhou, valor invalido.")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("saldo depositado.")
        else:
            print("valor invalido")
            return False
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [transacao for trnasacao in self._historico.transacoes if trnasacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saque

        if excedeu_limite:
            print("Operacao falhou o valor deve ser dentro do limite.")
        elif excedeu_saques:
            print("limite de saque atingido")

        else:
            return super().sacar(valor)
        return False

        def __str__(self)
        return f"""\
                Agencia: \t{self.agencia}
                C/C: \t\t{self.numero}
                Titular: \t {self.cliente.nome}
                """

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

    
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractproperty
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
       self.valor = valor
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

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

def depositar(clientes):
    cpf = input("coloque o cpf")
    clientes = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("cadastre-se antes")
        return
    valor = float(input("valor do deposito"))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta,transacao)

def filtrar_cliente(cliente):
    cliente_filtrados = [cliente for cliente in clientes if cliente.cpf ==cpf]
    return cliente_filtrados[0] if cliente_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("cliente nao encontrado")
        return
    #FIXME:
    return cliente.contas[0]

def sacar(cliente):
    cpf = input("coloque o cpf")
    clientes = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("nao encontrado")
        return
    valor = float(input("informe o valor"))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta,transacao)

def exibir_extrato(cliente):
    cpf = input("coloque o cpf")
    clientes = filtrar_cliente(cpf, clientes)

    transacoes = conta.historico.transacoes
    extrato = ''
    if not transacoes:
        extrato = "Vazio"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']:\n\t R$ {transacao['valor']:.2f}}"
    print(extrato)
    print(f'{conta.saldo:.2f}')

def criar_conta(numero_conta, clientes, contas):
    cpf = input("coloque o cpf")
    clientes = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("cadastre-se antes")
        return
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("criado")

def listar_contas(contas):
    for conta in contas:
        print("="*10)
        print(textwrap.dedent(str(conta)))

def criar_clientes(cliente):
    cpf = input("coloque o cpf")
    clientes = filtrar_cliente(cpf, clientes)

    if  cliente:
        print("já existente")
        return
    nome = input("Nome completo: ")
    data_nascimento = input("Data nascimento")
    endereco = input("endereco")
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, endereco=endereco)
    clientes.append(cliente)

def main():
    clientes = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
            sacar(clientes)


        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == '4':
            criar_cliente(clientes)
        
        elif opcao == '5':
            numero_conta = len(contas) +1
            criar_conta(numero_conta, clientes, contas)


        elif opcao == "0":
            break

        else:
            print("Selecione uma operação válida")