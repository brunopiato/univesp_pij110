import sqlite3
import pandas as pd


def cadastrar_pedido(
    id_cliente: int,
    id_item: int,
    qtd_vendida: int,
    valor_total: float
):   
    conn = sqlite3.connect('/workspaces/pij110/db/database.db')
    cursor = conn.cursor()

    cursor.execute(
        """
            INSERT INTO pedidos (id_cliente, id_item, qtd_vendida, valor_total)
            VALUES (?, ?, ?, ?)
        """,
        (id_cliente, id_item, qtd_vendida, valor_total)
    )

    conn.commit()
    conn.close()

    print(f"Novo pedido cadastrado com sucesso!")
    

def listar_pedidos():
    """Função para listar os pedidos que existem na base de dados em forma de tabela

    Returns:
        pd.DataFrame: DataFrame de Pandas com todos os pedidos cadastrados
    """    
    conn = sqlite3.connect('/workspaces/pij110/db/database.db')
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT 
                        id_pedido,
                        id_cliente,
                        id_item,
                        qtd_vendida,
                        valor_total,
                        data_atualizacao
                   FROM pedidos
                   """)
    pedidos = cursor.fetchall()
    conn.close()

    df_pedidos = pd.DataFrame(pedidos, columns=[
        'id_pedido',
        'id_cliente',
        'id_item',
        'qtd_vendida',
        'valor_total',
        'data_atualizacao',
    ])

    return df_pedidos