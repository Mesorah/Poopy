from perfil import *
import bdd
from trabalho import *

def acoes():
    pass


def get_personagem():
    personagem = Perfil()
    personagem.nome_personagem()
    personagem.exibir_perfil()
    trabalho = Trabalho()
    trabalho.trabalhin(personagem.nome, personagem.sobrenome)

    return personagem