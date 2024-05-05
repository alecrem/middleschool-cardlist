import streamlit as st
import pandas as pd
import streamlit_common.footer
import streamlit_common.lib as lib
import streamlit_common.locale

mslist_path = "static/middleschool_extra_fields.csv"
_ = streamlit_common.locale.get_locale()

if "number_shown_results" not in st.session_state:
    st.session_state["number_shown_results"] = 20
if "lang" not in st.session_state:
    st.session_state["lang"] = "en"


def add_more_results():
    st.session_state["number_shown_results"] += 20


def reset_more_results():
    st.session_state["number_shown_results"] = 20


st.set_page_config(
    page_title="Middle School Tutor | Card Search",
    page_icon="favicon.ico",
    layout="wide",
)
lang = st.sidebar.radio(
    label="Language / 言語",
    options=["English", "日本語"],
    index=1 if st.session_state["lang"] == "ja" else 0,
)
st.session_state["lang"] = "ja" if lang == "日本語" else "en"
l = st.session_state["lang"]
headcol1, headcol2 = st.columns([1, 7])
headcol1.image("favicon.ico", width=80)
headcol2.write(f"# Middle School Tutor")
st.write(f'## {_["search"]["title"][l]}')
st.write(_["search"]["instructions"][l])

mslist_df = pd.read_csv(mslist_path)
mslist_df.fillna("", inplace=True)
st.write(f'**{mslist_df.shape[0]}**{_["search"]["cards_are_legal"][l]}')

results_df = mslist_df

# Filter by card name
input_name = st.text_input(
    f'**{_["search"]["search_by_card_name"][l]}**',
    placeholder=_["search"]["search_by_card_name_placeholder"][l],
).strip()
exact_match = lib.get_legal_cardnames(input_name, mslist_df)
results_en_df = results_df[results_df["name"].str.contains(input_name, case=False)]
results_ja_df = results_df[results_df["name_ja"].str.contains(input_name, case=False)]
results_df = results_en_df.merge(results_ja_df, how="outer")

# Filter by color
(
    colorcol0,
    colorcol1,
    colorcol2,
    colorcol3,
    colorcol4,
    colorcol5,
    colorcol6,
) = st.columns(7)
colorcol0.write(f'**{_["search"]["search_by_color"][l]}**')
if colorcol1.checkbox(_["basic"]["color_w"][l]):
    results_df = results_df[results_df["w"] == True]
if colorcol2.checkbox(_["basic"]["color_u"][l]):
    results_df = results_df[results_df["u"] == True]
if colorcol3.checkbox(_["basic"]["color_b"][l]):
    results_df = results_df[results_df["b"] == True]
if colorcol4.checkbox(_["basic"]["color_r"][l]):
    results_df = results_df[results_df["r"] == True]
if colorcol5.checkbox(_["basic"]["color_g"][l]):
    results_df = results_df[results_df["g"] == True]
if colorcol6.checkbox(_["basic"]["color_c"][l]):
    results_df = results_df[results_df["c"] == True]

# Filter by mana value range
min_mv = mslist_df["mv"].min()
max_mv = mslist_df["mv"].max()
mv_options = [mv for mv in range(min_mv, max_mv + 1)]
start_mv, end_mv = st.select_slider(
    f'**{_["search"]["search_by_mv"][l]}**', options=mv_options, value=(min_mv, max_mv)
)
cond1 = results_df["mv"] >= start_mv
cond2 = results_df["mv"] <= end_mv
results_df = results_df[cond1 & cond2]

# Filter by type (select)
col1, col2 = st.columns(2)
type_list = streamlit_common.locale.get_type_options()
select_types = col1.multiselect(
    f'**{_["search"]["select_type"][l]}**',
    type_list[l],
    placeholder=_["search"]["select_type_placeholder"][l],
)
for cardtype in select_types:
    type_to_search = cardtype
    if l == "ja":
        type_to_search = type_list["en"][type_list["ja"].index(cardtype)]
    results_df = results_df[results_df["type"].str.contains(type_to_search, case=False)]

# Filter by type (text input)
input_type = col2.text_input(
    f'**{_["search"]["search_by_type"][l]}**',
    placeholder=_["search"]["search_by_type_placeholder"][l],
).strip()
results_df = results_df[results_df["type"].str.contains(input_type, case=False)]

# Filter by text
input_text = st.text_input(
    f'**{_["search"]["search_by_text"][l]}**',
    placeholder=_["search"]["search_by_text_placeholder"][l],
).strip()
results_df = results_df[results_df["text"].str.contains(input_text, case=False)]

# Filter by power and toughness ranges

powtou_df = mslist_df[mslist_df["power"].isin(range(0, 100))]

min_pow = int(powtou_df["power"].min(skipna=True))
max_pow = int(powtou_df["power"].max(skipna=True))
pow_range = range(min_pow, max_pow + 1)
pow_options = [pow for pow in pow_range]
start_pow, end_pow = st.select_slider(
    f'**{_["search"]["search_by_pow"][l]}**',
    options=pow_options,
    value=(min_pow, max_pow),
)
if start_pow > min_pow or end_pow < max_pow:
    results_df = results_df[results_df["power"].isin(pow_range)]
    results_df = results_df[results_df["power"] >= start_pow]
    results_df = results_df[results_df["power"] <= end_pow]

min_tou = int(powtou_df["toughness"].min(skipna=True))
max_tou = int(powtou_df["toughness"].max(skipna=True))
tou_range = range(min_tou, max_tou + 1)
tou_options = [tou for tou in tou_range]
start_tou, end_tou = st.select_slider(
    f'**{_["search"]["search_by_tou"][l]}**',
    options=tou_options,
    value=(min_tou, max_tou),
)
if start_tou > min_tou or end_tou < max_tou:
    results_df = results_df[results_df["toughness"].isin(tou_range)]
    results_df = results_df[results_df["toughness"] >= start_tou]
    results_df = results_df[results_df["toughness"] <= end_tou]

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
