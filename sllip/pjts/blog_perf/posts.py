"""
    posts.py serve para o arquivo no qual resultara na escrita dos posts
"""


class EscreverPost:
    def __init__(self):
        pass


    def titulo(self):
        print('Escreva seu título')

        titulo_usuario = input('R: ')

        return titulo_usuario


    def msg_post(self):
        print('Escreva sua msg')
        
        mensagem_usuario = input('R: ')

        return mensagem_usuario

    
    def juncao_msg(self, titulo, msg, _id):
        mensagem_completa = f''' Título {titulo}

id{_id}    Texto: {msg} '''
        
        return mensagem_completa