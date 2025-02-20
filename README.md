
<div style="text-align: center; font-size: 40px;">Dio Financy Sys Project</div>


# Implementar as seguintes funcionalidades no sistema: 

### 1. Decorador de log

### 2. Gerador de relatórios

### 3. Iterador personalizado

### 4. Data e hora



* Implemente um decorador que seja aplicado a todas as funções de transações (depósito, saque, criação de conta, etc). Esse decorador deve registrar (printar) a data e hora de cada transação, bem como o tipo de transação.

* Criar um gerador que permita iterar sobre as transações de uma conta e retorne, uma a uma, as transações que foram realizadas. Esse gerador deve também ter uma forma de filtrar as transações baseado em seu tipo (por exemplo, apenas saques ou apenas depósitos). 

* Implemente um iterador personalizado ContaIterador que permita iterar sobre todas as contas do banco, retornando informações básicas de cada conta (número, saldo atual, etc).

* Estabelecer um limite de 10 transações diárias para uma conta
Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia.
Mostre no extrato, a data e hora de todas as transações.

* Modificar o atual decorador de **log**, que imprime informações no console, para que ele salve essas informações em um arquivo de log, possibilitando uma revisão mais fácil e uma análise mais detalhada das operações dos usuários.

* O decorador deve registrar o seguinte para cada chamada de função:
1. Data e hora atuais  
2. Nome da função  
3. Argumentos da função  
4. Valor retornado pela função  
5. O arquivo de log deve ser chamado **log.txt**  
6. Se o arquivo **log.txt** já existir, os novos logs devem ser adicionados ao final do arquivo  
7. Cada entrada de log deve estar em uma nova linha.


