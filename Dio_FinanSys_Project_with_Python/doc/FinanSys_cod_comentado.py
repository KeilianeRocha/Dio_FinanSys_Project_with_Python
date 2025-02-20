import textwrap
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
# - Importação de módulos:
# - `textwrap` ⇒ formatar strings com indentação e quebras de linha.
# - `abc`: ⇒ criar classes abstratas e métodos abstratos.
# - `datetime`: ⇒ manipulação de datas e horas.
# - `pathlib`: ⇒ manipulação de caminhos de arquivos de forma independente do sistema operacional.

ROOT_PATH = Path(__file__).parent  
# - Uso de `Path`:
# - Para manipulação de caminhos de arquivos de forma segura e independente do sistema operacional.
# - Exemplo: `ROOT_PATH = Path(__file__).parent`.

# - Métodos especiais:
# - `__init__`: Construtor da classe, chamado ao criar uma instância.
# - `__repr__`: Retorna uma representação em string do objeto.
# - `__iter__` e `__next__`: Permitem que um objeto seja iterável.

class ContaIterador:
    # - Iteradores:
    # - Objetos que permitem iterar sobre uma coleção.
    # - Exemplo: `ContaIterador` para iterar sobre contas.
    def __init__(self, contas):
        self.contas = contas
        self._index = 0
    # - Uso de `raise`:
    # - Para lançar exceções.
    # - Exemplo: `raise StopIteration` no método `__next__`.
    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            self._index += 1
            return conta
        except IndexError:
            raise StopIteration


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("\n@@@ Você excedeu o número de transações permitidas para hoje!")
            return
        # - Uso de `len`:
        # - Para obter o tamanho de uma coleção.
        # - Exemplo: `if len(conta.historico.transacoes_do_dia()) >= 2:`.

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# - Herança:
# - Uma classe pode herdar atributos e métodos de outra classe.
# - Exemplo: `PessoaFisica` herda de `Cliente`.

class PessoaFisica(Cliente):
    # - Uso de `super()`:
    # - Chama métodos da classe pai.
    # - Exemplo: `super().__init__(endereco)` na classe `PessoaFisica`.
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ('{self.cpf}')>"

# - Definição de classes:
# - Classes são usadas para criar objetos que encapsulam dados (atributos) e comportamentos (métodos).
# - Exemplo: `Cliente`, `Conta`, `Historico`, etc.

class Conta:
    # - Encapsulamento:
    # - Uso de atributos privados (com `_`) para proteger dados.
    # - Exemplo: `_saldo`, `_numero`, `_agencia`, etc.
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    # - Métodos de classe (`@classmethod`):
    # - Métodos que pertencem à classe, não à instância.
    # - Exemplo: `nova_conta` na classe `Conta`.
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    # - Propriedades (`@property`):
    # - Permitem definir métodos que podem ser acessados como atributos.
    # - Exemplo: `saldo`, `numero`, `agencia`, etc
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

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        # - Uso de `return`:
        # - Para retornar valores de funções.
        # - Exemplo: `return True` no método `sacar`.
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    # - List comprehensions:
    # - Sintaxe concisa para criar listas.
    # - Exemplo: `[transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]`.
    def sacar(self, valor):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                # - Uso de `if __name__ == "__main__":`
                # - Garante que o código só seja executado quando o script é rodado diretamente, não quando importado.
                if transacao["tipo"] == Saque.__name__
            ]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    # - Formatação de strings:
    # - Uso de f-strings para inserir variáveis em strings.
    # - Exemplo: f"Agência:\t{self.agencia}".
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            Saldo:\tR$ {self.saldo:.2f}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            # - Uso de `dict`:
            # - Para criar e manipular dicionários.
            # - Exemplo: `self._transacoes.append({"tipo": transacao.__class__.__name__, 
            # "valor": transacao.valor, "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")})`.
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def transacoes_do_dia(self):
        hoje = datetime.now().date()
        return [
            transacao
            for transacao in self._transacoes
            if datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date() == hoje
        ]

    # - Uso de `yield`:
    # - Transforma uma função em um gerador, que pode ser iterado.
    # - Exemplo: `gerar_relatorio` na classe `Historico`.
    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"] == tipo_transacao:
                yield transacao
