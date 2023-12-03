---
sdk: streamlit
sdk_version: 1.25.0
app_file: "Middle_School_Card_Search.py"
---

# middleschool-cardlist

Composes a list of Magic cards legal in the Middle School format.

## List of Middle School legal cards

You can download the list in the following formats:

- [JSON (Oracle IDs and card names only)](output/middleschool.json)
- [CSV (Oracle IDs and card names only)](output/middleschool.csv)
- [JSON (with additional columns)](output/middleschool_extra_fields.json)
- [CSV (with additional columns)](output/middleschool_extra_fields.csv)

## Composing the list

Feel free to take a look at [the Jupyter notebook](https://github.com/alecrem/middleschool-cardlist/blob/main/middleschool-cardlist.ipynb) for a quick idea of the process (outdated version).

To actually compose the list, please run the shell and python scripts in the `list_scripts` directory in order.

### Requirements

Command line utilities:

- [wget](https://www.gnu.org/software/wget/)
- [bzip2](https://sourceware.org/bzip2/)
- [jq](https://stedolan.github.io/jq/)

Python modules:

- json
- pandas
- requests_html

## Streamlit web interface

This repository also hosts a web app where users can search for Middle School legal cards or check the legality of cards in a list.

The app is deployed here: [alecrem-middleschool.hf.space](https://alecrem-middleschool.hf.space/).

To run the Streamlit app locally, install the [streamlit](https://docs.streamlit.io/library/get-started) module and run:

```sh
streamlit run Middle_School_Card_Search.py
```
