from perfil import *
from trabalho import *
from loja import *
import bdd
import sqlite3
from contextlib import closing
from pathlib import Path
import os

class IniciarJogo:
    """ Inicias as outras classes, para não perder os dados """
    def __init__(self):
        self.personagem = Perfil()
        self.trabalho = EscolhaTrabalho()
        self.tra = Trabalho(self.personagem, self.trabalho)
        self.loja = Loja(self.personagem, self.tra)
    

    """ Limpa o terminal da pessoa """
    @staticmethod
    def limpa_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')


    """ Loop para começar o jogo e chamadas de funções """
    def iniciar_jogo(self):

        while True:
            print('Você tem algum perfil salvo?[s/n]')

            resp_perfil_salvo = input(': ').lower()
            self.limpa_terminal()

            if resp_perfil_salvo[0] == 's':
                nome = input("Digite o nome do personagem: ")
                self.limpa_terminal()

                sobrenome = input("Digite o sobrenome do personagem: ")
                self.limpa_terminal()

                if self.carregar_perfil(nome, sobrenome):
                    print('Perfil encontrado')
                    sleep(0.4)
                    self.limpa_terminal()
                    break

                else:
                    print('Perfil não encontrado')
                    sleep(0.8)
                    self.limpa_terminal()

            elif resp_perfil_salvo[0] == 'n':
                self.personagem.nome_personagem()
                self.limpa_terminal()
                self.personagem.sobrenome_personagem()
                self.limpa_terminal()
                break


        while True:
            self.exibe_opcoes()

            acao = input('O que fazer? ')
            self.limpa_terminal()

            if not self.verifica_numero(acao) or int(acao) not in [1, 2, 3, 4, 5, 6]:
                print('Opção inválida!')
                sleep(0.5)
                self.limpa_terminal()
            
            else:
                self.escolha_opcoes(int(acao))

                if int(acao) == 6:
                    break


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
        

    """ Carrega o perfil do banco de dados """
    def carregar_perfil(self, nome, sobrenome):
        ARQUIVO_BRUTO = Path(__file__).parent
        NOME_BANCO_DE_DADOS = 'perfis.db'
        ARQUIVO_COMPLETO = ARQUIVO_BRUTO / NOME_BANCO_DE_DADOS

        with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('''
                    SELECT nome, sobrenome, dinheiro, trabalho_atual, experiencia, energia FROM Perfis
                    WHERE nome = ? AND sobrenome = ?
                ''', (nome, sobrenome))
                resultado = cursor.fetchone()

                if resultado:
                    self.personagem.nome, self.personagem.sobrenome, self.personagem.dinheiro, self.trabalho.trabalho_atual, self.trabalho.experiencia, self.tra.energia = resultado
                    #self.nome, self.sobrenome, self.dinheiro, self.trabalho_atual, self.experiencia, self.energia = resultado
                    print('opaaaa')
                    return True
        print('etaaaa')
        return False
        

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
            sleep(0.4)
            self.limpa_terminal()

        elif opcao == 4:
            self.loja.escolha_produto()

        elif opcao == 5:
            self.exibir_perfil()
        #######################
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

