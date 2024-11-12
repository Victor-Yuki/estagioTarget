"""
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de
informar a quantidade de vezes em que ela ocorre.
"""

string = input("Entre com uma string: ")
qntdd_a = 0
for _ in string.lower():
    if _ in ['a']:
        qntdd_a += 1
if qntdd_a == 0:
    print(f"Não tem 'a' na string: [{string}].")
else:
    print(f"Tem 'a' na string: [{string}]. Contagem de 'a': {qntdd_a}.")
