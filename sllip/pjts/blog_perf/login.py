"""
    O arquivo login.py serve para o usuário que já tem sua conta para logar 
"""

from bdd import pega_id, pega_informacoes

class Login:
    def __init__(self):
        self.nome = None
        self.sobrenome = None
        self.senha = None


    """ Pergunta nome, sobrenome, senha """
    def pergunta_infomacoes(self):
        self.nome = input('qual seu nome? ').strip()
        self.sobrenome = input('qual seu sobrenome? ').strip()
        self.senha = input('qual sua senha? ').strip()


    """ Verifica se o perfil existe """
    def verifica_perfil(self):
        if pega_id(self.nome, self.sobrenome, self.senha):
            print('logou')
            self.carrega_perfil()

            return True

        else:
            print('perfil não encontrado')
            
            return False


    """ Pega as informações como nome, sobrenome, senha do bdd.py """
    def carrega_perfil(self):
        
        pega_informacoes(self.nome, self.sobrenome, self.senha)