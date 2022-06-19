try:
    a = []
except NameError as erro:
    print('Erro')
except IndexError as erro:
    print('Erro de índice.')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    print('Seu código foi executado com sucesso!')
finally:
    a = ''
    


print('Continua...')