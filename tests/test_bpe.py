import pytest

from tests.utils import test_strings, unpack

from bpe import BasicTokenizer

def test_basic():
    tokenizer = BasicTokenizer()
    text = "hello world"
    tokenizer.train(text, vocab_size=256 + 5)
    
@pytest.mark.parametrize("text", test_strings)
def test_encode_decode_identity(text):
    text = unpack(text)
    tokenizer = BasicTokenizer()
    encoded = tokenizer.encode(text)
    decoded = tokenizer.decode(encoded)
    assert decoded == text