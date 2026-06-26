import time
from bs4 import BeautifulSoup as bs
import requests

NUM_OF_PAGES = 2
WAIT_TIME = 35
MIN_SCORE = 500

page_num = 1
news_to_read = []


def get_soup(page_num: int):
    url = f"https://news.ycombinator.com/?p={page_num}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url=url, headers=headers)
    return bs(response.text, "lxml")


def get_news(page_soup):
    page_news = []
    all_news = page_soup.select(".titleline")
    subtexts = page_soup.select(".subtext")
    for news, subtext in zip(all_news, subtexts):
        a = news.select_one("a")
        news_text = a.getText()
        news_link = a.get("href", None)
        score_element = subtext.select_one(".score")
        if score_element:
            # only if score is mentioned in subText:
            score = int(score_element.getText().replace(" points", ""))
            if score > MIN_SCORE:
                page_news.append({"text": news_text, "link": news_link, "score": score})
    return page_news


def sort_news(news_to_read: list) -> None:
    news_to_read.sort(key=lambda k: k["score"], reverse=True)


def print_news(news_to_read: list):
    for news in news_to_read:
        print(
            f"News : {news["text"]}\nLink to read more: {news["link"]}\nScore: {news["score"]}"
        )
        print("----------------------------")


while page_num <= NUM_OF_PAGES:
    if page_num > 1:
        time.sleep(WAIT_TIME)
    page_soup = get_soup(page_num)
    page_news = get_news(page_soup)
    news_to_read.extend(page_news)
    page_num += 1

sort_news(news_to_read)
print(len(news_to_read))
print_news(news_to_read)
