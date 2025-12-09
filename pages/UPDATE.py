import funcoes
import streamlit as st
import pandas as pd

funcoes.config()
funcoes.button()
funcoes.quadro()
funcoes.titulolet()

if "logado" not in st.session_state or not st.session_state.logado:
    st.switch_page("pages/LOGIN.py")

st.title("ATUALIZAR CADASTROS")
st.subheader("DADOS DO PRODUTO")

with st.form("form_update", clear_on_submit=True):
    cod = st.text_input("Digite o código do produto:")
    prec = st.text_input("Digite o preço:")
    und =  st.text_input("Quantidade em estoque")

    if st.form_submit_button("Atualizar Preço"):
        funcoes.atualizar_prec(cod,prec)

    if st.form_submit_button("Atualizar Estoque"):
        funcoes.atualizar_und(cod,und)

    if st.form_submit_button("Excluir cadastro"):
        funcoes.apagar(cod)

dados = funcoes.dataframe()
tabela = pd.DataFrame(dados,columns=["ID","Produto","Código","Preço","Estoque"])
st.dataframe(tabela)