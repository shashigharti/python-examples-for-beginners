# !/usr/bin/env python3
""" Exploring binomial distribution: Generate and visualize probabilities.

    ----------------------------------------------------------------------------
    This module contains functions to generate events, calculate probability
    and visualize.
    ----------------------------------------------------------------------------
"""
# import libraries
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def generate_events(number_of_observations=10, reviews_per_observation=10):
    """ Generates events of size equal to 'number_of_observations'. 
    
    Parameters:
        number_of_observations (int): Total number of experiments or observations
        reviews_per_observation (int): Total reviews per experiment. For e.g, 10 reviews per
        experiment.
    
    Returns:
        events (list): 1D array of size equal to 'reviews_per_observation' params with cells
        set a 1's for positive reviews. Random number < .95 represent is assumed to be
        positive review.
    """
    events = []
    for _ in range(number_of_observations):
        outcomes = []
        for _ in range(reviews_per_observation):
            rnd_number = random.random()
            outcomes.append(1) if rnd_number < 0.95 else outcomes.append(0)

        events.append(outcomes)

    return events


def get_metrics(events, reviews_per_observation=10, positive_reviews=8):
    """ Calculate probability of getting given number of positive reviews i.e, 'positive_reviews'.
    
    Parameters:
        events (list): 2D array with events as row and outcomes as column.
        reviews_per_observation (int): Total reviews per experiment or observation. For e.g, 10 reviews per
        experiment.
        positive_reviews (int): Target event for which the probability is to be calculated.
    
    Returns:
        rows (list): 1D array containing information of the experiment and probability of 
        target event.
    """

    number_of_events = len(events)
    events_freq_count = {i: 0 for i in range(reviews_per_observation + 1)}

    # count positive reviews for each event. 1 represent the positive review
    for event in events:
        count = event.count(1)
        events_freq_count[count] += 1

    positive_review_per = events_freq_count[positive_reviews] / number_of_events

    rows = [
        "%d" % number_of_events,
        "%d" % reviews_per_observation,
        "%d" % positive_reviews,
        "{:.2%}".format(positive_review_per),
    ]

    return rows


def display_table(data):
    """ Displays data in table format.
    
    Parameters:
        data (tuple): It is a tuple with headers and rows.
    
    Returns:
        None
    """
    headers = data[0]
    rows = data[1]

    for i in headers:
        print(i.ljust(len(i) + 10), end="")

    print("")
    for row in rows:
        for index, col in enumerate(row):
            header_length = len(headers[index]) + 10
            r_offset = header_length - len(col)
            print(col, end=" " * r_offset)
        print("")


def plot_hist(observations, reviews_per_observation,  positive_reviews):
    """ Plots histogram.
    
    Parameters:
        observations (list): 2D list with the outcomes of all the experiments
        reviews_per_observation (int): Total reviews per experiment or observation. For e.g, 10 reviews per
        experiment.
    
    Returns:
        None 
    """
    freq_hist_of_outcomes = []
    for events in observations:
        freq_hist_of_outcomes.append([event.count(1) for event in events])

    # Display plots in 3 columns
    plot_rows = (len(freq_hist_of_outcomes) // 3) + 1
    fig, axes = plt.subplots(nrows=plot_rows, ncols=3, figsize=(20, 20))
    fig.subplots_adjust(hspace=0.5)

    for ax, freq_lst in zip(axes.ravel(), freq_hist_of_outcomes):
        _, _, patches = ax.hist(
            freq_lst,
            bins=[i for i in range(1, reviews_per_observation + 1)],
            edgecolor="black",
            linewidth=1.2,
            density=True
        )
        for thispatch in patches: 
            xy = thispatch.xy
            if (xy[0] == positive_reviews):
                thispatch.set_facecolor('r')

        ax.set_title("%s Observations" % (len(freq_lst)))
        ax.set_xlabel(
            "No of positive reviews out of %d reviews" % (reviews_per_observation)
        )
        ax.set_ylabel("Percentage")
        ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
