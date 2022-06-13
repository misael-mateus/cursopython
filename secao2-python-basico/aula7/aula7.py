nome = "Danniel"
idade = 32
altura = 1.71
e_maior = idade > 18
peso = 72
imc = peso / (altura ** 2) # outra forma de fazer peso / (altura * altura)

print(nome, 'tem', idade, 'anos de idade e seu imc é: ', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é: {imc:.2f}')
print('{} tem {} anos de idade e seu imc é: {:.2f}'.format(nome, idade, imc))
print('{2} tem {1} anos de idade e seu imc é: {0}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é: {im}'.format(n=nome, i=idade, im=imc))
