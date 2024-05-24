"""
    O main.py serve para ver o menu do codigo, como os posts feitos, com perfis etc

"""

from posts import *
from envia_mensagem_perfil import *
from cadastro import *
from ver_posts import *
from mostrar_pessoas import *
from login import *
from bdd import *

from time import sleep

class MenuBlog:
    def __init__(self):
        self.nome = None
        self.sobrenome = None
        self.senha = None

        cria_tabela_perfil()
        cria_tabela_msg()


    """ Limpa o terminal da pessoa """
    @staticmethod
    def limpa_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    
    """ Exibe as informações que o usuário pode fazer """
    def exibir_alternativas(self):
        print('''
[1] ver posts
[2] ver as pessoas
[3] escrever um blog              
[4] sair''')
        

    """ Pega a resposta do usuário """
    def alternativas(self):
        while True:
            self.exibir_alternativas()

            resp = input('R: ') 

            if Cadastro.verifica_numero(resp):
                if int(resp) == 4:
                    print('fechando....')
                    sleep(1)
                    self.limpa_terminal()
                    break

                self.caminho_alternativas(int(resp))
            
            else:
                print("Entrada inválida. Tente novamente.")
                sleep(1)
                self.limpa_terminal()

    
    """ Envia para um função depedendo das alternativas do usuário """
    def caminho_alternativas(self, opcao):
        if opcao == 1:
            sleep(1)
            self.limpa_terminal()
            vp = VerPosts()
            vp.mostrar_post()
            vp.resposta_usuario()


        elif opcao == 2:
            sleep(1)
            self.limpa_terminal()
            mp = MostrarPessoas()
            mp.mostrar_todas_pessoas()

        elif opcao == 3:
            sleep(1)
            self.limpa_terminal()
            ep = EscreverPost()
            tl = ep.titulo()
            msg = ep.msg_post()
            ep.juncao_msg(tl ,msg)
            self.limpa_terminal()

            em = EnviaMsg(tl, msg, pega_id(self.nome, self.sobrenome, self.senha))
            em.envia_para_o_arquivo_do_banco_de_dados_mensagem()

        elif opcao == 4:
            pass

        else:
            print('Opção inválida')
            sleep(1)
            self.limpa_terminal()


    """ Incia o jogo, falando para o usuário colocar seu nome, sobrenome e senha """
    def iniciar_jogo(self):
        while True:
            print('Você tem algum perfil salvo? [s/n]')

            resp = input()[0].lower()

            if resp == 's':
                login = Login()
                login.pergunta_infomacoes()
                
                sleep(1)
                self.limpa_terminal()

                self.nome = login.nome
                self.sobrenome = login.sobrenome
                self.senha = login.senha

                if login.verifica_perfil():
                    self.limpa_terminal()
                    self.continuando_jogo()
                    break
            
                else:
                    sleep(1)
                    self.limpa_terminal()

            else:

                self.nome = Cadastro.nome_usuario()
                self.sobrenome = Cadastro.sobrenome_usuario()
                self.senha = Cadastro.senha_usuario()

                em = EnviaPerfil(self.nome, self.sobrenome, self.senha)
                em.envia_para_o_arquivo_do_banco_de_dados_perfis()

                sleep(1)
                self.limpa_terminal()
                self.continuando_jogo()


    """ Leva para as alternativas """
    def continuando_jogo(self):
        self.alternativas()




if __name__ == "__main__":
    mb = MenuBlog()
    mb.iniciar_jogo()

    # mb.alternativas()

# mb.iniciar_jogo()