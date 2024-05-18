from perfil import *
from trabalho import *
from loja import *
import bdd
import sqlite3
from contextlib import closing
from pathlib import Path
import os
import sys

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

            if not self.verifica_numero(acao) or int(acao) not in [1, 2, 3, 4, 5, 6, 7]:
                print('Opção inválida!')
                sleep(0.5)
                self.limpa_terminal()
            
            else:
                self.escolha_opcoes(int(acao))

                if int(acao) == 7:
                    break


    """ Printa no terminal as opções que o jogador tem """
    def exibe_opcoes(self):
        print('''
    1- Escolher o trabalho
    2- Trabalhar
    3- Dormir
    4- Loja
    5- Exibir perfil
    6- Salvar
    7- Sair e salvar
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
        print('AAAAAAAAAAAAAAAAAAAAAKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD')

        ARQUIVO_BRUTO = Path(__file__).parent
        NOME_BANCO_DE_DADOS = 'perfis.db'
        # ARQUIVO_COMPLETO = os.path.join(os.path.dirname(__file__), 'perfis.db')

        if getattr(sys, 'frozen', False):  # Se estiver executando como um executável empacotado
            base_dir = os.path.dirname(sys.executable)
        else:  # Se estiver executando como um script Python
            base_dir = os.path.dirname(__file__)

        ARQUIVO_COMPLETO  = os.path.join(base_dir, 'perfis.db')

        with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
            with closing(connection.cursor()) as cursor:
                
                print(ARQUIVO_COMPLETO, 'JFFFKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK')

                print('ESTOU SENDO EXECUTADO DDDDDDDDDDDDDDDDDDDDDDDDDDDD')

                cursor.execute('''
                CREATE TABLE IF NOT EXISTS Perfis(
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    sobrenome TEXT,
                    dinheiro REAL,
                    trabalho_atual TEXT,
                    experiencia INTEGER,
                    energia INTEGER
                )
            ''')
                
                connection.commit()
                
                print('PASSEI POR OUTRO EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')

                cursor.execute('''
                    SELECT nome, sobrenome, dinheiro, trabalho_atual, experiencia, energia FROM Perfis
                    WHERE nome = ? AND sobrenome = ?
                ''', (nome, sobrenome))
                resultado = cursor.fetchone()

                print(cursor.execute('''
                    SELECT nome, sobrenome, dinheiro, trabalho_atual, experiencia, energia FROM Perfis
                    WHERE nome = ? AND sobrenome = ?
                ''', (nome, sobrenome)))

                print('PASSEI PELO ULTIMO FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF')

                if resultado:
                    self.personagem.nome, self.personagem.sobrenome, self.personagem.dinheiro, self.trabalho.trabalho_atual, self.trabalho.experiencia, self.tra.energia = resultado
                    print('Sucesso')
                    return True
                
        print('ERROR')
        return False
        

    """ Função onde executa outras funções com base da escolha do jogador """
    def escolha_opcoes(self, opcao):
        if opcao == 1:
            self.trabalho.escolha_trabalho()

        elif opcao == 2:
            self.tra.faxineiro()

        elif opcao == 3:
            self.tra.descancar()
            sleep(0.4)
            self.limpa_terminal()

        elif opcao == 4:
            self.loja.escolha_produto()

        elif opcao == 5:
            self.exibir_perfil()
        elif opcao == 6 or opcao == 7:       
            bdd.enviar_dados_para_banco_de_dados(self.personagem.nome, self.personagem.sobrenome,
                                              self.personagem.dinheiro, self.trabalho.trabalho[self.trabalho.num_trabalho_atual]['nome_trabalho'],
                                                self.trabalho.experiencia, self.tra.energia)
            
            
        
        else:
            print('opção inexistente')


    """ Verifica se é um numero """
    def verifica_numero(self, numero):
        return numero.isnumeric()
    


jogo = IniciarJogo()
jogo.iniciar_jogo()