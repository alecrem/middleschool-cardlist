# Important: run this script from the parent directory
# (the root directory in this repository)
#
# python3 list_scripts/8_add_other_fields.py

import json
import pandas as pd
import re


def add_other_fields(row: pd.DataFrame) -> pd.DataFrame:
    print(f"{row['name']} | {row['oracle_id']}")
    for index, card in enumerate(cards):
        if card["identifiers"]["scryfallOracleId"] == row["oracle_id"]:
            row["mv"] = card["manaValue"]
            row["rarity"] = card["rarity"]
            row["text"] = card["text"] if "text" in card else None
            row["type"] = card["type"]
            if "power" in card:
                power = re.sub("[^0-9]", "", f"0{card['power']}")
                row["power"] = int(power)
            else:
                row["power"] = None
            if "toughness" in card:
                toughness = re.sub("[^0-9]", "", f"0{card['toughness']}")
                row["toughness"] = int(toughness)
            else:
                row["toughness"] = None
            colors = card["colors"]
            row["w"] = True if "W" in colors else False
            row["u"] = True if "U" in colors else False
            row["b"] = True if "B" in colors else False
            row["r"] = True if "R" in colors else False
            row["g"] = True if "G" in colors else False
            row["c"] = True if len(colors) < 1 else False
            return row
    return row


middleschool_df = pd.read_csv("static/middleschool.csv")
ms_with_banned_df = pd.read_csv("static/middleschool_with_banned.csv")
with open("data/middleschool.json") as json_data:
    cards = json.loads(json_data.read())

middleschool_df = middleschool_df.apply(add_other_fields, axis=1)
middleschool_df["power"] = middleschool_df["power"].astype("Int64")
middleschool_df["toughness"] = middleschool_df["toughness"].astype("Int64")

ms_with_banned_df = ms_with_banned_df.apply(add_other_fields, axis=1)
ms_with_banned_df["power"] = ms_with_banned_df["power"].astype("Int64")
ms_with_banned_df["toughness"] = ms_with_banned_df["toughness"].astype("Int64")

middleschool_df.to_csv("static/middleschool_extra_fields.csv")
middleschool_df.to_json("static/middleschool_extra_fields.json")
ms_with_banned_df.to_csv("static/middleschool_extra_fields_with_banned.csv")
ms_with_banned_df.to_json("static/middleschool_extra_fields_with_banned.json")
