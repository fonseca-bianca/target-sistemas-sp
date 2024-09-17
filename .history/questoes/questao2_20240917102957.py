"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor 
sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule 
a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
pertence ou não a sequência.
IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua 
preferência ou pode ser previamente definido no código;
"""

# usuário irá inserir o número por meio de uma entrada
numero = int(input("Informe um número: "))

def pertence_fibonacci(n):
    a = 0
    b = 1
    
    while True:
        if a == n: # verifica se o número da sequência é o mesmo informado pelo usuário
            return True # encerra o loop quando True
        if a > n:
            return False # o inverso do anterior
        a, b = b, a + b

# exibir mensagem se o número informado pertence à sequência de finbonacci ou não
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")