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

st.title('Junção dos Resultados - Fusion')

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
        try:
            tabela = ler_TM(tab)
        except:
            st.write('Tipo de dado Errado')

    if tipos == 'Proteínas e Metabólitos':
        try:
            tabela = ler_PM(tab)
        except:
            st.write('Tipo de dado Errado')

    if tipos == 'Transcritos e Proteínas':
        try:
            tabela = ler_TP(tab)
        except:
            st.write('Tipo de dado Errado')

    if tipos == 'Transcritos, Proteínas e Metabólitos':
        try:
            tabela = ler_TPM(tab)
        except:
            st.write('Tipo de dado Errado')
            
    try:
        st.write(tabela)
    
        excel = make_excel(tabela)
    
        ste.download_button(label="Download Resultados",
                            data=excel,
                            file_name="Resultados_Organizados_Fusion.xlsx",
                            mime="application/vnd.ms-excel")
    except:
        pass
