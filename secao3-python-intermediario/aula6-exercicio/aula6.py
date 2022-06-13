"""
1 - Crie uma função1 que recebe uma função2 como parânetro e retorne o valor da
função2 executada.
"""
# def ola_mundo():
#     return 'Olá mundo!'
#
# def mestre(funcao):
#     return funcao()
#
# executando = mestre(ola_mundo)
# print(executando)

"""
2 - Crie uma função1 que receba uma função2 como parâmetro como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número
diferente de argumentos.
"""
def func1(nome):
    return nome
def func2(idade):
    return idade
def func_mestre(*args):
    print(args)

func_mestre('Danniel', 32)
