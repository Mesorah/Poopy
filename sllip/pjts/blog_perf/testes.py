from main import *
from posts import *
from envia_mensagem_perfil import *
from cadastro import *
from login import *
from bdd import *
from ver_posts import *


# escreverpost = EscreverPost()

# titulo = escreverpost.titulo()

# msg = escreverpost.msg_post()

# msg_junta = escreverpost.juncao_msg(titulo, msg)

# gd = GuardaMsg(msg_junta)

# gd.adiciona_msg()

# cd = Cadastro()
# cd.nome_usuario()
# cd.sobrenome_usuario()
# cd.senha_usuario()
# gd = EnviaPerfil(cd.nome, cd.sobrenome, cd.senha)
# gd.envia_para_o_arquivo_do_banco_de_dados_perfis()



# login = Login()

# login.pergunta_infomacoes()

# _id = pega_id(login.nome, login.sobrenome, login.senha)
# print(_id)


# post = EscreverPost()
# tl = post.titulo()
# msg = post.msg_post()

# junc = post.juncao_msg(tl, msg)

# em = EnviaMsg(tl, msg, pega_id(login.nome, login.sobrenome, login.senha))
# em.envia_para_o_arquivo_do_banco_de_dados_mensagem()

vp = VerPosts()
vp.mostrar_post()