# -*- coding: utf-8 -*-
# @Author: Bruno Piato
# @Date:   2026-03-18 16:10:49
# @Last Modified by:   Bruno Piato
# @Last Modified time: 2026-03-31 07:54:20
import streamlit as st
import pandas as pd
# Importando as funções que criamos no passo anterior
from utils.estoque import (
    listar_estoque, 
    cadastrar_novo_componente, 
    adicionar_quantidade, 
    alterar_preco, 
    remover_quantidade, 
    excluir_componente
)

def st_verificar_estoque():
    st.subheader("🔍 Consulta e Atualização de Estoque")
    
    df_estoque = listar_estoque()
    
    if df_estoque.empty:
        st.info("Nenhum componente cadastrado no sistema.")
        return

    # Sistema de busca simples
    busca = st.text_input("Buscar componente pelo nome")
    if busca:
        df_filtrado = df_estoque[df_estoque['Nome'].str.contains(busca, case=False, na=False)]
    else:
        df_filtrado = df_estoque

    st.dataframe(df_filtrado, use_container_width=True)

    st.divider()
    
    # Seção para atualizar itens existentes
    st.subheader("⚙️ Ações Rápidas sobre Itens Existentes")
    
    # Criamos um selectbox para o usuário escolher qual ID quer alterar
    lista_nomes = df_estoque['ID'].astype(str) + " - " + df_estoque['Nome']
    escolha = st.selectbox("Selecione o Componente para alterar", lista_nomes)
    id_selecionado = int(escolha.split(" - ")[0])
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Adicionar Unidades**")
        qtd_add = st.number_input("Qtd a adicionar", min_value=1, step=1, key="add_qtd")
        if st.button("➕ Adicionar", key="btn_add"):
            adicionar_quantidade(id_selecionado, qtd_add)
            st.success("Estoque atualizado!")
            st.rerun()

    with col2:
        st.markdown("**Dar Baixa (Retirada)**")
        qtd_rem = st.number_input("Qtd a retirar", min_value=1, step=1, key="rem_qtd")
        if st.button("➖ Dar Baixa", key="btn_rem"):
            if remover_quantidade(id_selecionado, qtd_rem):
                st.success("Baixa realizada!")
                st.rerun()
            else:
                st.error("Quantidade insuficiente em estoque!")

    with col3:
        st.markdown("**Alterar Preço Unitário**")
        novo_p = st.number_input("Novo Preço (R$)", min_value=0.0, step=0.01, key="alt_preco")
        if st.button("💾 Atualizar Preço", key="btn_preco"):
            alterar_preco(id_selecionado, novo_p)
            st.success("Preço atualizado!")
            st.rerun()


def st_cadastrar_componente():
    st.subheader("📥 Cadastrar Novo Componente")
    
    with st.form("form_cadastro", clear_on_submit=True):
        nome = st.text_input("Nome do Componente (Ex: Resistor 10k, Arduino Uno)")
        qtd = st.number_input("Quantidade Inicial em Estoque", min_value=0, step=1)
        preco = st.number_input("Preço Unitário (R$)", min_value=0.0, step=0.01)
        descricao = st.text_input("Descrição do Componente (Ex: Ficha técnica)")
        
        submetido = st.form_submit_button("Cadastrar Componente")
        
        if submetido:
            if nome.strip() == "" or qtd == 0 or preco == 0:
                st.error("Os campos precisam ser preenchidos.")
            else:
                cadastrar_novo_componente(nome, qtd, preco, descricao)
                st.success(f"'{nome}' cadastrado com sucesso!")


def st_remover_componente():
    st.subheader("🗑️ Excluir Registro de Componente")
    st.warning("Atenção: Esta ação apagará o componente e todo o seu histórico permanentemente!")
    
    df_estoque = listar_estoque()
    
    if df_estoque.empty:
        st.info("Nenhum componente cadastrado.")
        return
        
    lista_nomes = df_estoque['ID'].astype(str) + " - " + df_estoque['Nome']
    escolha = st.selectbox("Selecione o Componente para DELETAR", lista_nomes, key="del_select")
    id_selecionado = int(escolha.split(" - ")[0])
    
    # Um checkbox de confirmação para evitar cliques acidentais
    confirmou = st.checkbox("Eu tenho certeza de que quero apagar este item permanentemente.")
    
    if st.button("🚨 Excluir Permanentemente", type="primary"):
        if confirmou:
            excluir_componente(id_selecionado)
            st.success("Componente deletado do banco de dados!")
            st.rerun()
        else:
            st.error("Você precisa marcar a caixa de confirmação para poder excluir.")