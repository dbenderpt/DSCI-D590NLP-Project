
from tester import analyzeSentiment, articles
import pandas as pd

data = pd.read_csv("articles.csv", encoding="ISO-8859-1")


articleText = data["text"]
print(type(articleText))
articleText = list(articleText)

#cleaning!
data["date"] = pd.to_datetime(data["date"], format="%m/%d/%y")


print(data['date'].dtype)

data['quarter'] = data['date'].dt.to_period('Q')

splitQuarters = {
    str(quarter): group["text"].tolist()
    for quarter, group in data.groupby('quarter')
}

print(splitQuarters)
