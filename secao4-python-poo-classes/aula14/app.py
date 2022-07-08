class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError('Erraado!')

try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')

