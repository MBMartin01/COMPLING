import os, sys
import torch
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tokenizer as T
import subprocess

def testEncode():

    word2idx = {'is': 0, 'the': 1, 'man': 2, 'who': 3, 'tall':4, 'happy':5, 
                    '?': 6, '<eos>': 7, '<unk>': 8, '<mask>': 9, '<pad>': 10}
    idx2word = ['is', 'the', 'man', 'who', 'tall', 'happy', '?', 
                    '<eos>', '<unk>', '<mask>', '<pad>']

    tokenizer = T.Tokenizer(maxSequenceLength=10)
    tokenizer.word2idx = word2idx
    tokenizer.idx2word = idx2word

    try:
        tokenizer.encode("the")
    except NotImplementedError:
        assert 0, "You need to implement the encode function"

    assert tokenizer.encode('<unk>') == [8], "Simple check failed"

    text = 'Is the man tall?'
    assert tokenizer.encode(text, add_special_tokens=True) == [7, 0, 1, 2, 4, 6, 7], "Checking add_special_tokens=True failed"

    text = ['Is the man tall?', 'Or is the man who is tall tall?']
    studentTensor = tokenizer.encode(text, padding=True, return_tensors='pt')
    goldTensor = torch.tensor([[0, 1, 2, 4, 6, 10, 10, 10, 10], [8, 0, 1, 2, 3, 0, 4, 4, 6]])
    assert torch.equal(studentTensor, goldTensor), "Checking padding=True and return_tensors='pt' failed"

    text = 'Is the man who is tall also quite tall though?'
    assert tokenizer.encode(text, truncate=True, add_special_tokens=True) == [7, 0, 1, 2, 3, 0, 4, 8, 8, 7], "Checking truncate=True (with maxSequenceLength as 10) and add_special_tokens=True failed"
