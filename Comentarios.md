# Dio_FinanSys_Project_with_Python

<div style="text-align: center; font-size: 40px;">Comentários</div>






## 1. Importação de módulos:
## - `textwrap`: Para formatar strings com indentação e quebras de linha.
## - `abc`: Para criar classes abstratas e métodos abstratos.
## - `datetime`: Para manipulação de datas e horas.
## - `pathlib`: Para manipulação de caminhos de arquivos de forma independente do sistema operacional.

## 2. Definição de classes:
## - Classes são usadas para criar objetos que encapsulam dados (atributos) e comportamentos (métodos).
## - Exemplo: `Cliente`, `Conta`, `Historico`, etc.

## 3. Herança:
## - Uma classe pode herdar atributos e métodos de outra classe.
## - Exemplo: `PessoaFisica` herda de `Cliente`.

## 4. Métodos especiais:
## - `__init__`: Construtor da classe, chamado ao criar uma instância.
## - `__repr__`: Retorna uma representação em string do objeto.
## - `__iter__` e `__next__`: Permitem que um objeto seja iterável.

## 5. Propriedades (`@property`):
## - Permitem definir métodos que podem ser acessados como atributos.
## - Exemplo: `saldo`, `numero`, `agencia`, etc.

## 6. Métodos de classe (`@classmethod`):
## - Métodos que pertencem à classe, não à instância.
## - Exemplo: `nova_conta` na classe `Conta`.

## 7. Métodos abstratos (`@abstractmethod`):
## - Métodos que devem ser implementados por classes filhas.
## - Exemplo: `valor` e `registrar` na classe `Transacao`.

## 8. Decoradores:
## - Funções que modificam o comportamento de outras funções ou métodos.
## - Exemplo: `@log_transacao` para registrar chamadas de funções.

## 9. Gerenciamento de arquivos:
## - Uso de `with open()` para abrir e fechar arquivos de forma segura.
## - Modos de abertura: 'a' para adicionar ao final do arquivo.

## 10. Manipulação de datas:
## - Uso de `datetime.now()` para obter a data/hora atual.
## - Formatação de datas com `strftime`.

## 11. List comprehensions:
## - Sintaxe concisa para criar listas.
## - Exemplo: `[transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]`.

## 12. Tratamento de exceções:
## - Uso de `try` e `except` para capturar e tratar erros.
## - Exemplo: Tratamento de `PermissionError` ao escrever no arquivo de log.

## 13. Funções:
## - Blocos de código reutilizáveis.
## - Exemplo: `menu()`, `filtrar_cliente()`, `recuperar_conta_cliente()`, etc.

## 14. Iteradores:
## - Objetos que permitem iterar sobre uma coleção.
## - Exemplo: `ContaIterador` para iterar sobre contas.
TODO
## 15. Polimorfismo:#
## - Capacidade de objetos de diferentes classes responderem ao mesmo método de forma diferente.
## - Exemplo: `Saque` e `Deposito` implementam o método `registrar` de forma diferente.

## 16. Encapsulamento:
## - Uso de atributos privados (com `_`) para proteger dados.
## - Exemplo: `_saldo`, `_numero`, `_agencia`, etc.

## 17. Uso de `if __name__ == "__main__":`
## - Garante que o código só seja executado quando o script é rodado diretamente, não quando importado.

## 18. Formatação de strings:
## - Uso de f-strings para inserir variáveis em strings.
## - Exemplo: f"Agência:\t{self.agencia}".

## 20. Uso de `*args` e `**kwargs`:
## - Permitem que funções aceitem um número variável de argumentos.
## - Exemplo: `def envelope(*args, **kwargs)` no decorador `log_transacao`.

## 21. Uso de `yield`:
## - Transforma uma função em um gerador, que pode ser iterado.
## - Exemplo: `gerar_relatorio` na classe `Historico`.

## 23. Uso de `super()`:
## - Chama métodos da classe pai.
## - Exemplo: `super().__init__(endereco)` na classe `PessoaFisica`.

## 24. Uso de `Path`:
## - Para manipulação de caminhos de arquivos de forma segura e independente do sistema operacional.
## - Exemplo: `ROOT_PATH = Path(__file__).parent`.

## 25. Uso de `textwrap.dedent`:
## - Remove indentação comum de strings multilinha.
## - Exemplo: `textwrap.dedent(menu)`.

## 26. Uso de `input()`:
## - Para capturar entrada do usuário.
## - Exemplo: `cpf = input("Informe o CPF do cliente: ")`.

## 27. Uso de `print()`:
## - Para exibir informações no console.
## - Exemplo: `print("\n=== Saque realizado com sucesso! ===")`.

## 28. Uso de `return`:
## - Para retornar valores de funções.
## - Exemplo: `return True` no método `sacar`.

## 29. Uso de `pass`:
## - Para indicar um bloco de código vazio.
## - Exemplo: `pass` em funções ou métodos que não têm implementação.

## 30. Uso de `if`, `elif`, `else`:
## - Para controle de fluxo condicional.
## - Exemplo: `if excedeu_saldo:` no método `sacar`.

## 31. Uso de `for`:
## - Para iterar sobre coleções.
## - Exemplo: `for transacao in transacoes:` no método `exibir_extrato`.

## 32. Uso de `while`:
## - Para loops que continuam enquanto uma condição for verdadeira.
## - Exemplo: `while True:` no método `main`.

## 33. Uso de `break`:
## - Para sair de loops.
## - Exemplo: `break` no método `main` para sair do loop infinito.

## 35. Uso de `raise`:
## - Para lançar exceções.
## - Exemplo: `raise StopIteration` no método `__next__`.

## 37. Uso de `None`:
## - Para representar a ausência de valor.
## - Exemplo: `return None` em `recuperar_conta_cliente`.

## 38. Uso de `float`:
## - Para converter strings em números decimais.
## - Exemplo: `valor = float(input("Informe o valor do depósito: "))`.

## 39. Uso de `len`:
## - Para obter o tamanho de uma coleção.
## - Exemplo: `if len(conta.historico.transacoes_do_dia()) >= 2:`.

## 40. Uso de `str`:
## - Para converter objetos em strings.
## - Exemplo: `str(conta)` no método `listar_contas`.

## 41. Uso de `int`:
## - Para converter strings em números inteiros.
## - Exemplo: `numero_conta = len(contas) + 1`.

## 42. Uso de `list`:
## - Para criar e manipular listas.
## - Exemplo: `clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]`.

## 43. Uso de `dict`:
## - Para criar e manipular dicionários.
## - Exemplo: `self._transacoes.append({"tipo": transacao.__class__.__name__, "valor": transacao.valor, "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")})`.

## 44. Uso de `http`: