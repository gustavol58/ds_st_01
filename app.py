import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px 


df = pd.read_csv('recaudos.csv')

st.set_page_config('Recaudos', layout= 'wide' )
st.title('Revisión de csv recaudos completo.')

# Una manera muy larga de centrar la imagen:
# col_c1, col_c2, col_c3 = st.columns(3)
# with col_c1:
#     st.write(' ')
# with col_c2:
#     st.image('pagos.jpg', width = 200)
# with col_c3:
#     st.write(' ')

# Afortunadamente existe una manera mas directa de hacerlo:
# st.columns(3)[1].image('pagos_dig.jpg', width = 200)

# Pero cuando son varias imágenes:
col_c1, col_c2, col_c3, col_c4, col_c5 = st.columns(5)
col_c2.image('pagos_dig.jpg', width = 200)
col_c4.image('pagos.jpg', width = 200)

col1, col2 = st.columns([0.3, 0.7])
with col1:
    select_col = st.selectbox('Escoja una columna: ', df.columns.to_list())

with col2:
    radio_ver_rgtos = st.radio('Primeros registros a ver: ', [5, 10, 20, 50, 100, 500, 1000, 3000, 5784], horizontal = True)

if st.button('Actualizar'):
    col3, col4 = st.columns([0.3, 0.5])
    with col3:
        col3.header('Lista')
        col3.dataframe(df[[select_col, 'Valor recaudo']].head(radio_ver_rgtos), hide_index=True)    
    fig1 = px.histogram(df.replace(np.nan, 'NaN').head(radio_ver_rgtos), x = select_col) 
    with col4:
        col4.header('Histograma (Cantidad veces)')
        col4.plotly_chart(fig1, use_container_width=True)
    fig3 = px.bar(df.replace(np.nan, 'NaN').head(radio_ver_rgtos), x = select_col, y = 'Valor recaudo')
    st.header('Mirar con el valor de recaudo en el eje vertical: ')
    st.plotly_chart(fig3)

    










