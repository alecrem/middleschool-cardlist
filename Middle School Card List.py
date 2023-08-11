import streamlit as st
import pandas as pd

mslist_path = "output/middleschool.csv"

st.write(
    """
    # Middle School Card List
    """
)

mslist_df = pd.read_csv(mslist_path)
st.write(mslist_df.shape[0], "cards are legal")

name_input = st.text_input("Search by English card name")

results_df = mslist_df[mslist_df["name"].str.contains(name_input.lower(), case=False)]
if name_input:
    st.write(results_df.shape[0], "cards found by", '"' + name_input + '"')
st.write(results_df[["name", "name_ja"]])
