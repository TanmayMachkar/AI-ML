import pandas as pd

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["coreschafer@gmail.com", "JaneDoe@gmail.com", "JohnDoe@gmail.com"]
}

#data frame - rows and columns. Container for multiple series object
df = pd.DataFrame(people)
print(df)
print(df["email"])
print(type(df["email"])) #series - rows of a single column

print(df[["last", "email"]]) #filtered down dataframe but not series
print(df.columns)

#integer location - iloc
print(df.iloc[0]) #1st row
print(df.iloc[[0, 1]]) #1st and 2nd row
print(df.iloc[[0, 1], 2]) #iloc(rows, col)

print(df.loc[[0, 1], "email"]) #get email values of 1st and 2nd row
print(df.loc[[0, 1], ["email", "last"]]) #get email and last values of 1st and 2nd row


import pandas as pd

df = pd.read_csv(r"C:\Users\ADMIN\AI-ML\Pandas\movies.csv")
print(df["title"])
print(df["industry"].value_counts())
print(df.loc[0]) #gets values of 1st row
print(df.loc[0, "industry"]) #gets industry value for col 1
print(df.loc[[0, 1, 2], "industry"]) #gets industry value for col 1, 2, 3
print(df.loc[0:2, "industry":"imdb_rating"]) #gets industry to imdb_rating value for col 1, 2, 3