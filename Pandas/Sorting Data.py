import pandas as pd

people = {
    "first": ["Corey", "Jane", "John", "Adam"],
    "last": ["Schafer", "Doe", "Doe", "Doe"],
    "email": ["coreschafer@gmail.com", "JaneDoe@gmail.com", "JohnDoe@gmail.com", "A@gmail.com"]
}
df = pd.DataFrame(people)

print(df.sort_values(by = "last")) #ascending order sort for column "last"
print(df.sort_values(by = "last", ascending = False)) #descending order sort for column "last"
print(df.sort_values(by = ["last", "first"], ascending = False))
print(df.sort_values(by = ["last", "first"], ascending = [False, True], inplace = True)) #for last descending order and for first ascending order
print(df)
print(df.sort_index())
print(df["last"].sort_values())



df = pd.read_csv(r"C:\Users\ADMIN\AI-ML\Pandas\movies.csv", index_col = "release_year") #set index as 'release year'

df.sort_values(by = ["title", "studio"], ascending = [True, False], inplace = True)
print(df)
print(df[["title", "studio"]].head(20))

print(df["imdb_rating"].nlargest(10))
print(df.nlargest(10, "imdb_rating"))
print(df.nsmallest(10, "imdb_rating"))