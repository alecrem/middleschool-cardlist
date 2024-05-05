import streamlit as st
import pandas as pd
import streamlit_common.footer
import streamlit_common.lib as lib
import streamlit_common.locale

mslist_path = "static/middleschool.csv"
_ = streamlit_common.locale.get_locale()

if "lang" not in st.session_state:
    st.session_state["lang"] = "en"

st.set_page_config(
    page_title="Middle School Tutor | Check Card List",
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
st.write(f'## {_["check"]["title"][l]}')
st.write(_["check"]["instructions"][l])

mslist_df = pd.read_csv(mslist_path)
mslist_df.fillna("", inplace=True)

col1, col2 = st.columns(2)

input_list = col1.text_area(
    label=f'##### {_["check"]["card_list"][l]}',
    placeholder="4 Lightning Bolt\n4 ボール・ライトニング",
    height=400,
)

cardnames = []

for line in input_list.split("\n"):
    cardname = lib.remove_number_of_copies(line)
    if cardname is not None:
        cardnames.append(lib.remove_number_of_copies(cardname))

input_cards = pd.DataFrame(cardnames, columns=["cardname"])
input_cards["legalnames"] = input_cards["cardname"].apply(
    lib.get_legal_cardnames, args=[mslist_df]
)
input_cards = input_cards.apply(lib.split_names_list, axis=1)
input_cards = input_cards.apply(lib.legal_to_checkmark, axis=1)
if input_cards.shape[0] > 0:
    input_cards = input_cards.sort_values(by="Legal", ascending=False)

illegal_cards = 0
if input_cards.shape[0] > 0:
    illegal_cards = input_cards[input_cards["Legal"] != "✅"].shape[0]

col2.write(
    f'##### {_["check"]["illegal_cards_1"][l]}{illegal_cards}{_["check"]["illegal_cards_2"][l]}'
)
if "English" in input_cards and "日本語" in input_cards:
    col2.dataframe(
        input_cards[["Legal", "English", "日本語"]],
        use_container_width=True,
        hide_index=True,
    )

if input_cards.shape[0] > 0:
    input_cards[input_cards["Legal"] == "✅"].apply(lib.row_to_button_link, axis=1)

streamlit_common.footer.write_footer()
