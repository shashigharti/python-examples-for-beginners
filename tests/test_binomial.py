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


def test_get_metrics():
    events = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 1]]
    reviews_per_observation, positive_reviews = 10, 8
    assert  binomial_distribution.get_metrics(events, reviews_per_observation, positive_reviews) == ['10', '10', '8', '10.00%']