"""
    O arquivo cadastro.py serve para o usuário logar em sua conta
"""

class Cadastro:
    def __init__(self):
        pass


    def nome_usuario(self):
        nome = input('Qual seu nome? ')

        while True:
            if self.verifica_letra(nome):
                break

            else:
                pass


    def sobrenome_usuario(self):
        sobrenome = input('Qual seu sobrenome? ')

        while True:
            if self.verifica_letra(sobrenome):
                break

            else:
                pass


    def identificador_usuario(self):
        identificador = input('Crie um identificador(tem que ser único): ')

        while True:
            if self.verifica_identificador(identificador):
                break

            else:
                pass


    def verifica_letra(self, palavra):
        for letra in palavra:
            if not letra.isalpha():
                return False
            
        return True
    

    def verifica_numero(self, numero):
        if isinstance(numero, int):
            return True
        
        return False


    def verifica_identificador(self, identificador):
        pass ## depois que criar o bdd ##