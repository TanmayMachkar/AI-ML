import pandas as pd

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["coreschafer@gmail.com", "JaneDoe@gmail.com", "JohnDoe@gmail.com"]
}
df = pd.DataFrame(people)
print(df["last"] == "Doe")

filt = (df["last"] == "Doe")

#below 2 return same thing
print(df[filt])
print(df.loc[filt])

print(df.loc[filt, "email"])

# & - and
# | - or
# ~ - gives opposite of what is filtered
filt = (df["last"] == "Doe") & (df["first"] == "John")
print(df.loc[filt, "email"])

filt = (df["last"] == "Doe") | (df["first"] == "John")
print(df.loc[filt, "email"])

filt = (df["last"] == "Doe") | (df["first"] == "John")
print(df.loc[~filt, "email"])

df = pd.read_csv(r"C:\Users\ADMIN\AI-ML\Pandas\movies.csv", index_col = "release_year") #set index as 'release year'
high_rating = (df["revenue"] < 1000)
print(df.loc[high_rating, ["studio"]])

lang = ["Bengali", "Kannada"]
filt = df["language"].isin(lang)
print(df.loc[filt, "title"])

filt = df["studio"].str.contains("Universal Pictures", na = False) # na = False means we won't be handling any errors
print(df.loc[filt, "title"])