import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import array

"""
# Bem vindo ao exemplo de Streamlit do Mbmaciel!

Abaixo os dados do banco ecletica.
Os dados foram capturados com cache.
"""
data = []
hora = []
conn = st.connection('mysql', type='sql')
df = conn.query('SELECT * from ecletica_financeiro limit 10;', ttl=600)

# num_ticket, data_hora_abre, data_hora_fecha, vlr_total, dinheiro
for row in df.itertuples():
    data.append({row.vlr_total})
    hora.append({row.data_hora_abre})
    chart_data = pd.DataFrame(
        {
            "col1": data,
            "col2": hora,
            
        }
    )
    
    #st.write(f"{row.num_ticket} , {row.data_hora_abre}, {row.data_hora_fecha}, {row.vlr_total}, {row.dinheiro} ")

st.bar_chart(chart_data, x="col1", y="col2")



