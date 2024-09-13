import os
import sqlite3

import pandas as pd

diretorio = os.getcwd()
db_path = os.path.join(diretorio, "Banco_de_Dados", "estoque.db")


def criar_tabela_estoque():
    # Conectar ao banco de dados SQLite
    conexao = sqlite3.connect(db_path)

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Definir o comando SQL para criar a tabela
    query = """
    CREATE TABLE IF NOT EXISTS fisico (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT,
        descricao TEXT,
        qtd INTEGER,
        un TEXT,
        preco REAL,
        codigo_barras TEXT
    );
    """

    # Executar o comando SQL
    cursor.execute(query)

    # Salvar as alterações
    conexao.commit()

    # Fechar a conexão
    conexao.close()

def criar_tabela_entrada():
    # Conectar ao banco de dados SQLite (o arquivo será criado se não existir)
    conexao = sqlite3.connect(db_path)

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Definir o comando SQL para criar a tabela
    query = """
    CREATE TABLE IF NOT EXISTS entrada (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT,
        descricao TEXT,
        qtd INTEGER,
        un TEXT,
        preco REAL,
        codigo_barras TEXT,
        data_entrada DATE,
        mes_entrada TEXT
    );
    """

    # Executar o comando SQL
    cursor.execute(query)

    # Salvar as alterações
    conexao.commit()

    # Fechar a conexão
    conexao.close()

def criar_tabela_saida():
    # Conectar ao banco de dados SQLite (o arquivo será criado se não existir)
    conexao = sqlite3.connect(db_path)

    # Criar um cursor para executar comandos SQL
    cursor = conexao.cursor()
    
    query = """
    CREATE TABLE IF NOT EXISTS saida (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT,
        descricao TEXT,
        qtd INTEGER,
        un TEXT,
        preco REAL,
        area TEXT,
        codigo_barras TEXT,
        data_saida DATE,
        mes_saida TEXT
    );
    """

    # Executar o comando SQL
    cursor.execute(query)

    # Salvar as alterações
    conexao.commit()

    # Fechar a conexão
    conexao.close()


criar_tabela_saida()

criar_tabela_entrada()

criar_tabela_estoque()
