# -*- coding: utf-8 -*-
# @Author: Bruno Piato
# @Date:   2026-03-31 07:42:14
# @Last Modified by:   Bruno Piato
# @Last Modified time: 2026-05-13 14:49:34
import streamlit as st


def st_home():
    """Homepage content."""
    with st.container():
        st.markdown("### 🏢 Institucional")
        st.caption("Mauricio Henrique Camargo | CNPJ: 11.458.173/0001-74 | Desde 2009")
        st.write("""
        Especializada em **serviços e comercialização de produtos na área elétrica**, 
        nossa empresa combina experiência de mercado com inovação tecnológica. Este 
        sistema de gestão de estoque reflete nosso compromisso com a organização e a 
        excelência operacional.
        """)
