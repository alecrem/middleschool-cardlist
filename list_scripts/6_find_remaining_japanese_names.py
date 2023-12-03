# Important: run this script from the parent directory
# (the root directory in this repository)
#
# python3 list_scripts/6_find_remaining_japanese_names.py

import pandas as pd
import time
from requests_html import HTMLSession

middleschool_df = pd.read_csv("data/middleschool_all_sets_removed_wrong_names.csv")

session = HTMLSession()


def find_japanese_name(name):
    url = "http://whisper.wisdom-guild.net/card/" + name + "/"
    r = session.get(url)
    # Find the text on the <title> element in the HTML document
    title = r.html.find("title")[0].text
    # Find the position of the English card name within the title
    idx = title.find(name)
    # The Japanese name should be before the English name,
    # so if idx is 0, there is no Japanese name
    if idx == 0:
        print(f"{name} ->")
        return None
    # If the exact English card name can't be found, we look for a '/'
    if idx == -1:
        idx = title.find("/")
        # No '/' means no Japanese name
        if idx == -1:
            return None
        # Take only the Japanese name from the title
        name_ja = title[0:idx]
    else:
        # Take only the Japanese name from the title
        name_ja = title[0 : idx - 1]
    print(f"{name} -> {name_ja}")
    return name_ja


english_only_cards = middleschool_df[middleschool_df["name_ja"].isnull()]
name_list = english_only_cards["name"].to_list()
for idx, name in enumerate(name_list):
    middleschool_df.loc[
        middleschool_df["name"] == name, "name_ja"
    ] = find_japanese_name(name)
    time.sleep(1)

# Write a CSV file
middleschool_df.to_csv("data/middleschool_all_sets_added_japanese_names.csv")
