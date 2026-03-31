# -*- coding: utf-8 -*-
# @Author: Bruno Piato
# @Date:   2026-03-18 16:10:49
# @Last Modified by:   Bruno Piato
# @Last Modified time: 2026-03-31 16:21:52
import hashlib
import sqlite3
from pathlib import Path

# caminho do banco
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "database.db"


def verificar_senha(senha_digitada, senha_no_banco):
    """Transforma a senha em hash para comparar com a salva no banco."""
    # Transforma a senha digitada em hash para comparar com o banco
    hash_digitado = hashlib.sha256(senha_digitada.encode()).hexdigest()
    return hash_digitado == senha_no_banco


def buscar_usuario(username):
    """Busca um usuário no banco de dados para realizar o login."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT username, senha_hash FROM usuarios WHERE username = ?", (username,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario # Retorna (username, senha_hash) ou None


def criar_admin_inicial(username, senha):
    """Cria um usuário e uma senha."""
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    conn = sqlite3.connect('db/database.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (username, senha_hash) VALUES (?, ?)", (username, senha_hash))
        conn.commit()
        print(f"Usuário {username} criado com sucesso!")
    except sqlite3.IntegrityError:
        print("Usuário já existe.")
    conn.close()
