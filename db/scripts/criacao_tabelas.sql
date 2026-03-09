-- DELETE FROM sqlite_sequence WHERE name='clientes';
-- DELETE FROM clientes;
-- DROP TABLE IF EXISTS clientes;
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf TEXT,
    nome TEXT,
    email TEXT,
    endereco TEXT,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- DROP TABLE IF EXISTS estoque;
CREATE TABLE IF NOT EXISTS estoque (
	id_item INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT,
	qtd_estoque INTEGER,
    preco REAL,
	data_atualizacao TIMESTAMP CURRENT_TIMESTAMP
);

-- DROP TABLE IF EXISTS pedidos;
CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    id_item INTEGER,
    qtd_vendida INTEGER,
    valor_total REAL,
    data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
);