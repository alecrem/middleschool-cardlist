# Project Plan: Fix Split Card Data in Output Files

## Problem Description
We need to add a new script in `list_scripts/` to fix split card data in our output files. There are 10 split cards in our card pool that have two issues:
1. Only the color of the first card is considered, while colors for both cards should count (e.g., Fire // Ice should be red and blue, not just red)
2. The rules text for the second half of the card is not present - we should have text for both halves separated by " // "

## Data Source
- Input: `static/middleschool_extra_fields_with_banned_images.csv`
- Output: New CSV and JSON files with corrected split card data
- Reference data: `data/set_INV.json` contains complete details for all 10 split cards

## Todo Items

### [x] 1. Create a script to fix split card data in our output files
- ✅ Created `list_scripts/10_fix_split_cards.py`
- ✅ Follows naming convention of existing scripts

### [x] 2. Identify all 10 split cards in our card pool by searching for '//' in names
- ✅ Successfully identified all 10 split cards:
  - Stand // Deliver, Spite // Malice, Pain // Suffering, Assault // Battery, Wax // Wane
  - Fire // Ice, Illusion // Reality, Life // Death, Night // Day, Order // Chaos

### [x] 3. Find corresponding split card data in data/set_INV.json for 5 split cards and data/set_APC.json for the other 5 split cards (including Fire // Ice)
- ✅ Successfully loaded data from both INV and APC sets
- ✅ Found and organized both halves (side "a" and side "b") for each split card

### [x] 4. Combine colors from both halves of split cards (e.g., Fire // Ice should be red and blue)
- ✅ Used `colorIdentity` field which contains combined colors from both halves
- ✅ Fire // Ice now correctly shows as red and blue
- ✅ Assault // Battery correctly shows as red and green

### [x] 5. Combine rules text from both halves separated by ' // '
- ✅ Successfully combined text from both sides with " // " separator
- ✅ Example: Fire // Ice shows "Fire deals 2 damage divided as you choose among one or two targets. // Tap target permanent. Draw a card."

### [x] 6. Generate new CSV and JSON output files with corrected split card data
- ✅ Generated `static/middleschool_extra_fields_with_banned_images_fixed_splits.csv`
- ✅ Generated `static/middleschool_extra_fields_with_banned_images_fixed_splits.json`
- ✅ Updated all 10 split cards successfully

## Technical Implementation Details

### Split Card Data Structure
Split cards in MTG JSON are represented as two separate objects:
- Each half has its own `uuid`, `colors`, `manaCost`, `text`, and `side` properties
- Both halves share the same `name` and have `layout: "split"`
- The `colorIdentity` field contains the combined colors from both halves
- Cross-references exist via `otherFaceIds` array

### Expected Outcome
- Fire // Ice will show as red and blue (not just red)
- Rules text will show: "Fire deals 2 damage divided as you choose among one or two targets. // Tap target permanent. Draw a card."
- All 10 split cards will have corrected color and text data

## Review

### Summary of Changes
Successfully implemented a comprehensive fix for split card data issues in the middleschool cardlist project. Created `list_scripts/10_fix_split_cards.py` which:

1. **Identified all 10 split cards** in the card pool from both INV and APC sets
2. **Fixed color representation** by using the `colorIdentity` field from MTG JSON data that combines colors from both halves
3. **Combined rules text** from both halves of each split card with " // " separator
4. **Generated corrected output files** with all split cards properly updated

### Technical Implementation
- **Script Location**: `list_scripts/10_fix_split_cards.py`
- **Input**: `static/middleschool_extra_fields_with_banned_images.csv`
- **Output**: 
  - `static/middleschool_extra_fields_with_banned_images_fixed_splits.csv`
  - `static/middleschool_extra_fields_with_banned_images_fixed_splits.json`

### Verification Results
- **Fire // Ice**: Now correctly shows as red and blue (was red only)
- **Assault // Battery**: Now correctly shows as red and green
- **All 10 split cards updated**: Stand // Deliver, Spite // Malice, Pain // Suffering, Assault // Battery, Wax // Wane, Fire // Ice, Illusion // Reality, Life // Death, Night // Day, Order // Chaos

### Files Modified
- Created: `list_scripts/10_fix_split_cards.py`
- Generated: `static/middleschool_extra_fields_with_banned_images_fixed_splits.csv`
- Generated: `static/middleschool_extra_fields_with_banned_images_fixed_splits.json`

The implementation successfully resolves GitHub issue #99 by providing accurate color and rules text data for all split cards in the middleschool card pool.