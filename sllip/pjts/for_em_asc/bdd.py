import sqlite3
from contextlib import closing
from pathlib import Path
import perfil
import testes

ARQUIVO_BRUTO = Path(__file__).parent
NOME_BANCO_DE_DADOS = 'perfis.db'
ARQUIVO_COMPLETO = ARQUIVO_BRUTO / NOME_BANCO_DE_DADOS



with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
    with closing(connection.cursor()) as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS Perfis(id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT)')
        
        cursor.execute(f'INSERT INTO Perfis(nome, sobrenome) Values(?, ?)', (testes.personagem.nome, testes.personagem.sobrenome))