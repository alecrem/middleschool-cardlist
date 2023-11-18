---
sdk: streamlit
sdk_version: 1.25.0
---

# middleschool-cardlist

Composes a list of Magic cards legal in the Middle School format

## List of Middle School legal cards

You can download the list in the following formats:

- [JSON](output/middleschool.json)
- [CSV](output/middleschool.csv)

## The process: the Jupyter notebook

Feel free to take a look at [the notebook](https://github.com/alecrem/middleschool-cardlist/blob/main/middleschool-cardlist.ipynb)

### Requirements to run the notebook

Command line utilities:

- [wget](https://www.gnu.org/software/wget/)
- [bzip2](https://sourceware.org/bzip2/)
- [jq](https://stedolan.github.io/jq/)

Python modules:

- json
- pandas
- requests_html

## Streamlit web interface

The app is deployed here: [middleschoolmtg.streamlit.app](https://middleschoolmtg.streamlit.app/)

To run the Streamlit app locally, install the [streamlit](https://docs.streamlit.io/library/get-started) module and run:

```sh
streamlit run Middle_School_Card_List.py
```
