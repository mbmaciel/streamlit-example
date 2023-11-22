import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Bem vindo ao exemplo de Streamlit do Mbmaciel!

Abaixo os dados do banco ecletica.
Os dados foram capturados com cache.

"""

# Initialize connection.
conn = st.connection('mysql', type='sql')

df = conn.query('SELECT * from ecletica_financeiro;', ttl=600)


# num_ticket, data_hora_abre, data_hora_fecha, vlr_total, dinheiro
for row in df.itertuples():
    df1 = pd.DataFrame({row.vlr_total}, columns=("col %d" % i for i in range(20)))

    st.write(f"{row.num_ticket} , {row.data_hora_abre}, {row.data_hora_fecha}, {row.vlr_total}, {row.dinheiro} ")

my_table = st.table(df1)

my_table.add_rows(df1)



