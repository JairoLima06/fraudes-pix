import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fraudes no Pix", layout="wide")

st.title("🚨 Detecção de Fraudes no Pix")
st.write("Protótipo com dados sintéticos")

df = pd.read_csv("data/pix_sintetico.csv")

st.subheader("📊 Dados coletados")
st.dataframe(df.head(20))

fraudes = df[df["suspeita"] == 1]
st.subheader("⚠️ Transações suspeitas")
st.dataframe(fraudes)

st.bar_chart(df["suspeita"].value_counts())
