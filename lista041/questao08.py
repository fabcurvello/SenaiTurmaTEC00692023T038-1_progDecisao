'''
8)	Desenvolver um programa que pergunte um número inteiro qualquer
e verifique se ele está na faixa de 1 a 10.
'''

num = int(input("Informe um número: "))

#lógica do op ternário1: var = (se for falso, se for verdadeiro)[teste condicional]
resposta = (f"{num} não está na faixa de 1 a 10", f"{num} está na faixa de 1 a 10")[num >= 1 and num <= 10]

print(resposta)