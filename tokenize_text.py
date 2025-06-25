def tokenize_arabic(text):
    """
    Tokenize Arabic text using Camel Tools' simple word tokenizer.

    This function splits Arabic text into tokens (words) using the 
    `simple_word_tokenize` method from the Camel Tools library.

    Args:
        text (str): Arabic text to tokenize.

    Returns:
        list[str]: A list of tokenized words.
    """
    from camel_tools.tokenizers.word import simple_word_tokenize
    return simple_word_tokenize(text)
