from collections import defaultdict

def encode_text(text):
    return [int(byte) for byte in text.encode("utf-8")]

def decode_text(tokens):
    return bytes(tokens).decode("utf-8")
    
def pair_counts(text):
    pairs = defaultdict(int)
    for pair in zip(text, text[1:]):
        pairs[pair] += 1
    return pairs

def most_common_pair(text):
    pairs = pair_counts(text)
    return max(pairs, key=pairs.get)

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