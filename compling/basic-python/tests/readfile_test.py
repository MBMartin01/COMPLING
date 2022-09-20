import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import readfile
import subprocess

def test():

    subprocess.run(["bash", "./tests/read.sh"])

    with open('./tests/temp', 'r') as f:

        lines = f.readlines()

    subprocess.run(["rm", "./tests/temp"])
    assert lines == ['Alice was beginning to get very tired of sitting by her sister\n', 'on the bank, and of having nothing to do:  once or twice she had\n', 'peeped into the book her sister was reading, but it had no\n', "pictures or conversations in it, `and what is the use of a book,'\n", "thought Alice `without pictures or conversation?'\n"]



#test()
