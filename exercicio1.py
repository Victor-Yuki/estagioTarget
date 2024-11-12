"""
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores 
anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado 
um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou 
não a sequência.
"""


def gerar_fibonacci_ate(n):
    seq = [0, 1]
    while n > seq[-1]:
        prox = seq[-1] + seq[-2]
        seq.append(prox)
    return seq


num = int(input("Entre com um número para ser analizado: "))
sequencia = gerar_fibonacci_ate(num)
if num in sequencia:
    print(f'{num} pertence à sequência de Fibonacci.')
else:
    print(f'{num} não pertence à sequência de Fibonacci.')