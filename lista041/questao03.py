'''
3)	Desenvolver um programa que pergunte um número,
e apresente como resposta se o referido número é par ou é ímpar.
'''

num = int(input("Informe um número: "))

resto = num % 2

if ( resto == 0 ):
    print(f"{num} é par!")
else:
    print(f"{num} é ímpar!")