import streamlit as st
import base64

# CONFIG
st.set_page_config(page_title="Perfil", layout="wide")

# FUNÇÃO BASE64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# IMAGENS DO REPOSITÓRIO
img_base64 = get_base64_image("iphone.png")
zap_base64 = get_base64_image("whatsapp.png")

# LINK DA EMPRESA
link_empresa = "https://www.apple.com/br/"

# TOPO (imagem clicável)
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 50px;">
            <a href="{link_empresa}" target="_blank">
                <img src="data:image/png;base64,{img_base64}"
                     width="320"
                     style="border-radius:12px;">
            </a>
        </div>
    """, unsafe_allow_html=True)

# LAYOUT PRINCIPAL
col_left, col_right = st.columns([3, 1])

with col_left:

    st.markdown("""
    <div style='margin-bottom:30px; font-size:30px;'>
        <b>Kesia</b>
    </div>
    """, unsafe_allow_html=True)

    # SUBCOLUNAS
    subcol1, subcol2 = st.columns([1, 4])

    # IMAGEM PERFIL
    with subcol1:

        st.markdown("""
        <div style="
            display:flex;
            justify-content:center;
            align-items:center;
            height:100%;
        ">
        """, unsafe_allow_html=True)

        st.image("foto.kesia.jpeg", width=250)

        st.markdown("</div>", unsafe_allow_html=True)

    # TEXTO
    with subcol2:

        st.markdown("""
        <div style="
            text-align: justify;
            font-size: 20px;
            line-height: 2.0;
            width: 100%;
        ">
            <b>Sobre Kesia:</b><br><br>

            Kesia é estudante e possui interesse em tecnologia,
            inovação e desenvolvimento pessoal. Busca constantemente
            aprender novas habilidades e crescer academicamente
            e profissionalmente.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top:30px;'>", unsafe_allow_html=True)

    # BOTÃO DA EMPRESA
    st.link_button(
        "Visitar Site da Empresa",
        link_empresa
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    st.empty()

# WHATSAPP CLICÁVEL
st.markdown(f"""
    <div style="text-align:center; margin-top:30px;">
        <a href="https://wa.me/5583999999999" target="_blank">
            <img src="data:image/png;base64,{zap_base64}" width="100">
        </a>
    </div>
""", unsafe_allow_html=True)
