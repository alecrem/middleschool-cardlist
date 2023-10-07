# Download mtgjson data and extract it on the `data` directory
# Feel free to make the file available in any other way

# Important: run this script from the parent directory
# (the root directory in this repository)

cd data
wget "https://mtgjson.com/api/v5/AllPrintings.json.bz2"
bunzip2 AllPrintings.json.bz2
cd -
