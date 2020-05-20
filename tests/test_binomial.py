# import libraries
import sys, os
import unittest
import math

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../")

# import local packages
from packages import binomial_distribution

def test_generate_events():
    events = binomial_distribution.generate_events()
    assert len(events) == 10


