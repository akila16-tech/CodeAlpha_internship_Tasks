import pandas as pd

url = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv"

df = pd.read_csv(url)

df.head()
df.shape
df.columns
df.info()
df.isnull().sum()
df.describe()
df.sort_values("average_rating", ascending=False)[["title","average_rating"]].head()
df.sort_values("ratings_count", ascending=False)[["title","ratings_count"]].head()
top10 = df.sort_values("average_rating", ascending=False).head(10)
top10[["title","average_rating"]]

import matplotlib.pyplot as plt

top10 = df.nlargest(10, 'ratings_count')

plt.figure(figsize=(10,5))
plt.bar(top10['title'], top10['ratings_count'])
plt.xticks(rotation=90)
plt.title("Top 10 Most Reviewed Books")
plt.show()

plt.hist(df['average_rating'], bins=20)
plt.title("Average Rating Distribution")
plt.show()
