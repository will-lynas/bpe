from collections import defaultdict 

class BasicTokenizer:
    def __init__(self):
        self.to_pairs = {}
        self.from_pairs = {}
    
    def encode_text(self, text):
        return [int(byte) for byte in text.encode("utf-8")]
    
    def decode_text(self, tokens):
        return bytes(tokens).decode("utf-8")
        
    @staticmethod
    def pair_counts(text):
        pairs = defaultdict(int)
        for pair in zip(text, text[1:]):
            pairs[pair] += 1
        return pairs
    
    @staticmethod
    def most_common_pair(text):
        pairs = BasicTokenizer.pair_counts(text)
        print(pairs)
        return max(pairs, key=pairs.get)
    
    @staticmethod
    def merge(tokens, pair, token):
        new_tokens = []
        i = 0
        while i < len(tokens):
            if i < len(tokens) - 1 and tokens[i] == pair[0] and tokens[i + 1] == pair[1]:
                new_tokens.append(token)
                i += 2
            else:
                new_tokens.append(tokens[i])
                i += 1
        return new_tokens
        
    def train(self, text, vocab_size=10_000, verbose=False):
        tokens = self.encode_text(text)
        num_merges = vocab_size - 256
        for i in range(num_merges):
            pair = BasicTokenizer.most_common_pair(tokens)
            token = 256 + i
            if verbose:
                print(f"Merging {pair[0], pair[1]} into {token}")
            tokens = BasicTokenizer.merge(tokens, pair, token)
            self.to_pairs[token] = pair
            self.from_pairs[pair] = token