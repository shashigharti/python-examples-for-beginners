import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest
import math
from packages import functions

def test_generate():
    y = lambda x: math.exp(x)
    assert len(functions.generate(y)) == 49
