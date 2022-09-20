import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import loops

def test():

    words = ['colorless', 'green', 'ideas', 'sleep', 'furiously']

    assert loops.sentPosition(words) == [(0, 'colorless'), (1, 'green'), (2, 'ideas'), (3, 'sleep'), (4, 'furiously')] 
