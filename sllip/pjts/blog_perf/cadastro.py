"""
    O arquivo cadastro.py serve para o usuário cadastrar em uma conta
"""

from bdd import enviar_dados_para_banco_de_dados_perfil

class Cadastro:
    def __init__(self):
        self.nome = None
        self.sobrenome = None
        self.senha = None

    
    """ Para cadastrar o nome do usuário """
    @classmethod
    def nome_usuario(cls):
        cls.nome = input('Qual seu nome? ')

        while True:
            if cls.verifica_letra(cls.nome):
                return cls.nome

            else:
                pass


    """ Para cadastrar o sobrenome do usuário """
    @classmethod
    def sobrenome_usuario(cls):
        cls.sobrenome = input('Qual seu sobrenome? ')

        while True:
            if cls.verifica_letra(cls.sobrenome):
                return cls.sobrenome

            else:
                pass


    """ Para cadastrar a senha do usuário """
    @classmethod
    def senha_usuario(cls):
        cls.senha = input('Crie uma senha: ')

        return cls.senha


    """ Verifica se a palavra é uma string """

    @staticmethod
    def verifica_letra(palavra):
        for letra in palavra:
            if not letra.isalpha():
                return False
            
        return True
    

    """ Verifica se a palavra é uma inteiro """
    @staticmethod
    def verifica_numero(numero):
        try:
            numero = int(numero)
            return True

        except ValueError:
            print('Isto não é um número inteiro')
        
        return False
    
    
    # def envia_para_o_arquivo_do_banco_de_dados_perfis(self):
    #     enviar_dados_para_banco_de_dados_perfil(self.nome, self.sobrenome, self.senha)
