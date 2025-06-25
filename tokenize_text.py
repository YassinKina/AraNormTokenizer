import re

# Common Arabic clitics in order of processing
CLITIC_PREFIXES = ['ال', 'و', 'ف', 'ب', 'ك', 'ل']

def tokenize_arabic(text):
    """
    Tokenize Arabic text and segment common clitics (e.g. و, ف, ب, ك, ل, ال).

    This function uses regex to extract Arabic words and then splits clitics
    from the beginning of each word.

    Args:
        text (str): Arabic text.

    Returns:
        list[str]: List of tokens with clitics separated.
    """
    #Extract Arabic words
    words = re.findall(r'[\u0600-\u06FF]+', text)

    tokens = []
    for word in words:
        # original = word  #Save for debugging
        prefixes = []

        # Iteratively strip clitic prefixes
        while True:
            for clitic in CLITIC_PREFIXES:
                if word.startswith(clitic) and len(word) > len(clitic):
                    prefixes.append(clitic)
                    word = word[len(clitic):]
                    break
            else:
                break  #No more clitics

        tokens.extend(prefixes)
        tokens.append(word)

    return tokens
