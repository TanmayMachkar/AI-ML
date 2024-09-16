import pandas as pd

df = pd.read_csv(r"C:\Users\ADMIN\AI-ML\Pandas\movies.csv", index_col = "release_year") #set index as 'release year'

print(df["imdb_rating"].median())
print(df.describe())
print(df["imdb_rating"].count())
print(df["industry"].value_counts())