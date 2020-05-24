import sys, os
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__) + '/../'))

from packages.twitter_scrapper import TwitterScrapper

def test_scrapper():
    keywords = ['machine learning', 'software developer']
    tscrapper = TwitterScrapper()
    assert len(tscrapper.scrape(keywords)) > 0