
import streamlit as st
import os

# CONFIG
st.set_page_config(page_title="Perfil Kesia Alves", layout="centered")

# FUNÇÃO PARA EVITAR ERRO SE NÃO ENCONTRAR IMAGEM
def mostrar_imagem(caminho, largura=None):
    if os.path.exists(caminho):
        st.image(caminho, width=largura)
    else:
        st.warning(f"Imagem não encontrada: {caminho}")

# TOPO
mostrar_imagem("iphone.png")

st.title("Kesia Alves")

# FOTO
mostrar_imagem("foto.kesia.jpeg", largura=200)

# DESCRIÇÃO
st.write(
    "Kesia Alves é estudante do 3º ano de Informática no Instituto Federal da Paraíba, campus de Itabaiana."
)

# WHATSAPP
mostrar_imagem("whatsapp.png", largura=100)
st.link_button("Acessar WhatsApp", "https://web.whatsapp.com/")
