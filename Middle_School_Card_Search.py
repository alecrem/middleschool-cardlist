import streamlit as st
import pandas as pd
import streamlit_common.footer
import streamlit_common.lib as lib
import streamlit_common.locale

mslist_path = "output/middleschool_extra_fields.csv"
_ = streamlit_common.locale.get_locale()

if "number_shown_results" not in st.session_state:
    st.session_state["number_shown_results"] = 20


def add_more_results():
    st.session_state["number_shown_results"] += 20


def reset_more_results():
    st.session_state["number_shown_results"] = 20


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

col1, col2 = st.columns(2)

# Filter by type (select)
select_types = col1.multiselect(
    _["search"]["select_type"][l],
    ["Artifact", "Creature", "Enchantment", "Instant", "Land", "Sorcery"],
)
for cardtype in select_types:
    results_df = results_df[results_df["type"].str.contains(cardtype, case=False)]

# Filter by type (text input)
input_type = col2.text_input(_["search"]["search_by_type"][l]).strip()
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
    if results_df.shape[0] > st.session_state["number_shown_results"]:
        st.write(_["search"]["top_results"][l])

    results_df["link"] = results_df["name"].apply(lib.compose_scryfall_url)
    results_df[: st.session_state["number_shown_results"]].transpose().apply(
        lib.row_to_link
    )

    if results_df.shape[0] > st.session_state["number_shown_results"]:
        st.button(label=_["search"]["see_more"][l], on_click=add_more_results)
    if st.session_state["number_shown_results"] > 20:
        st.button(
            label=_["search"]["see_20"][l],
            on_click=reset_more_results,
        )

streamlit_common.footer.write_footer()
