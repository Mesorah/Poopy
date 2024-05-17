import sqlite3
from contextlib import closing
from pathlib import Path
import perfil
import testes

"""  Arquivos onde vai ser localizado o banco de dados """
ARQUIVO_BRUTO = Path(__file__).parent
NOME_BANCO_DE_DADOS = 'perfis.db'
ARQUIVO_COMPLETO = ARQUIVO_BRUTO / NOME_BANCO_DE_DADOS

""" Pega os atributos do personagem """
personagem = testes.get_personagem()

""" Cria a connection e o cursor """
with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
    with closing(connection.cursor()) as cursor:

        """ Cria a tabela se não existir """
        cursor.execute('CREATE TABLE IF NOT EXISTS Perfis(id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT)')
        
        """ Insere os nomes e os sobrenomes """
        cursor.execute(f'INSERT INTO Perfis(nome, sobrenome) Values(?, ?)', (personagem.nome, personagem.sobrenome))