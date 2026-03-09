import streamlit as st
import pandas as pd
import sqlite3
from utils.pedidos import listar_pedidos

def st_pedidos():
    st.subheader("pedidos Cadastradas")
    
    if st.button("Listar pedidos"):
        # Conectar ao banco de dados e listar pedidos
        conn = sqlite3.connect('db/database.db')
        df_pedidos = listar_pedidos()
        conn.close()
        
        # Exibir pedidos em uma tabela
        if not df_pedidos.empty:
            st.dataframe(df_pedidos)
            st.success("pedidos listadas com sucesso.")
        else:
            st.info("Nenhuma venda cadastrada.")