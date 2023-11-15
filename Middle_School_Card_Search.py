import streamlit as st
import pandas as pd
import streamlit_common.footer
import streamlit_common.lib as lib

mslist_path = "output/middleschool.csv"
number_shown_results = 20

st.set_page_config(
    page_title="Middle School | Card Search",
    page_icon="🃏",
    layout="wide",
)
st.write(
    """
    # Middle School Card Search

    Enter any English or Japanese text to find all Middle School legal card titles which include it.
    """
)

mslist_df = pd.read_csv(mslist_path)
mslist_df.fillna("", inplace=True)
st.write(mslist_df.shape[0], "cards are legal")

name_input = st.text_input(f"Search by card name").strip()
exact_match = lib.get_legal_cardnames(name_input, mslist_df)
results_en_df = mslist_df[
    mslist_df["name"].str.contains(name_input.lower(), case=False)
]
results_ja_df = mslist_df[
    mslist_df["name_ja"].str.contains(name_input.lower(), case=False)
]
results_df = results_en_df.merge(results_ja_df, how="outer")
if name_input:
    if exact_match is not None:
        cardname = exact_match[0]
        if exact_match[1] is not None:
            cardname = f"{cardname} / {exact_match[1]}"
        st.write(
            f"✅ [{cardname}]({lib.compose_scryfall_url(exact_match[0])}) is an exact match"
        )
    st.write(results_df.shape[0], f'cards found by "{name_input}"')
    if results_df.shape[0] > number_shown_results:
        st.write(f"Top {number_shown_results} results:")
    results_df["link"] = results_df["name"].apply(lib.compose_scryfall_url)
    results_df[:number_shown_results].transpose().apply(lib.row_to_link)

streamlit_common.footer.write_footer()
