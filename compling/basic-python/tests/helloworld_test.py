import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import helloworld

def test0():
    assert helloworld.helloWorld() == "Hello World!"
