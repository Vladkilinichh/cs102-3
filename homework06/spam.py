import csv
import string
from bayas import NaiveBayesClassifier


with open("SMS") as f:
        data = list(csv.reader(f, delimiter="\t"))
        len(data)


def clean(s):
        translator = str.maketrans("", "", string.punctuation)
        return s.translate(translator)
X, y = [], []
for target, msg in data:
        X.append(msg)
        y.append(target)
        X = [clean(x).lower() for x in X]


X_train, y_train, X_test, y_test = X[:3900], y[:3900], X[3900:], y[3900:]
model = NaiveBayesClassifier(1)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
# 0.9820574162679426
