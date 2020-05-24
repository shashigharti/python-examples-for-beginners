from bs4 import BeautifulSoup, SoupStrainer
import requests

PROXY_URL = "https://free-proxy-list.net/"
URL = "https://twitter.com/search?f=tweets&vertical=default&q={q}"
RELOAD_URL = (
    "https://twitter.com/i/search/timeline?f=tweets&q={q}&max_position={max_position}"
)
HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 Edge/12.0"
}


def get_proxies():
    """Get proxy lists to connect to twitter server to fetch data      
    """
    response = requests.get(PROXY_URL, headers=HEADER, timeout=10).text
    soup = BeautifulSoup(response, "lxml")
    table = soup.find("table", id="proxylisttable")
    list_tr = table.find_all("tr")
    list_td = [elem.find_all("td") for elem in list_tr]
    list_td = list(filter(None, list_td))
    list_ip = [elem[0].text for elem in list_td]
    list_ports = [elem[1].text for elem in list_td]
    list_proxies = [":".join(elem) for elem in list(zip(list_ip, list_ports))]

    return list_proxies


def has_class(class_name):
    return lambda class_: class_ and class_name in class_.split()


only_tweet_tags = SoupStrainer(
    "div", class_=has_class("tweet"), **{"data-tweet-id": True}
)


def from_html(html):
    """Initiate beautifulsoup class to parse html and read tweet data
    """
    tweets = BeautifulSoup(html, "html.parser", parse_only=only_tweet_tags)
    for tweet in tweets:
        yield parse(tweet)


def parse(html):
    """Parse tweet data from html   
    """
    permalink = html["data-permalink-path"]
    screen_name = html["data-screen-name"]
    name = html["data-name"]
    content_div = html.find("div", class_=has_class("content"))
    tweet_body_tag = content_div.find("p", class_=has_class("tweet-text"))
    tweet_text = tweet_body_tag.text

    urls = [
        a["data-expanded-url"]
        for a in tweet_body_tag.find_all("a", class_=has_class("twitter-timeline-link"))
        if "data-expanded-url" in a.attrs
    ]

    timestamp = int(content_div.find(**{"data-time-ms": True})["data-time-ms"]) / 1000.0
    footer_div = content_div.find("div", class_=has_class("stream-item-footer"))
    footer_div.find("span", class_="ProfileTweet-action--retweet")

    tweet = dict(
        permalink=permalink,
        screen_name=screen_name,
        name=name,
        tweet_text=tweet_text,
        urls=urls,
        timestamp=timestamp,
    )
    return tweet


def get_query_url(query, pos):
    """Helper function to switch query url        
    """
    return (
        URL.format(q=query)
        if pos is None
        else RELOAD_URL.format(q=query, max_position=pos)
    )


def find_value(html, key):
    pos_begin = html.find(key) + len(key) + 2
    pos_end = html.find('"', pos_begin)
    return html[pos_begin:pos_end]

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
        print(i.ljust(len(i) + 4), end="")

    print("")
    for row in rows:
        for index, col in enumerate(row):
            header_length = len(headers[index]) + 4
            r_offset = header_length - len(col)
            print(col, end=" " * r_offset)
        print("")
