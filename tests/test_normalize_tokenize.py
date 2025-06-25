import pytest
from pathlib import Path
import sys
import os

#Make sure the app's directory is included in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from normalize import normalize_arabic
from tokenize_text import tokenize_arabic

#Test basic normalization on a Quranic phrase with diacritics
def test_normalization_basic():
    raw_text = "قُلۡ مَن يُنَجِّيكُم مِّن ظُلُمَٰتِ ٱلۡبَرِّ"
    expected = "قل من ينجيكم من ظلمات البر"
    assert normalize_arabic(raw_text) == expected

#Test tokenization on a normalized Arabic sentence
def test_tokenization_basic():
    normalized_text = "قل من ينجيكم من ظلمات البر"
    expected = ['قل', 'من', 'ينجيكم', 'من', 'ظلمات', 'البر']
    assert tokenize_arabic(normalized_text) == expected

#Test for clitic splitting (e.g., و, ب, ال) — expected to fail until clitic handling is fully implemented
def test_tokenization_clitics():
    text = "وبالبحر"
    expected = ['و', 'ب', 'البحر']  
    assert tokenize_arabic(text) == expected

#Test that all sample files in the sample_text/ directory normalize properly
def test_sample_file_normalization():
    sample_path = Path('sample_text')
    if not sample_path.exists():
        pytest.skip("Sample data folder not found.")
    
    txt_files = list(sample_path.glob('*.txt'))
    if not txt_files:
        pytest.skip("No .txt sample files found in sample_text folder.")
    
    for sample_file in txt_files:
        raw_text = sample_file.read_text(encoding='utf-8')
        normalized = normalize_arabic(raw_text)
        assert isinstance(normalized, str)
        assert len(normalized) > 0

#Test that tokenization produces valid lists of strings for each sample file
def test_sample_file_tokenization():
    sample_path = Path('sample_text')
    if not sample_path.exists():
        pytest.skip("Sample data folder not found.")
    
    txt_files = list(sample_path.glob('*.txt'))
    if not txt_files:
        pytest.skip("No .txt sample files found in sample_text folder.")
    
    for sample_file in txt_files:
        raw_text = sample_file.read_text(encoding='utf-8')
        tokens = tokenize_arabic(raw_text)
        assert isinstance(tokens, list), f"Tokens from {sample_file} is not a list"
        assert all(isinstance(token, str) for token in tokens), f"Not all tokens are strings in {sample_file}"
        assert len(tokens) > 0, f"No tokens produced from {sample_file}"
