import streamlit as st
import sqlite3
import funcoes

funcoes.config()
funcoes.button()
funcoes.quadro()
funcoes.titulolet()
funcoes.connectdb()

st.title ("SISTEMA DE CONTROLE")
st.header ("LOGIN")

email = st.text_input("Digite seu Email:")
senha = st.text_input("Digite sua Senha:", type="password")

if st.button("Login"):
    funcoes.login(email, senha)
