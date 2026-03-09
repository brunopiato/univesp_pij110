import sqlite3
from pathlib import Path

# caminho do banco
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "database.db"

# cria conexão (isso cria o arquivo automaticamente)
conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

# criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf TEXT,
    nome TEXT,
    email TEXT,
    endereco TEXT,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
conn.close()

print(f"Database criado em: {DB_PATH}")