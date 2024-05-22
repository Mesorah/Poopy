"""
    posts.py serve para o arquivo no qual resultara na escrita dos posts
"""


class EscreverPost:
    def __init__(self):
        pass


    """ Onde a pessoa irá escrever seu título da mensagem """
    def titulo(self):
        print('Escreva seu título')

        titulo_usuario = input('R: ')

        return titulo_usuario


    """ Onde a pessoa irá escrever sua mensagem """
    def msg_post(self):
        print('Escreva sua msg')
        
        mensagem_usuario = input('R: ')

        return mensagem_usuario

    
    """ Onde junta a msg com o título """
    def juncao_msg(self, titulo, msg):
        mensagem_completa = f''' Título {titulo}

Texto: {msg} '''
        
        return mensagem_completa