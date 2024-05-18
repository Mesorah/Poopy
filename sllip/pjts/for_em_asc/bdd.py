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

ARQUIVO_COMPLETO  = os.path.join(base_dir, 'perfis.db')


def enviar_dados_para_banco_de_dados(nome, sobrenome, dinheiro, trabalho_atual, experiencia, energia):
    with sqlite3.connect(ARQUIVO_COMPLETO) as connection:
        with closing(connection.cursor()) as cursor:
            

            # Cria a tabela se não existir
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


            # Verifica se o perfil já existe
            cursor.execute('''
                SELECT id FROM Perfis
                WHERE nome = ? AND sobrenome = ?
            ''', (nome, sobrenome))
            resultado = cursor.fetchone()


            if resultado:
                # Atualiza o perfil existente
                cursor.execute('''
                    UPDATE Perfis
                    SET dinheiro = ?, trabalho_atual = ?, experiencia = ?, energia = ?
                    WHERE id = ?
                ''', (dinheiro, trabalho_atual, experiencia, energia, resultado[0]))

            else:
                # Insere um novo perfil
                cursor.execute('''
                    INSERT INTO Perfis
                    (nome, sobrenome, dinheiro, trabalho_atual, experiencia, energia)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (nome, sobrenome, dinheiro, trabalho_atual, experiencia, energia))

            # cursor.execute('DELETE FROM perfis')
            connection.commit()

