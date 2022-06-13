"""
Operador ternário em Python
"""

# logged_user = False
#
# if logged_user:
#     msg = 'Usuário logado.'
# else:
#     msg = 'Usuário precisa logar.'
#
# print(msg)

logged_user = True
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

print(msg)