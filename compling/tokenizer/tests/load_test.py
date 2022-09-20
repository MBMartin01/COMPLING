import os, sys
import torch
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tokenizer as T
import subprocess

def testLoadTokenizer():

    testfname = './tests/TestVocab.txt'
    gold_idx2word = ['is', 'the', 'man', 'who', 'tall', 'happy', '?', '<eos>', '<unk>', '<mask>', '<pad>'] 
    gold_word2idx = {'is': 0, 'the': 1, 'man': 2, 'who': 3, 'tall':4, 'happy':5, 
                    '?': 6, '<eos>': 7, '<unk>': 8, '<mask>': 9, '<pad>': 10}

    tokenizer = T.Tokenizer()

    try:
        tokenizer.load_tokenizer(testfname)
    except NotImplementedError:
        assert 0, "You need to implement the load_tokenizer function"

    assert tokenizer.idx2word == gold_idx2word, "You are not updating self.idx2word"

    assert tokenizer.word2idx == gold_word2idx, "You are not updating self.word2idx"
