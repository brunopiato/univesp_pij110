import pandas as pd
import sqlite3

from utils.pedidos import listar_pedidos, cadastrar_pedido

cadastrar_pedido(
    id_cliente=1,
    id_item=1,
    qtd_vendida=2,
    valor_total=10.96
)

print(listar_pedidos())

# excluir_cliente(3)

# print(listar_pedidos())
