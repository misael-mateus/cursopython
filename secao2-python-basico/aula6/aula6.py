"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = "Danniel"
idade = 32
altura = 1.71
e_maior = idade > 18
peso = 72
imc = peso / (altura ** 2) # outra forma de fazer peso / (altura * altura)

print(nome, 'tem', idade, 'anos de idade e seu imc é: ', imc)
