""" O arquivo mostrar_pessoas.py serve para mostrar todas as pessoas(nome, sobrenome) do banco de dados """

from bdd import mostra_pessoas_bdd

class MostrarPessoas:
    def __init__(self):
        pass


    """ Mostra todas as pessoas """ 
    def mostrar_todas_pessoas(self):
        nome = mostra_pessoas_bdd()

        for pessoas in nome:

            print(f'Nome: {pessoas[0]} {pessoas[1]}')


if __name__ == '__main__':
    mp = MostrarPessoas()
    mp.mostrar_todas_pessoas()