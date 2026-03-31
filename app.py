# -*- coding: utf-8 -*-
# @Author: Bruno Piato
# @Date:   2026-03-18 16:10:49
# @Last Modified by:   Bruno Piato
# @Last Modified time: 2026-03-31 16:26:38


import streamlit as st
from dotenv import load_dotenv

from app.app_estoque import (
    st_cadastrar_componente,
    st_remover_componente,
    st_verificar_estoque,
)
from app.app_home import st_home
from utils.configuracao_db import buscar_usuario, verificar_senha

load_dotenv()

st.set_page_config(page_title="Mauricio Henrique Camargo", layout="wide")

st.title("Mauricio Henrique Camargo")

# Sessão para armazenar o estado do login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Função para realizar o login
def login(username, password):
    """Função para verificar se as informações fornecidas no login estão presentes no banco de dado."""
    usuario_db = buscar_usuario(username)

    # usuario_db[1] é a senha_hash vinda do banco
    return usuario_db and verificar_senha(password, usuario_db[1])


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
