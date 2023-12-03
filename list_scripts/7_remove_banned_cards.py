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

# Write a CSV file
middleschool_df.to_csv("output/middleschool.csv")
middleschool_df.to_json("output/middleschool.json")
