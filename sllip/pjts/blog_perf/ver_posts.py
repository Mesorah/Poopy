""" O arquivo ver_posts.py serve para ver todos os posts que existem no banco de dados """

from bdd import pega_informacoes_posts, pega_blog_unico, verifica_id_mensagem_bdd
from cadastro import *


class VerPosts:
    def __init__(self):
        pass

    
    """ Mostra os posts dos blogs, (apenas id, título e nome) """
    def mostrar_post(self):
        if pega_informacoes_posts():

            valores = pega_informacoes_posts()

            print('Qual blog você quer acesasar?')

            for blogs in valores:
                _id, titulo, nome, sobrenome = blogs

                nome_completo = ' '.join(nome).replace(' ', '')

                print(f'Título: {titulo}, Nome: {nome_completo} {sobrenome} Id: {_id}')

            self.resposta_usuario()

        else:
            print('Nenhum blog encontrado')

    
    """ Pega a resposta do usuário """
    def resposta_usuario(self):
        while True:
            resp = input('R: ')

            if Cadastro.verifica_numero(resp) and verifica_id_mensagem_bdd(int(resp)):

                return self.acessar_unico_blog(resp)
            
            else:
                print('Número incorreto')


    """ Printa o blog que o usuario escolheu em resposta_usuario """
    def acessar_unico_blog(self, resp):
        resultado = pega_blog_unico(resp)

        for blog in resultado:
            print(f'''Título: {blog[1]}
Texto: {blog[2]}''')


if __name__ == '__main__':
    vp = VerPosts()
    vp.mostrar_post()
    vp.resposta_usuario()