import streamlit as st

st.title('Calculadora De Hidráulica') 

valor_da_pressao = st.number_input('Digite o Valor Da Pressão')

st.write(f'O Valor Da Pressão É : {valor_da_pressao} ')