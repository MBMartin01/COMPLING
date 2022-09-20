import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import add 

def test0():

    a = 100.0
    b = 200.1

    assert add.Add(a,b) == 300.1
