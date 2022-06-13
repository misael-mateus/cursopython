"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
# def saudacao(saudacao, nome):
#     print(saudacao, nome)
#
# var = saudacao('Olá', 'Danniel')

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
"""
# def numeros(n1, n2, n3):
#     soma = n1 + n2 + n3
#     print(soma)
#
# numeros(2, 4, 5)

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um 
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado 
do aumento do percentual do mesmo.
"""
# def funcao(valor, percentual):
#     return valor + (valor * percentual /100)
#
# ap = funcao(15, 100)
# print(ap)

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado
"""
def fizz_buzz(n):
    if n % 5 == 0 and n % 3 == 0:
        return 'FizzBuzz'
    if n % 5 == 0:
        return "buzz"
    if n % 3 == 0:
        return 'Fizz'
    return n

# print(fizz_buzz(7))
# print(fizz_buzz(10))
# print(fizz_buzz(15))
# print(fizz_buzz(22))

for i in range(100):
    fizz_buzz(i)
    print(fizz_buzz(i))
