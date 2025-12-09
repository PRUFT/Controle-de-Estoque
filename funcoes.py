import streamlit as st
import sqlite3
import pandas as pd

def connectdb():
    conexao = sqlite3.connect("login.db")
    cursor = conexao.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL, senha TEXT NOT NULL)""")
    conexao.commit()
    conexao.close()

def login(email,senha): 
    if email == "":
        st.warning("Digite um Email")
        return
    elif len(senha) < 6:
        st.warning("Senha muito Curta!")
        return
    elif senha == "":
        st.warning("Digite uma senha")
        return    
    else:
        conexao = sqlite3.connect("login.db")
        cursor = conexao.cursor()
        cursor.execute("""SELECT * FROM users WHERE email = ? AND senha = ?""",(email,senha))
        resultado = cursor.fetchone()
        if resultado:
            st.session_state.logado = True
            st.success("Login Realizado!!")
            st.switch_page("pages/MENU.py")
        else:
            st.error("Erro de Login!!")
            return

def registrar(email,senha):
    if email == "":
        st.warning("Digite um Email")
        return
    elif senha == "":
        st.warning("Digite uma senha")
        return
    elif len(senha) < 6:
        st.warning("Senha muito Curta!")
        return
    else:
        conexao = sqlite3.connect("login.db")
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO users (email,senha) VALUES (?,?)", (email,senha))
        conexao.commit()
        conexao.close()
        st.info("Cadastro Feito!!")
        st.session_state.logado = False
        st.switch_page("pages/LOGIN.py")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def bancomenu():
    conexao = sqlite3.connect("produtos.db")
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS prods(id INTEGER PRIMARY KEY AUTOINCREMENT, prod TEXT NOT NULL, cod TEXT NOT NULL, prec NUMERIC(10,2), und TEXT NOT NULL)")
    conexao.commit()
    conexao.close()

def cadprod(prod, cod, prec, und):
    if prod == "":
        st.error("Produto inválido!")
        return
    elif cod == "":
        st.error("Código Do Produto inválido!")
        return
    elif und == "":
        st.error("Quantidade Inválida!")
        return
    else:
        conexao = sqlite3.connect("produtos.db")
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO prods (prod, cod, prec, und) VALUES (?,?,?,?)", (prod, cod, prec, und))
        conexao.commit()
        conexao.close()
        st.info("Produto Cadastrado!!")

def dataframe():
    conexao = sqlite3.connect("produtos.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM prods")
    dados = cursor.fetchall()
    cursor.close
    return dados

def config():
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] {
                display: none;
            }
            [data-testid="stHeader"] {
                display:none;
            }  
        </style>
        """,
        unsafe_allow_html=True)

def button():
    st.markdown("""
    <style>
    div.stButton > Button {
        background-color:darkblue;
    }
    .st-emotion-cache-1anq8dj {
        background-color:darkblue;
    }
    </style>
    """,unsafe_allow_html=True)

def quadro():
    st.markdown("""
    <style>
    .block-container {
        background-color:#1C1C1C;
        border:2px solid #000080;
        border-radius:12px;
        margin-top:5%;
        padding-top:5px;
        padding-left:30px;
        padding-right:30px;
    }
    </style>
    """, unsafe_allow_html=True)
    
def titulolet():
    st.markdown("""
    <style>
    .st-emotion-cache-467cry h1{
        background-color:#000080;
        text-align:center;
        border:2px solid #696969;
        border-radius:12px;}
    .st-bx {
            background-color:#4F4F4F;}
    .st-c1{
            background-color:#4F4F4F;}
    .st-b7{
            background-color:#4F4F4F;}
    .st-emotion-cache-13k62yr {
            background-color:#363636;}
    .stMarkdownContainer {
            background-color:yellow;}
    .stAlertContentError{
            background-color:red;}
    </style>
    """, unsafe_allow_html=True)

def consultacod(cod):
    if cod == "":
        st.warning("Campo Vázio")
        return
    else:
        conexao = sqlite3.connect("produtos.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM prods WHERE cod = ?",(cod,))
        linha = cursor.fetchall()
        if linha:
            df = pd.DataFrame(linha,columns=["id","Prod","Cod","Preço","Estoque"])
            st.table(df)
            conexao.close()
            return df
        else:
            st.error("Nenhum Produto cadastrado!!")
            return

def consultaprod(prod):
    if prod == "":
        st.warning("Campo Vázio")
        return
    else:
        conexao = sqlite3.connect("produtos.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM prods WHERE prod = ? ",(prod,))
        linha = cursor.fetchall()
        if linha:
            df = pd.DataFrame(linha, columns=["id","Prod","Cod","Preço","Estoque"])
            st.table(df)
            conexao.close()
            return df
        else:
            st.error("Nenhum Produto Cadastrado!!")
            return
        
#----------------------------------------------------------------------------------------------------------------
def apagar(cod):
    if cod == "":
        st.warning("Digite o código do produto")
        return
    conexao = sqlite3.connect("produtos.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM prods WHERE cod = ?",(cod,))
    resultado = cursor.fetchall()
    if resultado:
        cursor.execute("DELETE FROM prods WHERE cod = ?",(cod,))
        conexao.commit()
        conexao.close()
    else:
        st.error("Esse Código não Foi Cadastrado")
        return

def atualizar_prec(cod, prec):
    if cod == "":
            st.warning("Digite o código do produto")
            return
    elif prec == "":
        st.warning("Digite o preço")
        return
    else:
        conexao = sqlite3.connect("produtos.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM prods WHERE cod = ?",(cod,))
        resultado = cursor.fetchall()
        if resultado:
            cursor.execute("UPDATE prods SET prec = ? WHERE cod = ?",(prec,cod))
            conexao.commit()
            conexao.close()
            return
        else:
            st.error("Produto Sem Cadastro")
            return
    
def atualizar_und(cod, und):
    if cod == "":
        st.warning("Digite o Código")
        return
    elif und == "":
        st.warning("Digite a Quantidade em Estoque")
    else:
        conexao = sqlite3.connect("produtos.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM prods WHERE cod = ?",(cod,))
        resultado = cursor.fetchall()
        if resultado:
            cursor.execute("UPDATE prods SET und = ? WHERE cod = ?",(und,cod))
            conexao.commit()
            conexao.close()
            return
        else:
            st.error("Produto Sem Cadastro")
            return
    
    
