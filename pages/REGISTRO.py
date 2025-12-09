import streamlit as st
import sqlite3
import funcoes

funcoes.config()
funcoes.button()
funcoes.quadro()
funcoes.titulolet()

if "logado" not in st.session_state or not st.session_state.logado:
    st.switch_page("pages/LOGIN.py")

st.title ("SISTEMA DE CONTROLE")
st.header ("Tela de Registro")

email = st.text_input("Digite um Email:")
senha = st.text_input("Digite uma Senha:", type="password")

if st.button("Registrar"):
    funcoes.registrar(email,senha)

if st.button("Menu Principal"):
    st.switch_page("pages/MENU.py")
    st.session_state.logado = True


