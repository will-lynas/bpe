from collections import defaultdict 

from .common import encode_text, most_common_pair, merge

class BasicTokenizer:
    def __init__(self):
        self.to_pairs = {}
        self.from_pairs = {}
    
    def train(self, text, vocab_size=10_000, verbose=False):
        tokens = encode_text(text)
        num_merges = vocab_size - 256
        for i in range(num_merges):
            pair = most_common_pair(tokens)
            token = 256 + i
            if verbose:
                print(f"Merging {pair[0], pair[1]} into {token}")
            tokens = merge(tokens, pair, token)
            self.to_pairs[token] = pair
            self.from_pairs[pair] = token