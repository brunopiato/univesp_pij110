/**
 * @Author: Bruno Piato
 * @Date:   2026-03-18 16:10:49
 * @Last Modified by:   Bruno Piato
 * @Last Modified time: 2026-03-31 07:30:14
 */
-- DROP TABLE IF EXISTS estoque;
CREATE TABLE IF NOT EXISTS estoque (
	id_item INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT,
	qtd_estoque INTEGER,
    preco REAL,
    descricao TEXT,
	data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
