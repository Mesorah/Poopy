from perfil import *
from trabalho import *
from loja import *
import bdd


personagem = Perfil()
trabalho = EscolhaTrabalho()
tra = Trabalho(personagem, trabalho)
loja = Loja(personagem, tra)

class InicarJogo:
    def __init__(self, personagem, trabalho, tra, loja):
        self.personagem = personagem
        self.trabalho = trabalho
        self.tra = tra
        self.loja = loja

    def iniciar_jogo(self):
        personagem = Perfil()
        personagem.nome_personagem()
        personagem.sobrenome_personagem()

        while True:
            self.exibe_opcoes()

            acao = input('o que fazer? ')

            if not self.verifica_numero(acao) or int(acao) not in [1, 2, 3, 4]:
                print('ue')
            
            else:

                self.escolha_opcoes(int(acao))

        personagem = get_personagem()


    def exibe_opcoes(self):
        print('''
    1- [Escolher o trabalho]
    2- [Trabalhar]
    3- [Dormir]
    4- [Loja]
    5- [Exibir perfil]
    ''') 
        
    def escolha_opcoes(self, opcao):
        if opcao == 1:
            trabalho = EscolhaTrabalho()
            trabalho.escolha_trabalho()

        elif opcao == 2:
            tra = Trabalho(Perfil(), EscolhaTrabalho())
            tra.limpador_privado()

        elif opcao == 3:
            tra = Trabalho(Perfil(), EscolhaTrabalho())
            tra.descancar()

        elif opcao == 4:
            lj = Loja(Perfil(), Trabalho(Perfil(), EscolhaTrabalho()))
            lj.escolha_produto()

        elif opcao == 5:
            pass


        else:
            print('Ué')


    def get_personagem(self):
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


    """ Verifica se o que ele mandou é um número """
    def verifica_numero(self, numero):
        for caracter in numero:
            if not caracter.isnumeric():
                return False

        return True

inicio = InicarJogo()

inicio.iniciar_jogo()