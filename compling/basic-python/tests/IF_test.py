import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import IF

def test0():

    assert not IF.checkWordLength('figaro')

    assert not IF.checkWordLength('abkljklkJ')

    assert IF.checkWordLength('Massachusetts')
