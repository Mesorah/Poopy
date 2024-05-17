from perfil import *
from trabalho import *
from loja import *

class IniciarJogo:
    def __init__(self):
        self.personagem = Perfil()
        self.trabalho = EscolhaTrabalho()
        self.tra = Trabalho(self.personagem, self.trabalho)
        self.loja = Loja(self.personagem, self.tra)

    def iniciar_jogo(self):
        self.personagem.nome_personagem()
        self.personagem.sobrenome_personagem()

        while True:
            self.exibe_opcoes()

            acao = input('O que fazer? ')

            if not self.verifica_numero(acao) or int(acao) not in [1, 2, 3, 4, 5]:
                print('Opção inválida!')
            
            else:
                self.escolha_opcoes(int(acao))

    def exibe_opcoes(self):
        print('''
    1- Escolher o trabalho
    2- Trabalhar
    3- Dormir
    4- Loja
    5- Exibir perfil
    ''') 

    def escolha_opcoes(self, opcao):
        if opcao == 1:
            self.trabalho.escolha_trabalho()

        elif opcao == 2:
            self.tra.limpador_privado()

        elif opcao == 3:
            self.tra.descancar()

        elif opcao == 4:
            self.loja.escolha_produto()

        elif opcao == 5:
            self.personagem.exibir_perfil()

    def verifica_numero(self, numero):
        return numero.isnumeric()

jogo = IniciarJogo()
jogo.iniciar_jogo()
