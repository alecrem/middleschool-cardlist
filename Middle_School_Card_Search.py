import streamlit as st
import pandas as pd
import urllib.parse
import streamlit_common.footer


def compose_scryfall_url(x: str) -> str:
    return f"https://scryfall.com/search?q=prefer%3Aoldest%20!%22{urllib.parse.quote_plus(x)}%22"


def row_to_link(x: pd.DataFrame) -> None:
    st.markdown(f"- [{x['name']} / {x.name_ja}]({x.link})")


def is_legal(cardname: str) -> str:
    english_match = mslist_df[mslist_df["name"].str.lower() == cardname.lower()]
    if english_match.shape[0] > 0:
        return english_match["name"].to_list()[0]
    japanese_match = mslist_df[mslist_df["name_ja"] == cardname]
    if japanese_match.shape[0] > 0:
        return japanese_match["name_ja"].to_list()[0]
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
exact_match = is_legal(name_input)
results_en_df = mslist_df[
    mslist_df["name"].str.contains(name_input.lower(), case=False)
]
results_ja_df = mslist_df[
    mslist_df["name_ja"].str.contains(name_input.lower(), case=False)
]
results_df = results_en_df.merge(results_ja_df, how="outer")
if name_input:
    if exact_match is not None:
        st.write(
            f"✅ [{exact_match}]({compose_scryfall_url(exact_match)}) is an exact match"
        )
    st.write(results_df.shape[0], f'cards found by "{name_input}"')
    if results_df.shape[0] > number_shown_results:
        st.write(f"Top {number_shown_results} results:")
    results_df["link"] = results_df["name"].apply(compose_scryfall_url)
    results_df[:number_shown_results].transpose().apply(row_to_link)

streamlit_common.footer.write_footer()
