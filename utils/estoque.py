# -*- coding: utf-8 -*-
# @Author: Bruno Piato
# @Date:   2026-03-18 16:10:49
# @Last Modified by:   Bruno Piato
# @Last Modified time: 2026-03-30 20:26:10

import sqlite3
import pandas as pd
from pathlib import Path

# caminho do banco
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "database.db"


def listar_estoque():
    """Função para listar os estoques que existem na base de dados em forma de tabela

    Returns:
        pd.DataFrame: DataFrame de Pandas com todos os estoques cadastrados
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
                    SELECT 
                        id_item,
                        nome,
                        qtd_estoque,
                        preco,
                        data_atualizacao
                    FROM estoque
                    """)
    estoque = cursor.fetchall()
    conn.close()

    df_estoque = pd.DataFrame(estoque, columns=[
        'ID', 'Nome', 'Quantidade em Estoque', 'Preço', 'Data de Atualização'])

    return df_estoque


def cadastrar_estoque(
    nome: str,
    qtd_estoque: int,
    preco: float
):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
            INSERT INTO estoque (nome, qtd_estoque, preco)
            VALUES (?, ?, ?)
        """,
        (nome, qtd_estoque, preco)
    )

    conn.commit()
    conn.close()

    print(f"Estoque '{nome}' cadastrado com sucesso!")





