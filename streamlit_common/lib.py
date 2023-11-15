import streamlit as st
import pandas as pd
import re
import urllib.parse


def compose_scryfall_url(cardname: str) -> str:
    """Compose a Scryfall URL from the passed card name"""
    return f"https://scryfall.com/search?q=prefer%3Aoldest%20!%22{urllib.parse.quote_plus(cardname)}%22"


def row_to_link(row: pd.DataFrame) -> None:
    """Prints a list item with a Scryfall link for the card in the row passed"""
    cardname = row["name"]
    if row.name_ja is not "":
        cardname = f"{cardname} / {row.name_ja}"
    st.markdown(f"- [{cardname}]({row.link})")


def get_legal_cardnames(cardname: str, mslist_df: pd.DataFrame) -> list:
    """Returns a list with the English and Japanese names for the card
    if there is an exact match, or `None` if there is not.
    """
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
    """Remove the number of copies in front of the card name
    from a line in a card list
    """
    if len(line.strip()) < 1:
        return None
    pattern = re.compile("^([0-9]+) +")
    return pattern.sub("", line)


def is_cardname_legal(cardname: str, mslist_df: pd.DataFrame) -> bool:
    """Returns wether a card with exactly the passed name is legal in the format"""
    if mslist_df[mslist_df["name"].str.lower() == cardname.lower()].shape[0] > 0:
        return True
    if mslist_df[mslist_df["name_ja"] == cardname].shape[0] > 0:
        return True
    return False
