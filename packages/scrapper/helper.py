from bs4 import BeautifulSoup, SoupStrainer
import requests

PROXY_URL = "https://free-proxy-list.net/"
URL = "https://twitter.com/search?f=tweets&vertical=default&q={q}"
RELOAD_URL = "https://twitter.com/i/search/timeline?f=tweets&q={q}&vertical=default&include_available_features=1&include_entities=1&max_position={max_position}"

def has_class(class_name):
    return lambda class_: class_ and class_name in class_.split()

only_tweet_tags = SoupStrainer(
    "div", class_=has_class("tweet"), **{"data-tweet-id": True}
)

def from_html(html):
    tweets = BeautifulSoup(html, "html.parser", parse_only=only_tweet_tags)
    for tweet in tweets:
        try:
            yield parse(tweet)
        except BaseException:
            pass

def parse(html):
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


def find_value(html, key):
    pos_begin = html.find(key) + len(key) + 2
    pos_end = html.find('"', pos_begin)
    return html[pos_begin:pos_end]


def get_query_url(query, pos):
    return (
        URL.format(q=query)
        if pos is None
        else RELOAD_URL.format(q=query, max_position=pos)
    )


def get_proxies():
    response = requests.get(PROXY_URL)
    soup = BeautifulSoup(response.text, "lxml")
    table = soup.find("table", id="proxylisttable")
    list_tr = table.find_all("tr")
    list_td = [elem.find_all("td") for elem in list_tr]
    list_td = list(filter(None, list_td))
    list_ip = [elem[0].text for elem in list_td]
    list_ports = [elem[1].text for elem in list_td]
    list_proxies = [":".join(elem) for elem in list(zip(list_ip, list_ports))]

    return list_proxies
