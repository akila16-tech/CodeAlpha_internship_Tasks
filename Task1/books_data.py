from google.colab import files
import pandas as pd

url = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv"

df = pd.read_csv(url)

print(df.head())

df.to_excel("Books_Data.xlsx", index=False)

print("Excel file created successfully!")

files.download("Books_Data.xlsx")
