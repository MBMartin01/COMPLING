import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import basicClass
import inspect

def test():

    names = list(map(lambda x: x[0], inspect.getmembers(basicClass)))
    assert 'Linguist' in names, "Missing the class Linguist"

    name = 'Chomsky'
    advisor = 'Harris'
    uni = 'Penn'

    try:
        ling = basicClass.Linguist(name, advisor)
    except:
        assert 1 == 0, 'Your class does not accept two arguments'

    assert hasattr(ling, 'name'), 'Missing the instance attribute name'
    assert hasattr(ling, 'advisor'), 'Missing the instance attribute advisor'

    assert ling.name == name
    assert ling.advisor == advisor

    assert hasattr(ling, 'addUniversity'), 'Missing the method addUniversity'

    try:
        ling.addUniversity(uni)
    except:
        assert 1 == 0, 'The class method addUniversity does not accept an argument'

    assert hasattr(ling, 'uni'), 'Missing the instance attribute uni'
    assert ling.uni == uni
