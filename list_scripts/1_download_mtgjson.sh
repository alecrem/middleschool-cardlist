# Important: run this script from the parent directory
# (the root directory in this repository):
#
# sh list_scripts/1_download_mtgjson.sh

# Download mtgjson data and extract it on the `data` directory
# Feel free to make the file available in any other way

cd data
wget "https://mtgjson.com/api/v5/AllPrintings.json.bz2"
bunzip2 AllPrintings.json.bz2
cd -
