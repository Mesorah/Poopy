from perfil import *
from trabalho import *
from loja import *
import bdd

class IniciarJogo:
    """ Inicias as outras classes, para não perder os dados """
    def __init__(self):
        self.personagem = Perfil()
        self.trabalho = EscolhaTrabalho()
        self.tra = Trabalho(self.personagem, self.trabalho)
        self.loja = Loja(self.personagem, self.tra)

    """ Loop para começar o jogo e chamadas de funções """
    def iniciar_jogo(self):
        nome = input('Digite seu nome: ')
        sobrenome = input('Digite seu sobrenome: ')

        if not self.personagem.carregar_perfil(nome, sobrenome):
            print('Perfil não encontrado. Criando um novo perfil.')
            self.personagem.nome = nome
            self.personagem.sobrenome = sobrenome

            """
                perfil.py

                , self.trabalho_atual, self.experiencia, self.energia



                testes.py

                else:
            # Carrega o trabalho atual, experiência e energia
            self.trabalho.experiencia = self.personagem.experiencia
            self.tra.energia = self.personagem.energia
            # Encontrar o trabalho pelo nome
            for idx, trabalho in enumerate(self.trabalho.trabalho):
                if trabalho['nome_trabalho'] == self.personagem.trabalho_atual:
                    self.trabalho.num_trabalho_atual = idx
                    break
            """


        while True:
            self.exibe_opcoes()

            acao = input('O que fazer? ')

            if not self.verifica_numero(acao) or int(acao) not in [1, 2, 3, 4, 5, 6]:
                print('Opção inválida!')
            
            else:
                self.escolha_opcoes(int(acao))


    """ Printa no terminal as opções que o jogador tem """
    def exibe_opcoes(self):
        print('''
    1- Escolher o trabalho
    2- Trabalhar
    3- Dormir
    4- Loja
    5- Exibir perfil
    6- Sair e salvar
    ''') 
    

    """ Exibe todo o perfil do jogador """
    def exibir_perfil(self):
        print(f'''
Nome: {self.personagem.nome}
Sobrenome: {self.personagem.sobrenome}
Dinheiro: {self.personagem.dinheiro}
Trabalho atual: {self.trabalho.trabalho[self.trabalho.num_trabalho_atual]['nome_trabalho']}
Experiencia: {self.trabalho.experiencia}
Energia {self.tra.energia}
''')
        

    """ Função onde executa outras funções com base da escolha do jogador """
    def escolha_opcoes(self, opcao):
        if opcao == 1:
            self.trabalho.escolha_trabalho()

        elif opcao == 2:
            # self.tra.self.trabalho.trabalho[self.trabalho.num_trabalho_atual]['nome_trabalho']()
            # print(self.trabalho.trabalho[self.trabalho.num_trabalho_atual]['nome_trabalho'])
            self.tra.faxineiro()

        elif opcao == 3:
            self.tra.descancar()

        elif opcao == 4:
            self.loja.escolha_produto()

        elif opcao == 5:
            self.exibir_perfil()

        elif opcao == 6:       
            bdd.enviar_dados_para_banco_de_dados(self.personagem.nome, self.personagem.sobrenome,
                                              self.personagem.dinheiro, self.trabalho.trabalho[self.trabalho.num_trabalho_atual]['nome_trabalho'],
                                                self.trabalho.experiencia, self.tra.energia)
            
            return
            
        
        else:
            print('opção inexistente')


    """ Verifica se é um numero """
    def verifica_numero(self, numero):
        return numero.isnumeric()
    


jogo = IniciarJogo()
jogo.iniciar_jogo()
