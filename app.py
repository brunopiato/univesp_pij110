import streamlit as st
from utils.clientes import listar_clientes
from app.app_cliente import st_cliente
from app.app_estoque import st_estoque

st.set_page_config(page_title="Aplicativo Empresa do Maurício", layout="wide")

st.title("Aplicativo Empresa do Maurício")

st.sidebar.markdown('# Aplicativo da Empresa')

st.sidebar.header("Menu")

# Exemplo de estrutura para usar funções do módulo utils
option = st.sidebar.selectbox(
    "Escolha uma opção",
    [
        "Home",
        "Cliente",
        "Estoque",
        "Pedidos",
    ]
)

if option == "Home":
    st.subheader("Bem-vindo ao Aplicativo da Empresa")
    st.info("Selecione uma opção no menu para continuar.")
elif option == "Cliente":
    st.subheader("Lista de Clientes")
    st_cliente()
elif option == "Estoque":
    st.subheader("Gerenciamento de Estoque")
    st.info("Funcionalidade de estoque em desenvolvimento.")
    st_estoque()
elif option == "Pedidos":    
    st.subheader("Gerenciamento de pedidos")
    st.info("Funcionalidade de pedidos em desenvolvimento.")
    st_pedidos()

st.sidebar.info("Use o menu para navegar entre as opções")