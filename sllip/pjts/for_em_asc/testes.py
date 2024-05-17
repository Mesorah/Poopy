from perfil import *
import bdd
from trabalho import *

def acoes():
    pass


def get_personagem():
    personagem = Perfil()

    personagem.nome_personagem()
    personagem.exibir_perfil()

    trabalho = EscolhaTrabalho()
    trabalho.escolha_trabalho()


    return personagem