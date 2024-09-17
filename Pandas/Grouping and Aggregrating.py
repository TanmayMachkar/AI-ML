import pandas as pd

df = pd.read_csv(r"C:\Users\ADMIN\AI-ML\Pandas\movies.csv", index_col = "release_year") #set index as 'release year'

print(df["imdb_rating"].median())
print(df.describe())
print(df["imdb_rating"].count())
print(df["industry"].value_counts())

print(df["studio"].value_counts())
print(df["studio"].value_counts(normalize = True)) #sort by percentage


##### GROUP BY
lang_group = df.groupby(["language"])

print(lang_group.get_group("English"))
print(lang_group["studio"].value_counts().loc["English"])
#alternate way given below
filt = df["language"] == "English"
print(df.loc[filt])
print(df.loc[filt]["studio"].value_counts())
#above process first finds rows that contain "English" then from those columns we group the studio and find out their value counts

print(lang_group["imdb_rating"].median())
print(lang_group["imdb_rating"].agg(["median", "mean"]))
print(lang_group["imdb_rating"].agg(["median", "mean"]).loc["Hindi"])
#alternate way given below
filt = df["language"] == "English"
print(df.loc[filt]["studio"].str.contains("Universal Pictures"))
#above process first finds rows that contain "English" and then finds out which rows have studio as "Universal Pictures"
print(df.loc[filt]["studio"].str.contains("Universal Pictures").sum()) #sum also works with boolean values

print(lang_group["studio"].apply(lambda x: x.str.contains("Universal Pictures").sum()))

#get % of studios that have language as english
studio_value_counts = df["language"].value_counts()
studio_uses_english = df["language"].str.contains("English").sum()
studio_uses_english_series = pd.Series([studio_uses_english], index=["English_Studio_Uses"])
python_df = pd.concat([studio_value_counts, studio_uses_english_series], axis=1)
python_df.columns = ["Total_Languages", "English_Studio_Uses"]
python_df["Percentage_Studio_Using_English"] = (python_df["English_Studio_Uses"] / python_df["Total_Languages"]) * 100
print(python_df)