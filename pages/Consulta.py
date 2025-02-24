import streamlit as st
import pandas as pd

dados = pd.read_csv("clientes.csv") #se não usar o streamlit copia o caminho do cliente.csv

st.title("Clientes cadastrados")
st.divider()

st.dataframe(dados)

