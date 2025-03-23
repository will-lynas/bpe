from bpe.basic import BasicTokenizer

def test_basic():
    tokenizer = BasicTokenizer()
    text = "hello world"
    tokenizer.train(text, vocab_size=256 + 5)