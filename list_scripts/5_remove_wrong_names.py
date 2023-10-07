import pandas as pd

# Remove Japanese card names that are wrong on MTGJSON
wrongnames = [
    "Aether Barrier",
    "Aether Burst",
    "Aether Charge",
    "Aether Flash",
    "Aether Mutation",
    "Aether Sting",
    "Aether Storm",
    "Aether Tide",
    "Tainted Aether",
    "Tar Pit Warrior",
]

middleschool_df = pd.read_csv("data/middleschool_all_sets.csv")

# Write a CSV file
middleschool_df.to_csv("data/middleschool_all_sets_removed_wrong_names.csv")
