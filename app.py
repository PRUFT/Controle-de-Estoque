import streamlit as st
import sqlite3
import funcoes

funcoes.config()

if "logado" not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:
    st.switch_page("pages/LOGIN.py")