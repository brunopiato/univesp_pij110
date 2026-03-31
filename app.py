# -*- coding: utf-8 -*-
# @Author: Bruno Piato
# @Date:   2026-03-18 16:10:49
# @Last Modified by:   Bruno Piato
# @Last Modified time: 2026-03-31 07:47:22

import streamlit as st
from app.app_estoque import st_verificar_estoque, st_cadastrar_componente, st_remover_componente
from app.app_home import st_home
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Mauricio Henrique Camargo", layout="wide")

st.title("Mauricio Henrique Camargo")

# Sessão para armazenar o estado do login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Função para realizar o login
def login(username, password):
    # Substitua com a lógica de autenticação real
    return username == os.getenv("username") and password == os.getenv("password")

if not st.session_state.logged_in:
    st.sidebar.markdown('# Login')
    st.sidebar.header("Acesso Restrito")

    username = st.sidebar.text_input("Usuário")
    password = st.sidebar.text_input("Senha", type="password")

    if st.sidebar.button("Entrar"):
        if login(username, password):
            st.session_state.logged_in = True
            st.rerun()  # Recarrega a página imediatamente após o login
        else:
            st.sidebar.error("Usuário ou senha incorretos.")

    st.subheader("Bem-vindo ao Aplicativo de Gerenciamento de Estoque")
    st.info("Faça login para acessar as funcionalidades.")
else:
    st.sidebar.markdown('# Gerenciador de Estoque')
    st.sidebar.header("Menu")

    option = st.sidebar.selectbox(
        "Escolha uma opção",
        [
            "Home",
            "Verificar Estoque",
            "Cadastrar Componente",
            "Remover Componente",
        ]
    )

    if option == "Home":
        st.subheader("Bem-vindo ao Aplicativo de Gerenciamento de Estoque")
        st.info("Selecione uma opção no menu ao lado para continuar.")
        st_home()

    elif option == "Verificar Estoque":
        st_verificar_estoque()

    elif option == "Cadastrar Componente":
        st_cadastrar_componente()
        
    elif option == "Remover Componente":
        st_remover_componente()

    st.sidebar.info("Use o menu para navegar entre as opções")
