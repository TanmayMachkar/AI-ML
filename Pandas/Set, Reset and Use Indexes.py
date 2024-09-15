import pandas as pd

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["coreschafer@gmail.com", "JaneDoe@gmail.com", "JohnDoe@gmail.com"]
}
df = pd.DataFrame(people)
df.set_index("email", inplace = True) #set index and make changes permanently
print(df)
print(df.index)
print(df.loc["coreschafer@gmail.com"])
print(df.loc["coreschafer@gmail.com", "last"])
print(df.iloc[0]) #df.loc[0] doesnt work since index has been changed
df.reset_index(inplace = True)
print(df)

df = pd.read_csv(r"C:\Users\ADMIN\AI-ML\Pandas\movies.csv", index_col = "release_year") #set index as 'release year'
print(df.loc[1955])

df = pd.read_csv(r"C:\Users\ADMIN\AI-ML\Pandas\movies.csv", index_col = "title") #set index as 'release year'
print(df.loc["Pather Panchali"])
print(df.loc["Pather Panchali", "studio"])
print(df.sort_index()) #sort alphabetically by default
print(df.sort_index(ascending = False)) #sort alphabetically in descending order