#!/usr/bin/env python3
"""
Fix split card data in output files.

This script corrects two issues with split cards:
1. Only first half's colors are included (should combine both halves)
2. Only first half's rules text is included (should combine both halves with ' // ')

Input: static/middleschool_extra_fields_with_banned_images.csv
Output: New CSV and JSON files with corrected split card data
"""

import csv
import json
import sys
from pathlib import Path

def load_mtg_data():
    """Load MTG JSON data from INV and APC sets."""
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / "data"
    
    inv_file = data_dir / "set_INV.json"
    apc_file = data_dir / "set_APC.json"
    
    with open(inv_file, 'r', encoding='utf-8') as f:
        inv_data = json.load(f)
    
    with open(apc_file, 'r', encoding='utf-8') as f:
        apc_data = json.load(f)
    
    return inv_data + apc_data

def find_split_cards(mtg_data):
    """Find all split cards and organize them by name."""
    split_cards = {}
    
    for card in mtg_data:
        if card.get('layout') == 'split' and '//' in card.get('name', ''):
            name = card['name']
            if name not in split_cards:
                split_cards[name] = {}
            
            side = card.get('side', 'a')
            split_cards[name][side] = card
    
    return split_cards

def get_combined_colors(split_card_data):
    """Get combined colors from both halves of split card."""
    # Use colorIdentity which contains combined colors from both halves
    if 'a' in split_card_data:
        return split_card_data['a'].get('colorIdentity', [])
    elif 'b' in split_card_data:
        return split_card_data['b'].get('colorIdentity', [])
    return []

def get_combined_text(split_card_data):
    """Get combined rules text from both halves separated by ' // '."""
    side_a_text = ""
    side_b_text = ""
    
    if 'a' in split_card_data:
        side_a_text = split_card_data['a'].get('text', '')
    
    if 'b' in split_card_data:
        side_b_text = split_card_data['b'].get('text', '')
    
    return f"{side_a_text} // {side_b_text}"

def get_combined_japanese_name(split_card_data):
    """Get combined Japanese name from both halves separated by ' // '."""
    side_a_ja = ""
    side_b_ja = ""
    
    # Get Japanese faceName from both sides
    if 'a' in split_card_data:
        foreign_data = split_card_data['a'].get('foreignData', [])
        for foreign in foreign_data:
            if foreign.get('language') == 'Japanese':
                side_a_ja = foreign.get('faceName', '')
                break
    
    if 'b' in split_card_data:
        foreign_data = split_card_data['b'].get('foreignData', [])
        for foreign in foreign_data:
            if foreign.get('language') == 'Japanese':
                side_b_ja = foreign.get('faceName', '')
                break
    
    # Handle inconsistent data: if side A already has both parts, use it
    if side_a_ja and '//' in side_a_ja:
        return side_a_ja
    elif side_a_ja and side_b_ja:
        return f"{side_a_ja} // {side_b_ja}"
    
    return ""

def color_identity_to_bool_flags(color_identity):
    """Convert color identity list to boolean flags for CSV."""
    return {
        'White': 'W' in color_identity,
        'Blue': 'U' in color_identity,
        'Black': 'B' in color_identity,
        'Red': 'R' in color_identity,
        'Green': 'G' in color_identity,
        'Colorless': len(color_identity) == 0
    }

def main():
    print("Loading MTG data...")
    mtg_data = load_mtg_data()
    
    print("Finding split cards...")
    split_cards = find_split_cards(mtg_data)
    
    print(f"Found {len(split_cards)} split cards:")
    for name in split_cards:
        print(f"  - {name}")
    
    # Load input CSV
    script_dir = Path(__file__).parent
    input_file = script_dir.parent / "static" / "middleschool_extra_fields_with_banned_images.csv"
    
    print(f"Loading input file: {input_file}")
    
    rows = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    print(f"Loaded {len(rows)} cards from input file")
    
    # Update split cards
    updated_count = 0
    for row in rows:
        card_name = row.get('name', '')
        if '//' in card_name and card_name in split_cards:
            print(f"Updating split card: {card_name}")
            
            # Get combined data
            combined_colors = get_combined_colors(split_cards[card_name])
            combined_text = get_combined_text(split_cards[card_name])
            combined_japanese_name = get_combined_japanese_name(split_cards[card_name])
            color_flags = color_identity_to_bool_flags(combined_colors)
            
            # Update row
            row['text'] = combined_text
            if combined_japanese_name:
                row['name_ja'] = combined_japanese_name
            row['w'] = str(color_flags['White'])
            row['u'] = str(color_flags['Blue'])
            row['b'] = str(color_flags['Black'])
            row['r'] = str(color_flags['Red'])
            row['g'] = str(color_flags['Green'])
            row['c'] = str(color_flags['Colorless'])
            
            updated_count += 1
    
    print(f"Updated {updated_count} split cards")
    
    # Write updated CSV
    output_csv = script_dir.parent / "static" / "middleschool_extra_fields_with_banned_images_fixed_splits.csv"
    with open(output_csv, 'w', encoding='utf-8', newline='') as f:
        if rows:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
    
    print(f"Written corrected CSV to: {output_csv}")
    
    # Convert to JSON
    output_json = script_dir.parent / "static" / "middleschool_extra_fields_with_banned_images_fixed_splits.json"
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)
    
    print(f"Written corrected JSON to: {output_json}")
    
    print("Split card fix completed successfully!")

if __name__ == "__main__":
    main()