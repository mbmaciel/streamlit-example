import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Bem vindo ao exemplo de Streamlit do Mbmaciel!

Abaixo é apenas um exemplo de como funciona essa biblioteca.
Vou fazer alguns testes e ver como funciona.

Enquanto isso aprecie os dados:
"""

num_points = st.slider("Numero de pontos no espiral", 1, 10000, 1100)
num_turns = st.slider("Numero de voltar no espiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
