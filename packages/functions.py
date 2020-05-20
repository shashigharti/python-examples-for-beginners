# !/usr/bin/env python3
""" Exploring exponential function: Generate and visualize exponential functions.

    ----------------------------------------------------------------------------
    This module contains functions that generates various values for different 
    exponential functions and plots it to the graph.
    ----------------------------------------------------------------------------
"""

# import libraries
import math
import matplotlib.pyplot as plt


def generate(f, rng=[1, 50]):
    """ Generate x data points using range param and return y values.

    Parameters:
        f (function): function to apply.
        rng (list): range to generate x values.
    
    Returns:
        x (list): all x values.
        y (list): list of y values output from function 'f' applied to each x.
    """

    y = []
    r_iterator = range(*rng)
    for i in r_iterator:
        y.append(f(x=i))
    x = list(r_iterator)

    return x, y


def plot_graph(x, y, label_x, label_y, title):
    """ Plot the graph for given x, y values.

    Parameters:
        x (list): List of x co-ordinates.
        y (list): List of y co-ordinates for each x value.
        label_x (str): Label for x axis.
        label_y (str): Label for y axis
        title (str): Title string of the graph
    
    Returns:
        None
    """

    plt.figure()
    plt.plot(x, y)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.title(title)
