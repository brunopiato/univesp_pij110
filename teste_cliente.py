import pandas as pd
import sqlite3

from utils.clientes import listar_clientes, cadastrar_cliente, excluir_cliente

cadastrar_cliente(
    cpf="123.456.789-00",
    nome="João Silva",
    email="joao.silva@email.com",
    endereco="Rua Exemplo, 123 - São Paulo/SP"
)

print(listar_clientes())

# excluir_cliente(3)

# print(listar_clientes())
