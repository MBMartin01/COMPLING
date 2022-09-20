import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import counts
import json

def test():
    fname = 'alice.txt'

    with open('./tests/goldalice.json') as f:
        goldCounts = json.load(f)

    studentCounts = counts.getCounts(fname)
    assert type(studentCounts) == dict, f"Returning {studentCounts} which is of type {type(studentCounts)} not dict"

    for key in goldCounts:
        if key == "":
            continue
        assert key in studentCounts, f"Missing the word '{key}'"
        goldValue = goldCounts[key]
        studentValue = studentCounts[key]
        assert goldValue == studentValue, f"For the word '{key}' the count should be {goldValue} not {studentValue}"
