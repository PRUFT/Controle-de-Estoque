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

st.title("CONTROLE GERAL")
st.subheader("Cadastro de Produtos")

funcoes.bancomenu()

with st.form("form_produto", clear_on_submit=True):
    prod = st.text_input("Nome do produto:", key="produto")
    cod = st.text_input("Código do Produto:", key="codigo")
    prec = st.text_input("Digite o Preço do produto:", key="preco")
    und = st.text_input("Quantidade em Estoque:", key="unidade")

    if st.form_submit_button("Cadastrar Produto"):
        funcoes.cadprod(prod, cod, prec, und)

dados = funcoes.dataframe()
tabela = pd.DataFrame(dados, columns=["ID","Produto","Código","Preço","Estoque"])
st.dataframe(tabela)

if st.button("Registrar Usuário"):
    st.session_state.logado = True
    st.switch_page("pages/REGISTRO.py")

if st.button("Impressão de Etiquetas"):
    st.session_state.logado = True
    st.switch_page("pages/IMP.py")

if st.button("Atualizar dados"):
    st.session_state.logado = True
    st.switch_page("pages/UPDATE.py")




