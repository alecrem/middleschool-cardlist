import streamlit as st
import pandas as pd

mslist_path = "output/middleschool.csv"
top_results_count = 40

st.write(
    """
    # Middle School Card Search
    """
)

mslist_df = pd.read_csv(mslist_path)
mslist_df.fillna("", inplace=True)
st.write(mslist_df.shape[0], "cards are legal")

name_input = st.text_input(f"Search by card name")
results_en_df = mslist_df[
    mslist_df["name"].str.contains(name_input.lower(), case=False)
]
results_ja_df = mslist_df[
    mslist_df["name_ja"].str.contains(name_input.lower(), case=False)
]
results_df = results_en_df.merge(results_ja_df, how="outer")
if name_input:
    st.write(results_df.shape[0], f'cards found by "{name_input}"')
    results_df["link"] = results_df["name"].apply(
        lambda x: f"https://scryfall.com/search?q=prefer%3Aoldest%20!%22{x}%22"
    )
    st.write(results_df[["name", "name_ja", "link"]])
