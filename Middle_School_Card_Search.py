import streamlit as st
import pandas as pd
import streamlit_common.footer
import streamlit_common.lib as lib
import streamlit_common.locale

mslist_path = "output/middleschool_extra_fields.csv"
number_shown_results = 20
_ = streamlit_common.locale.get_locale()

st.set_page_config(
    page_title="MTG Middle School | Card Search",
    page_icon="🃏",
    layout="wide",
)
lang = st.sidebar.radio(
    label="Language / 言語",
    options=["English", "日本語"],
)
l = "ja" if lang == "日本語" else "en"
st.write(f'# {_["search"]["title"][l]}')
st.write(_["search"]["instructions"][l])

mslist_df = pd.read_csv(mslist_path)
mslist_df.fillna("", inplace=True)
st.write(f'**{mslist_df.shape[0]}**{_["search"]["cards_are_legal"][l]}')

results_df = mslist_df

# Filter by card name
input_name = st.text_input(_["search"]["search_by_card_name"][l]).strip()
exact_match = lib.get_legal_cardnames(input_name, mslist_df)
results_en_df = results_df[results_df["name"].str.contains(input_name, case=False)]
results_ja_df = results_df[results_df["name_ja"].str.contains(input_name, case=False)]
results_df = results_en_df.merge(results_ja_df, how="outer")

# Filter by type
input_type = st.text_input(_["search"]["search_by_type"][l]).strip()
results_df = results_df[results_df["type"].str.contains(input_type, case=False)]

# Filter by text
input_text = st.text_input(_["search"]["search_by_text"][l]).strip()
results_df = results_df[results_df["text"].str.contains(input_text, case=False)]

if results_df.shape[0] < mslist_df.shape[0]:
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
