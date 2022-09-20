import os, sys
import torch
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tokenizer as T
import subprocess

def testDecode():

    word2idx = {'is': 0, 'the': 1, 'man': 2, 'who': 3, 'tall':4, 'happy':5, 
                    '?': 6, '<eos>': 7, '<unk>': 8, '<mask>': 9, '<pad>': 10}
    idx2word = ['is', 'the', 'man', 'who', 'tall', 'happy', '?', 
                    '<eos>', '<unk>', '<mask>', '<pad>']

    tokenizer = T.Tokenizer(maxSequenceLength=10)
    tokenizer.word2idx = word2idx
    tokenizer.idx2word = idx2word

    try:
        tokenizer.decode([0])
    except NotImplementedError:
        assert 0, "You need to implement the decode function"

    ids = [3, 0, 4, 6]
    assert tokenizer.decode(ids) == ['who', 'is', 'tall', '?']

    ids = [[1, 2], [0, 6]]
    assert tokenizer.decode(ids) == [['the', 'man'], ['is', '?']]

    ids = torch.tensor([[1, 8, 0, 8], [0, 9, 10, 10]])
    assert tokenizer.decode(ids) == [['the', '<unk>', 'is', '<unk>'], ['is', '<mask>', '<pad>', '<pad>']]

