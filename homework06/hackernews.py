from bottle import (
    route, run, template, request, redirect
)

from scruputils import get_news
from db import News, session
from bayas import NaiveBayesClassifier
import string


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    id = request.query['id']
    label = request.query['label']
    s = session()
    line = s.query(News).filter(News.id == id).first()
    line.label = label
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    abc = get_news('https://news.ycombinator.com/newest')
    s = session()
    for g in abc:
        title = g['title']
        author = g['author']
        rows = s.query(News).filter(News.title == title).filter(News.author == author).first()
        if rows is None:
            new = News(title = g['title'],author = g['author'], url = g['urls'], comments = g['comments'], points = g['score'])
            s.add(new)
            s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    bs = NaiveBayesClassifier(1)
    s = session()
    nolable = s.query(News).filter(News.label == None).all()
    X = processing(nolable)
    X_train = s.query(News).filter(News.label != None).all()
    y = []
    for item in X_train:
        y.append(item.label)
    X_train = processing(X_train)
    bs.fit(X_train, y)
    predictions = bs.predict(X)
    counter = 0
    for item in nolable:
        item.label = predictions[counter]
        counter += 1
    nolable.sort(key=lambda x: x.label)
    nolable.reverse()
    return template('news_template', rows=nolable)
    pass


def processing(data):
    titles = []
    translator = str.maketrans("", "", string.punctuation)
    for record in data:
        titles.append(record.title)
    prossessed_titles = []
    for title in titles:
        title.translate(translator)
        title = title.lower()
        title = title.split()
        prossessed_titles.append(title)
    #print(prossessed_titles)
    return prossessed_titles


if __name__ == "__main__":
    run(host="localhost", port=8080)