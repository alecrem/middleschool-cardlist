# Important: run this script from the parent directory
# (the root directory in this repository)
#
# python3 list_scripts/8_add_other_fields.py

import json
import pandas as pd


def add_other_fields(row: pd.DataFrame) -> pd.DataFrame:
    print(f"{row['name']} | {row['oracle_id']}")
    for index, card in enumerate(cards):
        if card["identifiers"]["scryfallOracleId"] == row["oracle_id"]:
            row["mv"] = card["manaValue"]
            row["rarity"] = card["rarity"]
            row["text"] = card["text"] if "text" in card else None
            row["type"] = card["type"]
            row["power"] = card["power"] if "power" in card else None
            row["toughness"] = card["toughness"] if "toughness" in card else None
            colors = card["colors"]
            row["w"] = True if "W" in colors else False
            row["u"] = True if "U" in colors else False
            row["b"] = True if "B" in colors else False
            row["r"] = True if "R" in colors else False
            row["g"] = True if "G" in colors else False
            row["c"] = True if len(colors) < 1 else False
            return row
    return row


middleschool_df = pd.read_csv("output/middleschool.csv")
with open("data/middleschool.json") as json_data:
    cards = json.loads(json_data.read())

middleschool_df = middleschool_df.apply(add_other_fields, axis=1)

middleschool_df.to_csv("output/middleschool_extra_fields.csv")
middleschool_df.to_json("output/middleschool_extra_fields.json")
