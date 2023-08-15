'''
12)	Desenvolver um programa que pergunte 5 números inteiros e identifique
o maior número e o menor número.
'''

n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))
n3 = int(input("Informe outro número: "))
n4 = int(input("Informe outro número: "))
n5 = int(input("Informe o último número: "))

maior = n1

if ( maior < n2 ):
    maior = n2

if ( maior < n3 ):
    maior = n3

if ( maior < n4 ):
    maior = n4

if ( maior < n5 ):
    maior = n5

menor = n1

if ( menor > n2 ):
    menor = n2

if ( menor > n3 ):
    menor = n3

if ( menor > n4 ):
    menor = n4

if ( menor > n5 ):
    menor = n5

print(f"O maior valor inserido foi {maior}")
print(f"O menor valor inserido foi {menor}")