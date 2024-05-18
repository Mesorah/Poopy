import sqlite3 
from contextlib import closing
from pathlib import Path

class Perfil:
    def __init__(self):
        self.nome = None
        self.sobrenome = None
        self.dinheiro = 0


    """
        Pede para o usuário colocar o nome do personagem
    """
    def nome_personagem(self):
        while True:
            self.nome = input('Nome: ')

            if self.verifica_string(self.nome):
                print('ok')
                break
            
            else:
                print('ue')


    """
        Pede para o usuário colocar o sobrenome do personagem
    """
    def sobrenome_personagem(self):
        while True:
            self.sobrenome = input('Sobrenome: ')

            if self.verifica_string(self.sobrenome):
                print('ok')
                break
            
            else:
                print('ue')

    """ Alterações de nome """

    """ Carrega o perfil do banco de dados """
    def carregar_perfil(self, nome, sobrenome):
        ARQUIVO_BRUTO = Path(__file__).parent
        NOME_BANCO_DE_DADOS = 'perfis.db'
        ARQUIVO_COMPLETO = ARQUIVO_BRUTO / NOME_BANCO_DE_DADOS

        with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('''
                    SELECT nome, sobrenome, dinheiro FROM Perfis
                    WHERE nome = ? AND sobrenome = ?
                ''', (nome, sobrenome))
                resultado = cursor.fetchone()

                if resultado:
                    self.nome, self.sobrenome, self.dinheiro = resultado
                    return True

        return False


    """ Altera o nome do personagem para um novo """
    def altera_nome(self):
        novo_nome = input('Qual seu novo nome? ')

        if self.verifica_string(novo_nome):
            self.nome = novo_nome


            print('Nome alterado com sucesso!')
        else:
            print('O nome deve conter apenas letras.')


    """ Altera o sobrenome do personagem para um novo """
    def altera_sobrenome(self):
        novo_sobrenome = input('Qual seu novo sobrenome? ')

        if self.verifica_string(novo_sobrenome):
            self.sobrenome = novo_sobrenome


            print('sobrenome alterado com sucesso!')
        else:
            print('O sobrenome deve conter apenas letras.')


    """
        Verifica se a variável é uma string
    """
    def verifica_string(self, nome):
        for letra in nome:
            if not letra.isalpha():
                return False
            
        return True
    