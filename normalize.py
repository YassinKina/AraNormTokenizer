import re

def normalize_arabic(text: str) -> str:
    """
    Normalize Arabic text by removing diacritics, standardizing characters, and cleaning punctuation.

    This function performs the following steps:
    - Removes Quranic diacritics and vowel marks (tashkeel)
    - Replaces alif variants (e.g., أ, إ, آ) and alif wasl (ٱ) with a standard alif (ا)
    - Converts taa marbuta (ة) to ha (ه)
    - Removes tatweel (ـ) used for elongation in writing
    - Removes non-Arabic characters, digits, and punctuation
    - Converts text to lowercase and strips extra whitespace

    Args:
        text (str): Raw Arabic input text.

    Returns:
        str: Cleaned and normalized Arabic text.
    """

    #Remove all tashkeel and Quranic marks
    diacritics_quranic = re.compile(
        r'[\u0610-\u061A\u064B-\u065F\u06D6-\u06DC\u06DF-\u06E8\u06EA-\u06ED\u06EE-\u06EF]'
    )
    text = diacritics_quranic.sub('', text)

    #Remove alif wasl (ٱ U+0671) and superscript alif (ٰ U+0670)
    text = re.sub(r'[\u0670\u0671]', 'ا', text)

    #Normalize alifs
    text = re.sub(r'[إأآا]', 'ا', text)

    #Normalize taa marbuta
    text = re.sub(r'ة', 'ه', text)

    #Remove tatweel
    text = re.sub(r'ـ', '', text)

    #Remove non-arabic letters, digits, punctuation 
    text = re.sub(r'[^\u0600-\u06FF\s]', '', text)

    text = text.lower()

    text = ' '.join(text.split())

    return text
