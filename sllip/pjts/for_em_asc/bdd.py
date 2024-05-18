import sqlite3
from contextlib import closing
from pathlib import Path
import testes

from testes import TipoPerfis

"""  Arquivos onde vai ser localizado o banco de dados """
ARQUIVO_BRUTO = Path(__file__).parent
NOME_BANCO_DE_DADOS = 'perfis.db'
ARQUIVO_COMPLETO = ARQUIVO_BRUTO / NOME_BANCO_DE_DADOS

""" Pega os atributos do personagem """
personagem = testes.get_personagem()

nome = TipoPerfis.nome
sobrenome = TipoPerfis.sobrenome
dinheiro = TipoPerfis.dinheiro
trabalho_atual = TipoPerfis.trabalho_atual
experiencia = TipoPerfis.experiencia
energia = TipoPerfis.energia

""" Cria a connection e o cursor """
with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
    with closing(connection.cursor()) as cursor:

        """ Cria a tabela se não existir """
        cursor.execute('CREATE TABLE IF NOT EXISTS Perfis(id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT)')
        
        """ Insere os nomes e os sobrenomes """
        cursor.execute(f'''INSERT INTO Perfis
                       (nome, sobrenome, dinheiro, trabalho_atual, experiencia, energia)
                        Values(?, ?, ?, ?, ?, ?)''', (nome, sobrenome, dinheiro, trabalho_atual, experiencia, energia))