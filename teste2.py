import streamlit as st
import base64

# CONFIG
st.set_page_config(page_title="Perfil Kesia Alves", layout="wide")

# FUNÇÃO base64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image("star.png")
zap_base64 = get_base64_image("zap2026.png")

# TOPO
st.image("iphone.png")

st.write("### Kesia Alves")
st.image("foto.kesia.jpeg")

st.write("Kesia Alves é estudante do 3º ano de Informática no Instituto Federal da Paraíba, campus de Itabaiana.")

st.image("whatsapp.png")
st.link_button("Acessar WhatsApp", "https://web.whatsapp.com/")

# IMAGEM CLICÁVEL CENTRAL
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 50px;">
            <a href="https://starlink.com/" target="_blank">
                <img src="data:image/png;base64,{img_base64}" 
                     width="320" 
                     style="border-radius:12px;">
            </a>
        </div>
    """, unsafe_allow_html=True)

# LAYOUT PRINCIPAL
col_left, col_right = st.columns([3,1])

with col_left:
    st.markdown("""
    <div style='margin-bottom:30px; font-size:30px;'>
        <b>Kesia Alves</b>
    </div>
    """, unsafe_allow_html=True)

    subcol1, subcol2 = st.columns([1,4])

    # IMAGEM
    with subcol1:
        st.image("foto.kesia.jpeg", width=250)

    # TEXTO
    with subcol2:
        st.markdown("""
        <div style="
            text-align: justify;
            font-size: 20px;
            line-height: 2.0;
        ">
            <b>Sobre Kesia:<br>
            Kesia Alves é estudante do 3º ano do curso de Informática no Instituto Federal da Paraíba (IFPB),
            campus Itabaiana. Está em fase de formação técnica, desenvolvendo habilidades em tecnologia,
            programação e resolução de problemas, com foco no crescimento acadêmico e profissional.
        </div>
        """, unsafe_allow_html=True)

# WHATSAPP FINAL
st.markdown(f"""
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://wa.me/5583998234415" target="_blank">
            <img src="data:image/png;base64,{zap_base64}" width="100">
        </a>
    </div>
""", unsafe_allow_html=True)
