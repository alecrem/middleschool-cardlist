import streamlit as st
import pandas as pd
import re
import urllib.parse


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


def remove_number_of_copies(line: str) -> str:
    if len(line.strip()) < 1:
        return None
    pattern = re.compile("^([0-9]+) +")
    return pattern.sub("", line)


def is_cardname_legal(cardname: str, mslist_df: pd.DataFrame) -> bool:
    if mslist_df[mslist_df["name"].str.lower() == cardname.lower()].shape[0] > 0:
        return True
    if mslist_df[mslist_df["name_ja"] == cardname].shape[0] > 0:
        return True
    return False
