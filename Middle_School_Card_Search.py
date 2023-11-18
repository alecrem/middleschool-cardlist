import streamlit as st
import pandas as pd
import streamlit_common.footer
import streamlit_common.lib as lib
import streamlit_common.locale

mslist_path = "output/middleschool.csv"
number_shown_results = 20
_ = streamlit_common.locale.get_locale()

st.set_page_config(
    page_title="Middle School | Card Search",
    page_icon="🃏",
    layout="wide",
)
l = st.sidebar.radio(
    label="luage / 言語",
    options=["en", "ja"],
    captions=["English", "日本語"],
)
st.write(f'# {_["search"]["title"][l]}')
st.write(_["search"]["instructions"][l])

mslist_df = pd.read_csv(mslist_path)
mslist_df.fillna("", inplace=True)
st.write(f'**{mslist_df.shape[0]}**{_["search"]["cards_are_legal"][l]}')

name_input = st.text_input(_["search"]["search_by_card_name"][l]).strip()
exact_match = lib.get_legal_cardnames(name_input, mslist_df)
results_en_df = mslist_df[
    mslist_df["name"].str.contains(name_input.lower(), case=False)
]
results_ja_df = mslist_df[
    mslist_df["name_ja"].str.contains(name_input.lower(), case=False)
]
results_df = results_en_df.merge(results_ja_df, how="outer")
if name_input:
    if exact_match[0]:
        cardname = exact_match[1]
        if exact_match[2] is not None:
            cardname = f"{cardname} / {exact_match[2]}"
        st.write(
            f'✅ [{cardname}]({lib.compose_scryfall_url(exact_match[1])}) {_["search"]["exact_match"][l]}'
        )
    st.write(f'**{results_df.shape[0]}**{_["search"]["cards_found"][l]}')
    if results_df.shape[0] > number_shown_results:
        st.write(_["search"]["top_results"][l])
    results_df["link"] = results_df["name"].apply(lib.compose_scryfall_url)
    results_df[:number_shown_results].transpose().apply(lib.row_to_link)

streamlit_common.footer.write_footer()
