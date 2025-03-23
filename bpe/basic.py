from collections import defaultdict 

from .common import encode_text, most_common_pair, merge, decode_text

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
            
    def encode(self, text):
        """
        string -> list of ints
        """
        tokens = encode_text(text)
        if len(tokens) < 2:
            return tokens
        out = []
        out.append(tokens[0])
        i = 1
        while i < len(tokens):
            pair = (out[-1], tokens[i])
            if pair in self.to_pairs:
                out.pop()
                out.append(self.from_pairs[pair])
            else:
                out.append(tokens[i])
            i += 1
        return out
    
    def decode(self, tokens):
        """
        list of ints -> string
        """
        def inner(tokens):
            out = []
            for token in tokens:
                if token < 256:
                    out.append(token)
                else:
                    out.extend(inner(self.to_pairs[token]))
            return out
        return decode_text(inner(tokens))