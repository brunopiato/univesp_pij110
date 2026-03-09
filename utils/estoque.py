import sqlite3
import pandas as pd

def cadastrar_estoque(
    nome: str,
    qtd_estoque: int,
    preco: float
):
    conn = sqlite3.connect('/workspaces/pij110/db/database.db')
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


def listar_estoque():
    """Função para listar os estoques que existem na base de dados em forma de tabela

    Returns:
        pd.DataFrame: DataFrame de Pandas com todos os estoques cadastrados
    """    
    conn = sqlite3.connect('/workspaces/pij110/db/database.db')
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

    df_estoque = pd.DataFrame(estoque, columns=['ID', 'Nome', 'Quantidade em Estoque', 'Preço', 'Data de Atualização'])

    return df_estoque