""" O bdd.py serve para se conectar no banco de dados """

import sqlite3
from contextlib import closing
from pathlib import Path
import os
import sys

# Caminho do arquivo onde será localizado o banco de dados
ARQUIVO_BRUTO = Path(__file__).parent
NOME_BANCO_DE_DADOS = 'perfis.db'

if getattr(sys, 'frozen', False):  # Se estiver executando como um executável empacotado
    base_dir = os.path.dirname(sys.executable)
else:  # Se estiver executando como um script Python
    base_dir = os.path.dirname(__file__)

ARQUIVO_COMPLETO = os.path.join(base_dir, 'perfis.db')


""" Cria a tabela perfil se existir, com a foreing_keys ligada """
def cria_tabela_perfil():
    try:

        with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
            connection.execute('PRAGMA foreign_keys = ON;')
            with closing(connection.cursor()) as cursor:

                # Cria a tabela se não existir
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Perfis(
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        sobrenome TEXT NOT NULL,
                        senha TEXT NOT NULL
                    )
                ''')

                connection.commit()

    except sqlite3.Error as e:
        print(f"Erro ao criar tabela Perfis: {e}")


""" Cria a tabela mensagem se existir, com a foreing_keys ligada """
def cria_tabela_msg():
    try:

        with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
            connection.execute('PRAGMA foreign_keys = ON;')
            with closing(connection.cursor()) as cursor:

                # Cria a tabela se não existir
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Mensagens(
                        id INTEGER PRIMARY KEY,
                        titulo TEXT NOT NULL,
                        mensagem TEXT NOT NULL,
                        perfil_id INTEGER,
                        FOREIGN KEY (perfil_id) REFERENCES Perfis (id)
                    )
                ''')

                connection.commit()

    except sqlite3.Error as e:
        print(f"Erro ao criar tabela Mensagens: {e}")


""" Envia para o banco de dados Perfis o nome e o sobrenome """
def enviar_dados_para_banco_de_dados_perfil(nome, sobrenome, senha):
    cria_tabela_perfil()

    try:
        with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
            connection.execute('PRAGMA foreign_keys = ON;')
            with closing(connection.cursor()) as cursor:

                cursor.execute('INSERT INTO Perfis (nome, sobrenome, senha) VALUES (?, ?, ?)', (nome, sobrenome, senha))
                connection.commit()

    except sqlite3.Error as e:
        print(f"Erro ao inserir dados na tabela Perfis: {e}")


""" Envia para o banco de dados Mensagens o título, mensgem e o id do perfil """
def enviar_dados_para_banco_de_dados_msg(titulo, mensagem, perfil_id):
    cria_tabela_msg()

    try:
        with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
            connection.execute('PRAGMA foreign_keys = ON;')
            with closing(connection.cursor()) as cursor:

                cursor.execute('INSERT INTO Mensagens (titulo, mensagem, perfil_id) VALUES (?, ?, ?)', (titulo, mensagem, perfil_id))
                connection.commit()
                
    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade ao inserir dados na tabela Mensagens: {e}")

    except sqlite3.Error as e:
        print(f"Erro ao inserir dados na tabela Mensagens: {e}")


""" Pega o id da pessoa """
def pega_id(nome, sobrenome, senha):
    try:
        with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('SELECT id FROM Perfis WHERE nome = ? AND sobrenome = ? AND senha = ?', (nome, sobrenome, senha))
                resultado = cursor.fetchone()

                if resultado:
                    resultado = resultado[0]

                    return resultado

                return False

    except TypeError as ErroTipo:
        print(f'Id não encontrado {ErroTipo}')


""" Pega as informações como nome, sobrenome, senha do Perfis """
def pega_informacoes(nome, sobrenome, senha):
    try:
        with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('SELECT * FROM Perfis WHERE nome = ? AND sobrenome = ? AND senha = ?', (nome, sobrenome, senha))
                resultado = cursor.fetchone()

                if resultado:
                    print(resultado)

                    return True
                
                return False

    except TypeError as ErroTipo:
        print(f'Id não encontrado {ErroTipo}')


""" Pegar o título das mensagens(posts) """
def pega_informacoes_posts():
    with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('''
                SELECT Mensagens.id, Mensagens.titulo, Perfis.nome, Perfis.sobrenome
                FROM Mensagens
                JOIN Perfis ON Mensagens.perfil_id = Perfis.id
            ''')
                mensagens = cursor.fetchall()

                if not mensagens:
                    return False

                return mensagens
                
            
""" Pega um blog pelo id """
def pega_blog_unico(_id):
    with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('SELECT * FROM Mensagens where id = (?)', _id)
                mensagem = cursor.fetchall()
                if len(mensagem) >= 1:

                    return mensagem
                
                else:
                    print('Texto não encontrado')


""" Mostra todas as pessoas do banco de dados """
def mostra_pessoas_bdd():
    with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute('SELECT nome, sobrenome FROM Perfis')
                pessoas = cursor.fetchall()

                return pessoas
            

""" Verifica se o id da mensagem existe """
def verifica_id_mensagem_bdd(_id):
    with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute('SELECT id FROM Mensagens WHERE id = ?', (_id,))
            resultado = cursor.fetchone()
            
            if resultado:
                return True  # ID existe na tabela

            return False  # ID não existe na tabela


if __name__ == '__main__':
    # enviar_dados_para_banco_de_dados_perfil('João', 'Silva', '2323')
    # enviar_dados_para_banco_de_dados_msg('Olá', 'Esta é uma mensagem', 1) 
    # print(pega_id('João', 'Silva', '23231'))

    pass