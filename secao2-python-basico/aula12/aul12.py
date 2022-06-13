"""
Operadores Lógicos - Aula 4
and, or, not
in e not in
"""
usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Danniel'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Usuário logado')
else:
    print('Usuário ou senha inválidos.')
