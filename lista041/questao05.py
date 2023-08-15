'''
5)	Desenvolver um programa que pergunte 4 notas escolares de um aluno e
exiba mensagem informando que o aluno foi aprovado se a média escolar for
maior ou igual a 5. Se o aluno não foi aprovado, indicar uma mensagem
informando essa condição. Apresentar junto com a mensagem de aprovação ou
reprovação o valor da média obtida pelo aluno.
'''

nota1 = float(input("Informe sua Nota 1: "))
nota2 = float(input("Informe sua Nota 2: "))
nota3 = float(input("Informe sua Nota 3: "))
nota4 = float(input("Informe sua Nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if ( media >= 5 ):
    print(f"APROVADO - Média: {media}")
else:
    print(f"REPROVADO - Média: {media}")