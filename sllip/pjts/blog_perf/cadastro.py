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
    def nome_usuario(self):
        self.nome = input('Qual seu nome? ')

        while True:
            if self.verifica_letra(self.nome):
                return self.nome

            else:
                pass


    """ Para cadastrar o sobrenome do usuário """
    def sobrenome_usuario(self):
        self.sobrenome = input('Qual seu sobrenome? ')

        while True:
            if self.verifica_letra(self.sobrenome):
                return self.sobrenome

            else:
                pass


    """ Para cadastrar a senha do usuário """
    def senha_usuario(self):
        self.senha = input('Crie uma senha: ')

        return self.senha


    """ Verifica se a palavra é uma string """
    def verifica_letra(self, palavra):
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
