import json
import pandas as pd

with open("data/middleschool.json") as json_data:
    cards = json.loads(json_data.read())

# Create a pandas DataFrame with all cards from all legal sets
column_names = ["oracle_id", "name", "name_ja"]
middleschool_df = pd.DataFrame(columns=column_names)
for card in cards:
    oracle_id = card["identifiers"]["scryfallOracleId"]
    name = card["name"]
    lang_ja = [lang for lang in card["foreignData"] if lang["language"] == "Japanese"]
    # Some cards do not have a Japanese name
    if len(lang_ja) > 0:
        name_ja = lang_ja[0]["name"]
    else:
        name_ja = None
    temporary_df = pd.DataFrame(
        {"oracle_id": [oracle_id], "name": [name], "name_ja": [name_ja]}
    )
    middleschool_df = pd.concat([middleschool_df, temporary_df])

# For cards with multiple occurrences, put the rows that have the Japanese name on top
middleschool_df = middleschool_df.sort_values(by=["name", "name_ja"])
# For cards with multiple occurrences, delete all rows except for the top one
middleschool_df = middleschool_df.drop_duplicates(subset=["oracle_id"])

# Write a CSV file
middleschool_df.to_csv("data/middleschool_all_sets.csv")
