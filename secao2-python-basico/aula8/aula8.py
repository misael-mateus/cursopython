"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
nome = "Danniel"
idade = 32
altura = 1.71
peso = 72
ano_atual = 2022
ano_de_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f"{nome} tem {idade} anos e {altura} de altura e pesa {peso}kg.")
print(f"O IMC de {nome} é {imc:.2f}.")
print(f"{nome} nasceu em {ano_de_nascimento}.")
