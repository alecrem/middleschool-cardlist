import streamlit as st
import pandas as pd

mslist_path = "output/middleschool.csv"

st.write(
    """
    # Middle School Card List
    """
)

mslist_df = pd.read_csv(mslist_path)
mslist_df.fillna("", inplace=True)
st.write(mslist_df.shape[0], "cards are legal")

lang = st.radio("Card language", ("English", "Japanese"))
name_input = st.text_input(f"Search by {lang} card name")
lang_col = {
    "English": "name",
    "Japanese": "name_ja",
}

results_df = mslist_df[
    mslist_df[lang_col[lang]].str.contains(name_input.lower(), case=False)
]
if name_input:
    st.write(results_df.shape[0], f'cards found by "{name_input}"')
st.write(results_df[["name", "name_ja"]])
