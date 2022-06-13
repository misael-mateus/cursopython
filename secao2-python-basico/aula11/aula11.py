"""
Operadores Relacionais - Aula 4
== igualdade > maior que
>= maqior que ou igual
< menor que
<= menor que ou igual a
!= diferente
"""
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

#Limite para pegar empréstime
idade_limite = 18

if idade >= idade_limite:
    print(f"{nome} pode pegar o empréstimo.")
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')

