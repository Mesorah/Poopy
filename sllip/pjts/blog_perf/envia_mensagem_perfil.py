from bdd import enviar_dados_para_banco_de_dados_perfil, enviar_dados_para_banco_de_dados_msg

"""
    O arquivo guarda_msg.py serve para enviar mensagens ou o perfil para o banco de dados
"""

class EnviaPerfil:
    """ Pega o nome, sobrenome e senha e envia para o banco de dados Perfis """
    def __init__(self, nome, sobrenome, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.senha = senha


    """ Envia o nome, sobrenome e senha para o Perfis """
    def envia_para_o_arquivo_do_banco_de_dados_perfis(self):
        enviar_dados_para_banco_de_dados_perfil(self.nome, self.sobrenome, self.senha)


class EnviaMsg:
    """ Pega o título, mensagem e id_perfil e envia para o banco de dados Mensagens """
    def __init__(self, titulo, mensagem, id_perfil):
        self.titulo = titulo
        self.mensagem = mensagem
        self.id_perfil = id_perfil

    def envia_para_o_arquivo_do_banco_de_dados_mensagem(self):
        enviar_dados_para_banco_de_dados_msg(self.titulo, self.mensagem, self.id_perfil)

    