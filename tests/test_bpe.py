import pytest

from tests.utils import test_strings, unpack

from bpe import BasicTokenizer

@pytest.mark.parametrize("tokenizer_factory", [BasicTokenizer])
@pytest.mark.parametrize("text", test_strings)
def test_train_works(tokenizer_factory, text):
    tokenizer = tokenizer_factory()
    tokenizer.train(text, vocab_size=256 + 5, verbose=True)
    
@pytest.mark.parametrize("tokenizer_factory", [BasicTokenizer])
@pytest.mark.parametrize("text", test_strings)
def test_encode_decode_identity(tokenizer_factory, text):
    text = unpack(text)
    tokenizer = tokenizer_factory()
    encoded = tokenizer.encode(text)
    decoded = tokenizer.decode(encoded)
    assert decoded == text
    
@pytest.mark.parametrize("tokenizer_factory", [BasicTokenizer])
def wikipedia_example(tokenizer_factory):
    """
    https://en.wikipedia.org/wiki/Byte_pair_encoding

    Input string is "aaabdaaabac"
    After 3 merges, the string will be "XdXac"
    Where X=ZY Y=ab Z=aa

    In ascii, a=97, b=98, c=99, d=100
    Then the new tokens will be Z=256, Y=257, X=258 (nb these are not their literal ascii values)

    Output should be [258, 100, 258, 97, 99]
    """
    tokenizer = tokenizer_factory()
    text = "aaabdaaabac"
    num_merges = 3
    tokenizer.train(text, vocab_size=256 + num_merges, verbose=True)
    encoded = tokenizer.encode(text)
    assert encoded == [258, 100, 258, 97, 99]
    decoded = tokenizer.decode(encoded)
    assert decoded == text