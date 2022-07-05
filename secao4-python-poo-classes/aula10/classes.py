class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} Comprando...')

    def falar(self):
        print('Estou em CLIENTE.')

# class Aluno(Pessoa):
#     def estudar(self):
#         print(f'{self.nomeclasse} Estudando...')

class ClienteVIP(Cliente):
    def falar(self):
        super().falar()
        print('Outra coisa qualquer')