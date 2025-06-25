# Project Plan: Add Image URIs to Card List (Issue #97)

## Problem Analysis
The task is to add a new script `9_add_image_uris.py` that will:
1. Read the existing `static/middleschool_extra_fields_with_banned.csv` file
2. For each card, make a request to the Scryfall API to get image URIs
3. Add a new `image_small` column with the small image URI from Scryfall
4. Save the enhanced data as both CSV and JSON files
5. Update the README with documentation for the new script

## Implementation Plan

### Todo Items:
- [ ] Create `list_scripts/9_add_image_uris.py` script
- [ ] Implement Scryfall API integration for fetching image URIs
- [ ] Add error handling for API requests and missing cards
- [ ] Generate output files: `static/middleschool_extra_fields_with_banned_images.csv` and `.json`
- [ ] Update README.md with documentation for the new script
- [ ] Test the script to ensure it works correctly
- [ ] Commit the changes

### Technical Details:
1. **Input**: `static/middleschool_extra_fields_with_banned.csv`
2. **Processing**: 
   - Read CSV into pandas DataFrame
   - For each card, query Scryfall API `cards/named` endpoint
   - Extract `image_uris.small` from API response
   - Add to new `image_small` column
3. **Output**: 
   - `static/middleschool_extra_fields_with_banned_images.csv`
   - `static/middleschool_extra_fields_with_banned_images.json`
4. **API**: Scryfall `cards/named` endpoint with exact name and set parameters

### Code Structure:
Following the pattern of existing scripts:
- Use pandas for data manipulation
- Include proper error handling
- Add progress indicators
- Follow the existing code style and patterns
- Include proper documentation

### Files to Modify/Create:
- `list_scripts/9_add_image_uris.py` (new)
- `static/middleschool_extra_fields_with_banned_images.csv` (new)
- `static/middleschool_extra_fields_with_banned_images.json` (new)
- `README.md` (update)

This plan focuses on creating a simple, focused script that adds image URI functionality while following the existing patterns in the codebase.

## Review

### Changes Made:
- ✅ Created `list_scripts/9_add_image_uris.py` script
- ✅ Implemented Scryfall API integration with proper rate limiting (0.1s delay = max 10 requests/second)
- ✅ Added comprehensive error handling for API failures and missing cards
- ✅ Included --test flag for development and testing with first 20 cards
- ✅ Updated README.md with new file listings and script documentation
- ✅ Added `requests` to Python module requirements
- ✅ Added `.claude` to .gitignore
- ✅ Successfully tested script with sample data

### Script Features:
- Reads from `static/middleschool_extra_fields_with_banned.csv`
- Maps cards to their sets using `data/middleschool.json`
- Queries Scryfall API `cards/named` endpoint with exact name and set
- Extracts `image_uris.small` property and adds to `image_small` column
- Generates both CSV and JSON output files
- Includes progress tracking and success/failure reporting
- Respects Scryfall's API rate limits

### Test Results:
- Successfully processed 20 test cards with 100% success rate
- All image URLs are valid and return proper images
- Script handles various card types and sets correctly
- Error handling works for missing data scenarios

The implementation is complete and ready for production use. The script will take approximately 10 minutes to process all ~5,800 cards due to API rate limiting, which is acceptable given the constraint.