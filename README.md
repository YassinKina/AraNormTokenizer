# Arabic Text Normalization & Tokenization Tool

This project is a simple web-based tool for preprocessing Arabic text, designed to assist in Natural Language Processing (NLP) tasks. It provides functionalities to normalize Arabic script and tokenize text into meaningful units, addressing some of the linguistic complexities unique to Arabic.

---

## Features

- **Text Normalization**  
  Removes diacritics, normalizes different forms of alif, converts taa marbuta, removes tatweel, and cleans punctuation to standardize input text.

- **Tokenization** 
  Splits text into tokens using whitespace, diacritical marks, and handles common Arabic clitics (prefixes such as و, ف, ب, ك, ل, ال).

- **Interactive Interface**  
  Built with [Streamlit](https://streamlit.io), allowing easy input and live processing results.

---

## Current Challenges

- Handling letters with *shadda* (ّ) currently causes incorrect tokenization, often splitting words where they should remain intact.  
- To mitigate this, clitics are temporarily kept attached to the words they follow to avoid erroneous splits.  
- Further improvements are planned to correctly handle *shadda* and improve tokenization accuracy.
- Initially camel tools library was used for tokenization, but there were some compatibility issues with certain modules from the library.

---

## Installation


1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/AraNormTokenizer.git
   cd AraNormTokenizer

  
2. Install requirements
  ```bash 
  pip install -r requirements.txt  

3. Run program
  ```bash 
  streamlit run app.py

