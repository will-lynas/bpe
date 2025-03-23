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