import os, sys
import torch
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tokenizer as T
import subprocess

def testSaveTokenizer():
    tokenizer = T.Tokenizer()
    tokenizer.idx2word = ['the', 'frog', 'hates', 'shells']
    tokenizer.word2idx = {'the': 0, 
                            'frog': 1, 
                            'hates': 2, 
                            'shells': 3}

    tempfname = "./tests/temp"
    if os.path.exists(tempfname):
        subprocess.run(["rm", tempfname])

    try:
        tokenizer.save_tokenizer(tempfname)
    except NotImplementedError:
        assert 0, "You need to implement the save_tokenizer function"

    assert os.path.exists(tempfname), "You are not saving your tokenizer to the argument fname"

    with open(tempfname, 'r') as f:
        studentLines = f.readlines()

    assert studentLines == ['the\n', 'frog\n', 'hates\n', 'shells\n'], "The output format of your save_tokenizer function is incorrect."
