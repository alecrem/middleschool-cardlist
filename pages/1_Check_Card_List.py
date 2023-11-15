import streamlit as st
import pandas as pd
import streamlit_common.footer
import streamlit_common.lib as lib

mslist_path = "output/middleschool.csv"

st.set_page_config(
    page_title="Middle School | Check Card List",
    page_icon="🃏",
    layout="wide",
)
st.write(
    """
    # Middle School List Check

    Paste or type your list here to confirm that every card in it is Middle School legal.
    """
)

mslist_df = pd.read_csv(mslist_path)
mslist_df.fillna("", inplace=True)

col1, col2 = st.columns(2)

input_list = col1.text_area(
    label="##### Card list", placeholder="4 Lightning Bolt\n4 ボール・ライトニング", height=400
)

cardnames = []

for line in input_list.split("\n"):
    cardname = lib.remove_number_of_copies(line)
    if cardname is not None:
        cardnames.append(lib.remove_number_of_copies(cardname))

input_cards = pd.DataFrame(cardnames, columns=["cardname"])
input_cards["legal"] = input_cards["cardname"].apply(
    lib.is_cardname_legal, args=[mslist_df]
)

col2.write("##### Middle School legality")
col2.dataframe(input_cards[["legal", "cardname"]], use_container_width=True)

streamlit_common.footer.write_footer()
