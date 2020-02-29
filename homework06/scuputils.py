import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    titles = []
    authors = []
    urls = []
    coms = []
    scores = []
    mya = parser.find_all('a', class_='storylink')
    for a in mya:
        titles.append(a.contents[0])
    author = parser.find_all('a', class_='hnuser')
    for a in author:
        authors.append(a.contents[0])
    myurl = parser.find_all('a', class_='storylink')
    for a in myurl:
        urls.append(a['href'])
    comments = parser.find_all('td', class_='subtext')
    for td in comments:
        coms.append(td.find_all('a')[-1].contents[0])
    score = parser.find_all('span', class_='score')
    for span in score:
        scores.append(span.contents[0])
    for i in range(len(titles)):
        new = {}
        new['title'] = titles[i]
        new['author'] = authors[i]
        new['urls'] = urls[i]
        new['comments'] = coms[i]
        new['score'] = scores[i]
        news_list.append(new)
    return news_list


def extract_next_page(parser):
    """ Extract next page URL """
    more = parser.find('a', class_='morelink')
    return more['href']


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        print(news_list)
        next_page = extract_next_page(soup)
        url = 'https://news.ycombinator.com/' + next_page
        news.extend(news_list)
        n_pages -= 1
    return news
