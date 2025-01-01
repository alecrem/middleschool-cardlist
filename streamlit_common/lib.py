import streamlit as st
import pandas as pd
import re
import urllib.parse


def compose_scryfall_url(cardname: str) -> str:
    """Compose a Scryfall URL from the passed card name"""
    return f"https://scryfall.com/search?q=prefer%3Aoldest%20!%22{urllib.parse.quote_plus(cardname)}%22"


def row_to_button_link(row: pd.DataFrame) -> None:
    """Prints a list item with a Scryfall link for the card in the row passed"""
    cardname = row.English
    if row.日本語 != "":
        cardname = f"{cardname} / {row.日本語}"
    st.write(f"- [{cardname}]({compose_scryfall_url(row.English)})")


def get_legal_cardnames(cardname: str, mslist_df: pd.DataFrame) -> list:
    """Returns a list with legality (boolean) plus the English and Japanese
    names for the card if there is an exact match, or the user's input if there is not.
    """
    if len(cardname) < 1:
        return [False, [], []]
    cardname_en_list = []
    cardname_ja_list = []
    banned_list = []
    legal = False
    banned = False
    english_match = mslist_df[mslist_df["name"].str.lower() == cardname.lower()]
    if english_match.shape[0] > 0:
        legal = True
        cardname_en_list = english_match["name"].to_list()
        cardname_ja_list = english_match["name_ja"].to_list()
        banned_list = english_match["banned"].to_list()
    japanese_match = mslist_df[mslist_df["name_ja"] == cardname]
    if japanese_match.shape[0] > 0:
        legal = True
        cardname_en_list = japanese_match["name"].to_list()
        cardname_ja_list = japanese_match["name_ja"].to_list()
        banned_list = japanese_match["banned"].to_list()
    if len(cardname_en_list) > 0:
        legalname_en = cardname_en_list[0]
    else:
        legalname_en = cardname
    if len(cardname_ja_list) > 0:
        legalname_ja = cardname_ja_list[0]
    else:
        legalname_ja = cardname
    if len(banned_list) > 0:
        banned = banned_list[0]
    else:
        banned = False
    return [legal, legalname_en, legalname_ja, banned]


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


def split_names_list(row: pd.DataFrame):
    """Splits the English and Japanese card names in a list into two different columns"""
    if not isinstance(row["legalnames"], list):
        return row
    row["islegal"] = row["legalnames"][0]
    row["English"] = row["legalnames"][1]
    if row["legalnames"][1] is not None:
        row["日本語"] = row["legalnames"][2]
    row["isbanned"] = row["legalnames"][3]
    return row
