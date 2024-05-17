from perfil import *
from trabalho import *
from loja import *
import bdd

def acoes():
    pass


def get_personagem():
    personagem = Perfil()
    personagem.nome_personagem()
    personagem.exibir_perfil()

    trabalho = EscolhaTrabalho()
    trabalho.escolha_trabalho()

    tra = Trabalho(personagem, trabalho)
    tra.limpador_privado()
    tra.descancar()
    tra.limpador_privado()

    print(tra.maximo_energia)

    lj = Loja(personagem, tra)
    lj.escolha_produto()

    print(tra.maximo_energia)

    return personagem