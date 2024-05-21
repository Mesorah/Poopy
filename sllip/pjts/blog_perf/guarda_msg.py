from posts import *

"""
    O arquivo guarda_msg.py serve para guardas os posts das pessoas
"""

class GuardaMsg:
    def __init__(self, post):
        self.post = post

        self.mensagens = []


    def guarda_msg(self, _id, nome, msg):

        self.mensagens.append(
            {'id': _id, 'nome': nome, 'msg': msg}
        )

        return self.mensagens

    def adiciona_msg(self):
        self.guarda_msg(self._id, self.nome, self.post)