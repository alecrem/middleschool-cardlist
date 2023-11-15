import streamlit as st
import pandas as pd
import urllib.parse
import streamlit_common.footer


def compose_scryfall_url(x: str) -> str:
    return f"https://scryfall.com/search?q=prefer%3Aoldest%20!%22{urllib.parse.quote_plus(x)}%22"


def row_to_link(x: pd.DataFrame) -> None:
    cardname = x["name"]
    if x.name_ja is not "":
        cardname = f"{cardname} / {x.name_ja}"
    st.markdown(f"- [{cardname}]({x.link})")


def get_legal_cardnames(cardname: str, mslist_df: pd.DataFrame) -> list:
    english_match = mslist_df[mslist_df["name"].str.lower() == cardname.lower()]
    cardname_en_list = None
    if english_match.shape[0] > 0:
        cardname_en_list = english_match["name"].to_list()
        cardname_ja_list = english_match["name_ja"].to_list()
    japanese_match = mslist_df[mslist_df["name_ja"] == cardname]
    if japanese_match.shape[0] > 0:
        cardname_en_list = japanese_match["name"].to_list()
        cardname_ja_list = japanese_match["name_ja"].to_list()
    if cardname_en_list is not None and len(cardname_en_list) > 0:
        return [
            cardname_en_list[0] or None,
            cardname_ja_list[0] or None,
        ]
    return None


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
exact_match = get_legal_cardnames(name_input, mslist_df)
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
            f"✅ [{cardname}]({compose_scryfall_url(exact_match[0])}) is an exact match"
        )
    st.write(results_df.shape[0], f'cards found by "{name_input}"')
    if results_df.shape[0] > number_shown_results:
        st.write(f"Top {number_shown_results} results:")
    results_df["link"] = results_df["name"].apply(compose_scryfall_url)
    results_df[:number_shown_results].transpose().apply(row_to_link)

streamlit_common.footer.write_footer()
