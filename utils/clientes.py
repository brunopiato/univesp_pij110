import sqlite3
import pandas as pd

def cadastrar_cliente(
    cpf: str,
    nome: str,
    email: str,
    endereco: str
):
    """Função para cadastrar clietne

    Args:
        cpf (str): CPF em forma textual
        nome (str): Nome do cliente
        email (str): Endereço de e-mail do cliente
        endereco (str): Endereço físico do cliente
    """    
    conn = sqlite3.connect('/workspaces/pij110/db/database.db')
    cursor = conn.cursor()

    cursor.execute(
        """
            INSERT INTO clientes (cpf, nome, email, endereco)
            VALUES (?, ?, ?, ?)
        """,
        (cpf, nome, email, endereco)
    )

    conn.commit()
    conn.close()

    print(f"Cliente '{nome}' cadastrado com sucesso!")


def listar_clientes():
    """Função para listar os clientes que existem na base de dados em forma de tabela

    Returns:
        pd.DataFrame: DataFrame de Pandas com todos os clientes cadastrados
    """    
    conn = sqlite3.connect('/workspaces/pij110/db/database.db')
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT 
                        id_cliente,
                        cpf,
                        nome,
                        email,
                        endereco
                   FROM clientes
                   """)
    clientes = cursor.fetchall()
    conn.close()

    df_clientes = pd.DataFrame(clientes, columns=['ID', 'CPF', 'Nome', 'Email', 'Endereço'])

    return df_clientes


def excluir_cliente(cliente_id):
    conn = sqlite3.connect('/workspaces/pij110/db/database.db')
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM clientes WHERE id_cliente = ?
        """, (cliente_id,))

    conn.commit()
    conn.close()

    print(f"Cliente com ID {cliente_id} excluído com sucesso!")


# def atualizar_cliente(cliente_id, nome, email, telefone):
#     conn = sqlite3.connect('/workspaces/pij110/db/database.db')
#     cursor = conn.cursor()

#     cursor.execute(
#         """
#         UPDATE clientes
#         SET nome = ?, email = ?, telefone = ?
#         WHERE id = ?
#         """, (nome, email, telefone, cliente_id))

#     conn.commit()
#     conn.close()

# def buscar_cliente_por_id(cliente_id):
#     conn = sqlite3.connect('/workspaces/pij110/db/database.db')
#     cursor = conn.cursor()

#     cursor.execute('SELECT id, nome, email, telefone FROM clientes WHERE id = ?', (cliente_id,))
#     cliente = cursor.fetchone()

#     conn.close()
#     return cliente
