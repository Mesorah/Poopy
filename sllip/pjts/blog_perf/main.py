"""
    O main.py serve para ver o menu do codigo, como os posts feitos, com perfis etc

"""

from main import *
from posts import *
from guarda_msg import *
from cadastro import Cadastro

class MenuBlog:
    def __init__(self):
        pass


    def exibir_alternativas(self):
        print('''
[1] ver posts
[2] ver as pessoas''')
        

    def alternativas(self):
        resp = input('R: ') 
        
        while True:
            if Cadastro.verifica_numero(resp):
                self.caminho_alternativas(int(resp))

            else:
                pass

    
    def caminho_alternativas(self, opcao):
        if opcao == 1:
            pass

        elif opcao == 2:
            pass