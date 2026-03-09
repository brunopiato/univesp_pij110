import streamlit as st
import pandas as pd
import sqlite3
from utils.estoque import listar_estoque

def st_estoque():
    st.subheader("Estoque Cadastrado")
    
    if st.button("Listar Estoque"):
        # Conectar ao banco de dados e listar estoque
        conn = sqlite3.connect('db/database.db')
        df_estoque = listar_estoque()
        conn.close()
        
        # Exibir estoque em uma tabela
        if not df_estoque.empty:
            st.dataframe(df_estoque)
            st.success("Estoque listado com sucesso.")
        else:
            st.info("Nenhum estoque cadastrado.")