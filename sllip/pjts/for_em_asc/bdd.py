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

with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS Perfis(id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT)')
        
        cursor.execute(f'INSERT INTO Perfis(nome, sobrenome) Values(?, ?)', (personagem.nome, personagem.sobrenome))