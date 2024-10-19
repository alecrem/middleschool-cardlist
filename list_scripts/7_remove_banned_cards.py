# Important: run this script from the parent directory
# (the root directory in this repository)
#
# python3 list_scripts/7_remove_banned_cards.py

import pandas as pd

# Remove cards that are banned in the format
banlist = [
    "Amulet of Quoz",
    "Balance",
    "Brainstorm",
    "Bronze Tablet",
    "Channel",
    "Dark Ritual",
    "Demonic Consultation",
    "Flash",
    "Goblin Recruiter",
    "Imperial Seal",
    "Jeweled Bird",
    "Mana Crypt",
    "Mana Vault",
    "Memory Jar",
    "Mind's Desire",
    "Mind Twist",
    "Rebirth",
    "Strip Mine",
    "Tempest Efreet",
    "Timmerian Fiends",
    "Tolarian Academy",
    "Vampiric Tutor",
    "Windfall",
    "Yawgmoth's Bargain",
    "Yawgmoth's Will",
]

middleschool_df = pd.read_csv("data/middleschool_all_sets_added_japanese_names.csv")
ms_with_banned_df = middleschool_df

print("Cards legal by set:", middleschool_df.shape[0])
# Find the rows with the banned cards
banned_df = middleschool_df[
    pd.DataFrame(middleschool_df.name.tolist()).isin(banlist).any(axis=1).values
]
print("Banned cards:", banned_df.shape[0])

# Append the banned cards to the main Middle School DataFrame,
# then remove any rows that appear twice,
# effectively leaving only the legal cards
middleschool_df = pd.concat([middleschool_df, banned_df]).drop_duplicates(keep=False)
print("Cards legal by set and not banned:", middleschool_df.shape[0])
middleschool_df = middleschool_df.reset_index(drop=True)
middleschool_df = middleschool_df[["oracle_id", "name", "name_ja"]]
middleschool_df = middleschool_df.sort_values(by=["name", "name_ja"])

# Make a dataframe including the banned cards,
ms_with_banned_df["banned"] = ms_with_banned_df["name"].apply(lambda x: x in banlist)
ms_with_banned_df = ms_with_banned_df.reset_index(drop=True)
ms_with_banned_df = ms_with_banned_df[["oracle_id", "name", "name_ja", "banned"]]
ms_with_banned_df = ms_with_banned_df.sort_values(by=["name", "name_ja"])
print(ms_with_banned_df[ms_with_banned_df["name"] == "Balance"])
print(ms_with_banned_df[ms_with_banned_df["name"] == "Lightning Bolt"])

# Write CSV and JSON files
middleschool_df.to_csv("static/middleschool.csv")
middleschool_df.to_json("static/middleschool.json")
ms_with_banned_df.to_csv("static/middleschool_with_banned.csv")
ms_with_banned_df.to_json("static/middleschool_with_banned.json")
