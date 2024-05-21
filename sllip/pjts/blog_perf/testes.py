from main import *
from posts import *
from guarda_msg import *


escreverpost = EscreverPost()

titulo = escreverpost.titulo()

msg = escreverpost.msg_post()

msg_junta = escreverpost.juncao_msg(titulo, msg)

gd = GuardaMsg(msg_junta)

gd.adiciona_msg()