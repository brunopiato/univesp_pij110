# -*- coding: utf-8 -*-
# @Author: Bruno Piato
# @Date:   2026-03-18 16:10:49
# @Last Modified by:   Bruno Piato
# @Last Modified time: 2026-03-30 20:21:52
import streamlit as st
import pandas as pd
import sqlite3
from utils.estoque import listar_estoque

def st_verificar_estoque():
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


def st_cadastrar_componente():
    st.subheader("Cadastrar componente")

def st_remover_componente():
    st.subheader("Remover componente")