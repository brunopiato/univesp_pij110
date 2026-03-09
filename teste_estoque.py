import pandas as pd
import sqlite3

from utils.estoque import listar_estoque, cadastrar_estoque
cadastrar_estoque(
    nome="potenciômetro",
    qtd_estoque=10,
    preco=5.89,
)

print(listar_estoque())
