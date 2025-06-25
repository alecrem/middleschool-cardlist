# Important: run this script from the parent directory
# (the root directory in this repository)
#
# python3 list_scripts/9_add_image_uris.py

import json
import pandas as pd
import requests
import time
import sys
from urllib.parse import quote


def get_card_set(oracle_id: str, cards_data: list) -> str:
    """Find the set code for a card given its oracle ID."""
    for card in cards_data:
        if card["identifiers"]["scryfallOracleId"] == oracle_id:
            return card["setCode"]
    return None


def fetch_image_uri(name: str, set_code: str) -> str:
    """Fetch image URI from Scryfall API with rate limiting."""
    # Rate limiting: max 10 requests per second
    time.sleep(0.1)
    
    url = "https://api.scryfall.com/cards/named"
    params = {
        "exact": name,
        "set": set_code
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if "image_uris" in data and "small" in data["image_uris"]:
                return data["image_uris"]["small"]
            else:
                print(f"Warning: No small image URI found for {name} in set {set_code}")
                return None
        else:
            print(f"Warning: API request failed for {name} in set {set_code} (status: {response.status_code})")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Request failed for {name} in set {set_code}: {e}")
        return None
    except Exception as e:
        print(f"Error: Unexpected error for {name} in set {set_code}: {e}")
        return None


def add_image_uris(df: pd.DataFrame, cards_data: list) -> pd.DataFrame:
    """Add image_small column to the dataframe."""
    df = df.copy()
    df["image_small"] = None
    
    print(f"Processing {len(df)} cards...")
    
    for index, row in df.iterrows():
        oracle_id = row["oracle_id"]
        name = row["name"]
        
        # Find the set code for this card
        set_code = get_card_set(oracle_id, cards_data)
        
        if set_code is None:
            print(f"Warning: Could not find set code for {name} (oracle_id: {oracle_id})")
            continue
            
        print(f"Processing {index + 1}/{len(df)}: {name} from {set_code}")
        
        # Fetch image URI from Scryfall
        image_uri = fetch_image_uri(name, set_code)
        df.at[index, "image_small"] = image_uri
    
    return df


def main():
    # Check for test mode
    test_mode = len(sys.argv) > 1 and sys.argv[1] == "--test"
    
    print("Loading data files...")
    
    # Load the CSV file with card data
    try:
        df = pd.read_csv("static/middleschool_extra_fields_with_banned.csv")
        if test_mode:
            df = df.head(20)
            print(f"TEST MODE: Using first 20 cards only")
        print(f"Loaded {len(df)} cards from CSV")
    except FileNotFoundError:
        print("Error: Could not find static/middleschool_extra_fields_with_banned.csv")
        sys.exit(1)
    
    # Load the JSON file with card details including set codes
    try:
        with open("data/middleschool.json") as json_file:
            cards_data = json.load(json_file)
        print(f"Loaded {len(cards_data)} cards from JSON")
    except FileNotFoundError:
        print("Error: Could not find data/middleschool.json")
        sys.exit(1)
    
    # Add image URIs
    print("Starting to fetch image URIs from Scryfall API...")
    df_with_images = add_image_uris(df, cards_data)
    
    # Count successful image fetches
    successful_images = df_with_images["image_small"].notna().sum()
    print(f"Successfully fetched {successful_images}/{len(df)} image URIs")
    
    # Save the results
    print("Saving results...")
    if test_mode:
        output_csv = "static/test_middleschool_extra_fields_with_banned_images.csv"
        output_json = "static/test_middleschool_extra_fields_with_banned_images.json"
    else:
        output_csv = "static/middleschool_extra_fields_with_banned_images.csv"
        output_json = "static/middleschool_extra_fields_with_banned_images.json"
    
    df_with_images.to_csv(output_csv, index=False)
    df_with_images.to_json(output_json, orient="records", indent=2)
    
    print(f"Results saved to:")
    print(f"  - {output_csv}")
    print(f"  - {output_json}")
    print("Done!")


if __name__ == "__main__":
    main()