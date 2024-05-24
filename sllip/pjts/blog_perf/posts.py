"""
    posts.py serve para o arquivo no qual resultara na escrita dos posts
"""


class EscreverPost:
    def __init__(self):
        pass


    """ Onde a pessoa irá escrever seu título da mensagem """
    @staticmethod
    def titulo():
        print('Escreva seu título')

        titulo_usuario = input('R: ')

        return titulo_usuario


    """ Onde a pessoa irá escrever sua mensagem """
    @staticmethod
    def msg_post():
        print('Escreva sua msg')
        
        mensagem_usuario = input('R: ')

        return mensagem_usuario

    
    """ Onde junta a msg com o título """
    @staticmethod
    def juncao_msg(titulo, msg):
        mensagem_completa = f''' Título {titulo}

Texto: {msg} '''
        
        return mensagem_completa