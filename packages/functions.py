# !/usr/bin/env python3
""" Exploring exponential function: Generate and visualize exponential functions

    ----------------------------------------------------------------------------
    This module contains files that generates various values for different 
    exponential functions and plots it to the graph
    ----------------------------------------------------------------------------
"""
# import libraries
import math

def generate(y, rng = [1, 50]):
    lst = []
    for i in range(*rng):
        lst.append(y(x=i))
    return lst