# - Métodos abstratos (`@abstractmethod`):
# - Métodos que devem ser implementados por classes filhas.
# - Exemplo: `valor` e `registrar` na classe `Transacao`.

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        # - Uso de `pass`:
        # - Para indicar um bloco de código vazio.
        # - Exemplo: `pass` em funções ou métodos que não têm implementação.
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

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
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
# - Decoradores:
# - Funções que modificam o comportamento de outras funções ou métodos.
# - Exemplo: `@log_transacao` para registrar chamadas de funções.

def log_transacao(func):
    # - Uso de `*args` e `**kwargs`:
    # - Permitem que funções aceitem um número variável de argumentos.
    # - Exemplo: `def envelope(*args, **kwargs)` no decorador `log_transacao`.
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # - Manipulação de datas:
        # - Uso de `datetime.now()` para obter a data/hora atual.
        # - Formatação de datas com `strftime`.
        try:
            # - Tratamento de exceções:
            # - Uso de `try` e `except` para capturar e tratar erros.
            # - Exemplo: Tratamento de `PermissionError` ao escrever no arquivo de log.
            with open(ROOT_PATH / "log.txt", "a", encoding="utf-8") as arquivo:
                # - Gerenciamento de arquivos:
                # - Uso de `with open()` para abrir e fechar arquivos de forma segura.
                # - Modos de abertura: 'a' para adicionar ao final do arquivo.
                arquivo.write(
                    f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}. Retornou {resultado}\n"
                )
        except PermissionError:
            print("Erro: Sem permissão para escrever no arquivo de log.")
        except Exception as e:
            print(f"Erro ao escrever no arquivo de log: {e}")

        return resultado

    return envelope

# - Funções:
# - Blocos de código reutilizáveis.
# - Exemplo: `menu()`, `filtrar_cliente()`, `recuperar_conta_cliente()`, etc.
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    # - Uso de `textwrap.dedent`:
    # - Remove indentação comum de strings multilinha.
    # - Exemplo: `textwrap.dedent(menu)`.
    return input(textwrap.dedent(menu))
# - Uso de `list`:
# - Para criar e manipular listas.
# - Exemplo: `clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]`.

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        # - Uso de `None`:
        # - Para representar a ausência de valor.
        # - Exemplo: `return None` em `recuperar_conta_cliente`.
        return None

    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None

    return cliente.contas[0]


@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    # - Uso de `float`:
    # - Para converter strings em números decimais.
    # - Exemplo: `valor = float(input("Informe o valor do depósito: "))`.
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def exibir_extrato(clientes):
    # - Uso de `input()`:
    # - Para capturar entrada do usuário.
    # - Exemplo: `cpf = input("Informe o CPF do cliente: ")`.
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        # - Uso de `for`:
        # - Para iterar sobre coleções.
        # - Exemplo: `for transacao in transacoes:` no método `exibir_extrato`.
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
    )

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    # - Uso de `str`:
    # - Para converter objetos em strings.
    # - Exemplo: `str(conta)` no método `listar_contas`.
    iterador = ContaIterador(contas)
    for conta in iterador:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []
    # - Uso de `while`:
    # - Para loops que continuam enquanto uma condição for verdadeira.
    # - Exemplo: `while True:` no método `main`.
    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            # - Uso de `int`:
            # - Para converter strings em números inteiros.
            # - Exemplo: `numero_conta = len(contas) + 1`.
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            # - Uso de `break`:
            # - Para sair de loops.
            # - Exemplo: `break` no método `main` para sair do loop infinito.
            break

        else:
            print(
                "\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@"
            )


main()
