from bs4 import BeautifulSoup, SoupStrainer
from billiard.pool import Pool
from itertools import cycle

from packages.scrapper import helper
import datetime as dt
import numpy as np
import logging
import requests
import urllib
import random
import json
import re


class TwitterScrapper:
    """ Scrap data from twitter without using API. 
    """

    def __init__(self, limit=50):
        self.limit = limit
        self.proxies = helper.get_proxies()
        self.proxy_pool = cycle(self.proxies)

    def query_page(self, query, pos, retry=5, timeout=60):
        """Sends request to twitter server to fetch the page data.        
        
        parameters:
            query (str): Query to search for the tweets.
            pos (str): Position is used for pagination
            retry (int): Number of times to retry when no data is received
            timeout (float): number of seconds to wait before timeout
            
        Returns:
            new-tweets, min_position (tuple): list of tweets per page, position
        """
        url = helper.get_query_url(query, pos)
        logging.info("Scraping tweets from {}".format(url))

        try:
            proxy = next(self.proxy_pool)
            logging.info("Using proxy {}".format(proxy))

            if pos is None:
                response = requests.get(
                    url, headers=helper.HEADER, proxies={"http": proxy}, timeout=timeout
                ).text
                html = response.encode("utf8")
                min_position = helper.find_value(response, "data-min-position")
            else:
                response = requests.get(
                    url.format(max_position=pos),
                    headers=helper.HEADER,
                    proxies={"http": proxy},
                    timeout=timeout,
                ).text
                try:
                    response_dict = json.loads(response)
                    min_position = response_dict["min_position"]
                    html = response_dict["items_html"].encode("utf8")
                except ValueError as e:
                    logging.exception(
                        'Failed to parse JSON "{}" while requesting "{}"'.format(e, url)
                    )

            tweets = list(helper.from_html(html))

            if not tweets:
                if retry > 0:
                    logging.info("Retrying... (Attempts left: {})".format(retry))
                    return self.query_page(query, min_position, retry - 1)
                else:
                    return [], min_position

            return tweets, min_position

        except BaseException as e:
            logging.exception('HTTPError {} while requesting "{}"'.format(e, url))

    def get_tweets_per_page(self, query):
        """Gets tweets from multiple pages.        
        
        parameters:
            query (str): Query to search for the tweets.

        Returns:
            new-tweets (list): list of tweets per page.
        """
        d = {" ": "%20", "#": "%23", ":": "%3A", "&": "%26"}
        for i, item in d.items():
            query = query.replace(i, item)

        num_tweets = 0
        pos = None
        try:
            while True:
                new_tweets, pos = self.query_page(query, pos)
                if len(new_tweets) == 0:
                    logging.info("Got {} tweets for {}.".format(num_tweets, query))
                    return

                yield new_tweets

                num_tweets += len(new_tweets)
                if num_tweets >= self.limit:
                    logging.info("Got {} tweets for {}.".format(num_tweets, query))
                    return
        except BaseException:
            logging.exception(
                "An unknown error occurred! Returning tweets gathered so far."
            )
        logging.info("Got {} tweets for {}.".format(num_tweets, query))

    def get_tweets(self, *args):
        """Returns tweets for the query passed as the argument       
        """
        tweets = list(self.get_tweets_per_page(*args))
        return tweets if tweets else []

    def scrape(self, keywords):
        all_tweets = []
        pool_size = 20

        start_date = dt.date.today() - dt.timedelta(14)
        query = " ".join(keywords)

        no_of_days = (dt.date.today() - start_date).days
        if no_of_days < pool_size:
            pool_size = no_of_days

        date_ranges = [
            start_date + dt.timedelta(days=elem)
            for elem in np.linspace(0, no_of_days, pool_size + 1)
        ]

        if self.limit and pool_size:
            self.limit = (self.limit // pool_size) + 1

        queries = [
            "{} since:{} until:{}".format(query, since, until)
            for since, until in zip(date_ranges[:-1], date_ranges[1:])
        ]

        pool = Pool(pool_size)
        logging.info("queries: {}".format(queries))

        try:
            for new_tweets in pool.imap_unordered(self.get_tweets, queries):
                all_tweets.extend(new_tweets)
        except KeyboardInterrupt:
            logging.info(
                "Program interrupted by user. Returning all tweets " "gathered so far."
            )
        finally:
            pool.close()
            pool.join()

        return all_tweets
        

if __name__ == "__main__":
    
    print(
        "Type comma separated keywords to search jobs (E.g, machine learning,software developer):"
    )
    keywords = input().strip().split(",")
    tapi = TwitterScrapper()
    print(tapi.scrape(keywords))

    
