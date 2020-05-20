# !/usr/bin/env python3
""" Exploring binomial distribution: Generate and visualize events.

    ----------------------------------------------------------------------------
    This module contains functions to generate random events and visualize as 
    histograms
    ----------------------------------------------------------------------------
"""
# import libraries
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def generate_events(number_of_observations=10, reviews_per_observation=10):
    """ Generates observations with random events
    
    Generates given number of observations and returns the list of observations

    Parameters:
        number_of_observations (list):
    
    Returns:
        observations (list): 2D array with rows as observations and columns as events
    """
    observations = []
    for _ in range(number_of_observations):
        events = []
        for _ in range(reviews_per_observation):
            rnd_number = random.random()
            events.append(1) if rnd_number < 0.95 else events.append(0)

        observations.append(events)

    return observations


def create_histogram(observations):
    histogram = []
    for observation in observations:
        count = observation.count(1)
        histogram.append(count)
    return histogram


def get_metrics(observations, reviews_per_observation=10, positive_reviews=8):
    number_of_observations = len(observations)
    observations_freq_count = {i: 0 for i in range(reviews_per_observation + 1)}

    for observation in observations:
        count = observation.count(1)
        observations_freq_count[count] += 1

    positive_review_per = (
        observations_freq_count[positive_reviews] / number_of_observations
    )

    rows = [
        "%d" % number_of_observations,
        "%d" % reviews_per_observation,
        "%d" % positive_reviews,
        "{:.2%}".format(positive_review_per),
    ]

    return rows


def display_table(table):
    headers = table[0]
    rows = table[1]

    for i in headers:
        print(i.ljust(len(i) + 10), end="")

    print("")
    for row in rows:
        for index, col in enumerate(row):
            header_length = len(headers[index]) + 10
            r_offset = header_length - len(col)
            print(col, end=" " * r_offset)
        print("")


# def imshow_pair(image_pair, titles=('', ''), figsize=(10, 5), **kwargs):
#     fig, axes = plt.subplots(ncols=2, figsize=figsize)
#     for ax, img, label in zip(axes.ravel(), image_pair, titles):
#         ax.imshow(img, **kwargs)
#         ax.set_title(label)


def plot_hist(observations, reviews_per_observation):
    freq_hist = []
    for observation in observations:
        freq_hist.append(create_histogram(observation))
    
    plot_rows = (len(freq_hist)//3) + 1
    fig, axes = plt.subplots(nrows=plot_rows, ncols=3, figsize=(20, 20))
    fig.subplots_adjust(hspace=0.5)

    for ax, hst in zip(axes.ravel(), freq_hist):
        ax.hist(
            hst,
            bins=[i for i in range(1, reviews_per_observation + 1)],
            edgecolor="black",
            linewidth=1.2,
            density=True,
        )
        ax.set_title("%s observations"%(len(hst)))
        ax.set_xlabel("No of positive reviews out of %d reviews"%(reviews_per_observation))
        ax.set_ylabel("Percentage")
        ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))

  
