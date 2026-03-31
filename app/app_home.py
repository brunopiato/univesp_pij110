# -*- coding: utf-8 -*-
# @Author: Bruno Piato
# @Date:   2026-03-31 07:42:14
# @Last Modified by:   Bruno Piato
# @Last Modified time: 2026-03-31 16:10:33
import streamlit as st


def st_home():
    """Homepage content."""
    with st.container():
        st.markdown("### 🏢 Institucional")
        st.caption("Mauricio Henrique Camargo | CNPJ: 11.458.173/0001-74 | Desde 2009")
        st.write("""
        Especializada em **Suporte Técnico e Manutenção em TI**, nossa empresa combina
        experiência de mercado com inovação tecnológica. Este sistema de gestão de estoque
        reflete nosso compromisso com a organização e a excelência operacional.
        """)
