# -*- coding: utf-8 -*-
# @Author: Bruno Piato
# @Date:   2026-03-18 16:10:49
# @Last Modified by:   Bruno Piato
# @Last Modified time: 2026-03-31 16:09:50

import sqlite3
from pathlib import Path

import pandas as pd

# caminho do banco
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "database.db"

def listar_estoque():
    """Função para listar os estoques que existem na base de dados em forma de tabela.

    Returns:
        pd.DataFrame: DataFrame de Pandas com todos os estoques cadastrados.

    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
                    SELECT
                        id_item,
                        nome,
                        qtd_estoque,
                        preco,
                        descricao,
                        data_atualizacao
                    FROM estoque
                    """)
    estoque = cursor.fetchall()
    conn.close()

    return  pd.DataFrame(estoque, columns=[
        'ID', 'Nome', 'Quantidade em Estoque', 'Preço', 'Descrição', 'Data de Atualização'])


def executar_query(query, params=()):
    """Função auxiliar para reduzir repetição de código de conexão."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def cadastrar_novo_componente(nome, qtd, preco, descricao):
    """Cadastro um novo componente na tabela."""
    query = """
        INSERT INTO estoque (nome, qtd_estoque, preco, descricao)
        VALUES (?, ?, ?, ?)
    """
    executar_query(query, (nome, qtd, preco, descricao))

def adicionar_quantidade(id_item, qtd_adicional):
    """Adiciona quantidade a um componente já existente na tabela."""
    query = """
        UPDATE estoque
        SET qtd_estoque = qtd_estoque + ?,
            data_atualizacao = CURRENT_TIMESTAMP
        WHERE id_item = ?
    """
    executar_query(query, (qtd_adicional, id_item))

def alterar_preco(id_item, novo_preco):
    """Altera o preço unitário de um componente já existente na tabela."""
    query = """
        UPDATE estoque
        SET preco = ?,
            data_atualizacao = CURRENT_TIMESTAMP
        WHERE id_item = ?
    """
    executar_query(query, (novo_preco, id_item))

def remover_quantidade(id_item, qtd_remover):
    """Retira uma quantidade do estoque (baixa)."""
    # Primeiro, verificamos se há estoque suficiente
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT qtd_estoque FROM estoque WHERE id_item = ?", (id_item,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and resultado[0] >= qtd_remover:
        query = """
            UPDATE estoque
            SET qtd_estoque = qtd_estoque - ?,
                data_atualizacao = CURRENT_TIMESTAMP
            WHERE id_item = ?
        """
        executar_query(query, (qtd_remover, id_item))
        return True
    return False

def excluir_componente(id_item):
    """Apaga o registro do componente definitivamente."""
    query = "DELETE FROM estoque WHERE id_item = ?"
    executar_query(query, (id_item,))
