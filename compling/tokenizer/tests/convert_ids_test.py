import os, sys
import torch
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tokenizer as T
import subprocess

def testConvertIDs2Tokens():

    word2idx = {'is': 0, 'the': 1, 'man': 2, 'who': 3, 'tall':4, 'happy':5, 
                    '?': 6, '<eos>': 7, '<unk>': 8, '<mask>': 9, '<pad>': 10}
    idx2word = ['is', 'the', 'man', 'who', 'tall', 'happy', '?', 
                    '<eos>', '<unk>', '<mask>', '<pad>']

    tokenizer = T.Tokenizer(maxSequenceLength=10)
    tokenizer.word2idx = word2idx
    tokenizer.idx2word = idx2word

    try:
        tokenizer.convert_ids_to_tokens(0)
    except NotImplementedError:
        assert 0, "You need to implement the convert_ids_to_tokens function"

    ids = 0
    assert tokenizer.convert_ids_to_tokens(ids) == "is"

    ids = [0, 1, 2, 8, 6]
    assert tokenizer.convert_ids_to_tokens(ids) == ['is', 'the', 'man', '<unk>', '?']
