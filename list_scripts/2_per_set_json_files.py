# Important: run this script from the parent directory
# (the root directory in this repository)
#
# python3 list_scripts/2_per_set_json_files.py
#
# Then, run the newly generated bash script:
#
# sh list_scripts/3_separate_json_files_per_set.sh

# The Raw data is very large, so let's make JSON files for all relevant sets
# Note: this can take a couple minutes to run

setlist = [
    "4ED",
    "ICE",
    "CHR",
    "HML",
    "ALL",
    "MIR",
    "VIS",
    "5ED",
    "WTH",
    "POR",
    "TMP",
    "STH",
    "EXO",
    "P02",
    "USG",
    "ULG",
    "6ED",
    "UDS",
    "PTK",
    "S99",
    "MMQ",
    "NEM",
    "PCY",
    "S00",
    "INV",
    "PLS",
    "7ED",
    "APC",
    "ODY",
    "TOR",
    "JUD",
    "ONS",
    "LGN",
    "SCG",
    "PDRC",
    "PHPR",
    "ATH",
    "BRB",
    "BTD",
    "DKM",
]
with open("list_scripts/3_separate_json_files_per_set.sh", "w") as f:
    for set in setlist:
        # Write a separate JSON document for each Middle School legal set
        line = f"cat data/AllPrintings.json | jq '.data.\"{set}\".cards' > data/set_{set}.json"
        f.write(line + "\n")
    line = "jq -s add data/set_* > data/middleschool.json"
    f.write(line + "\n")
