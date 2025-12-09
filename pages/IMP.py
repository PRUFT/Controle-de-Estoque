import streamlit as st
import sqlite3
import funcoes
import pandas as pd

funcoes.config()
funcoes.button()
funcoes.quadro()
funcoes.titulolet()

if "logado" not in st.session_state or not st.session_state.logado:
    st.switch_page("pages/LOGIN.py")

st.title("IMPRESSÃO DE ETIQUETAS")
st.subheader("Consulta")
with st.form("produto", clear_on_submit=True):
    cod = st.text_input("Código do Produto:")
    if st.form_submit_button("Consultar"):
        funcoes.consultacod(cod)
    
with st.form("form_produto", clear_on_submit=True):
    prod = st.text_input("Nome do Produto:")
    if st.form_submit_button("Consultar"):
        funcoes.consultaprod(prod)

if st.button("Imprimir"):
    st.info("Imprimindo...")

if st.button("Menu Principal"):
    st.switch_page("pages/MENU.py")
    st.session_state.logado = True

