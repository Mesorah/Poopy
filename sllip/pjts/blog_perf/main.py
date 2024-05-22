"""
    O main.py serve para ver o menu do codigo, como os posts feitos, com perfis etc

"""

from main import *
from posts import *
from envia_mensagem_perfil import *
from cadastro import Cadastro
from ver_posts import VerPosts

class MenuBlog:
    def __init__(self):
        pass

    
    """ Exibe as informações que o usuário pode fazer """
    def exibir_alternativas(self):
        print('''
[1] ver posts
[2] ver as pessoas''')
        

    """ Pega a resposta do usuário """
    def alternativas(self):
        self.exibir_alternativas()
        while True:
            resp = input('R: ') 

            if Cadastro.verifica_numero(resp):
                self.caminho_alternativas(int(resp))
                break
            else:
                print("Entrada inválida. Tente novamente.")

    
    """ Envia para um função depedendo das alternativas do usuário """
    def caminho_alternativas(self, opcao):
        if opcao == 1:
            vp = VerPosts()
            vp.mostrar_post()

        elif opcao == 2:
            pass

        else:
            print('Opção inválida')


    def iniciar_jogo(self):
        pass

if __name__ == "__main__":
    mb = MenuBlog()
    mb.alternativas()

# mb.iniciar_jogo()