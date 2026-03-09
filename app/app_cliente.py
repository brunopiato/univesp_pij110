import streamlit as st
import pandas as pd
import sqlite3
from utils.clientes import listar_clientes

def st_cliente():
    st.subheader("Clientes Cadastrados")
    
    if st.button("Listar Clientes"):
        # Conectar ao banco de dados e listar clientes
        conn = sqlite3.connect('db/database.db')
        df_clientes = listar_clientes()
        conn.close()
        
        # Exibir clientes em uma tabela
        if not df_clientes.empty:
            st.dataframe(df_clientes)
            st.success("Clientes listados com sucesso.")
        else:
            st.info("Nenhum cliente cadastrado.")