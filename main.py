import streamlit as st
import streamlit_ext as ste
from funcs import *

st.set_page_config(page_title='Junção dos Resultados - Fusion', layout='wide')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html=True)

title_col1, title_col2, title_col3, title_col4 = st.columns((1, 2, 2, 1))
col1, col2, col3, col4 = st.columns((1, 2, 2, 1))

st.title('TJunção dos Resultados - Fusion')

tab = st.file_uploader('Insira o arquivo com os resultados do Fusion',
                       type='xlsx',
                       accept_multiple_files=False)

tipos = st.radio('Quais os dados na tabela?',
                 ['Transcritos e Metabólitos',
                  'Proteínas e Metabólitos',
                  'Transcritos e Proteínas',
                  'Transcritos, Proteínas e Metabólitos'],
                 index=None)

if tab and tipos:

    if tipos == 'Transcritos e Metabólitos':
        tabela = ler_TM(tab)

    if tipos == 'Proteínas e Metabólitos':
        tabela = ler_PM(tab)

    if tipos == 'Transcritos e Proteínas':
        tabela = ler_TP(tab)

    if tipos == 'Transcritos, Proteínas e Metabólitos':
        tabela = ler_TPM(tab)

    st.write(tabela)

    excel = make_excel(tabela)

    ste.download_button(label="Download Resultados",
                        data=excel,
                        file_name="Resultados_Organizados_Fusion.xlsx",
                        mime="application/vnd.ms-excel")
