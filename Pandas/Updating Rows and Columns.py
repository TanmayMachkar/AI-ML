import pandas as pd

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["coreschafer@gmail.com", "JaneDoe@gmail.com", "JohnDoe@gmail.com"]
}
df = pd.DataFrame(people)
print(df.columns)
df.columns = ["first_name", "last_name", "email"] #rename
print(df)

# df.columns = [x.upper() for x in df.columns]
# print(df)

df.columns = df.columns.str.replace(" ", "_") #replace " " with "_"
print(df)

df.rename(columns = {"first_name" : "first", "last_name" : "last"}, inplace = True) #True means make changes permanent
print(df)

df.loc[2] = ["John", "Smith", "JohnSmith@gmail.com"]
print(df)

df.loc[2, ["last", "email"]] = ["Doe", "JohnDoe@gmail.com"]
print(df)

df.loc[2, "last"] = "Smith"
print(df)

df.at[2, "last"] = "Doe"
print(df)

filt = (df["email"] == "JohnDoe@gmail.com")
print(df[filt]["last"])

filt = (df["email"] == "JohnDoe@gmail.com")
df.loc[filt, "last"] = "Smith"
print(df)

df["email"] = df["email"].str.lower()
print(df)

##### APPLY
print(df["email"].apply(len)) #find out length of all attributes of email column

def update_email(email):
    return email.upper()

print(df["email"].apply(update_email)) #convert to upper all attributes of email column
df["email"] = df["email"].apply(update_email)
print(df)

df["email"] = df["email"].apply(lambda x: x.lower())
print(df)

#min value of each column
print(df.apply(pd.Series.min)) 
print(df.apply(lambda x: x.min()))

##### APPLYMAP
print(df.applymap(len)) #finds length of all attributes of every column
print(df.applymap(str.lower))

##### MAP & REPLACE
print(df["first"].map({"Corey": "Chris", "Jane" : "Mary"})) # replaces 2 names but doesn't retain 3rd name which was not modified

print(df["first"].replace({"Corey": "Chris", "Jane" : "Mary"})) #temporary change

df["first"] = df["first"].replace({"Corey": "Chris", "Jane" : "Mary"})
print(df)



df = pd.read_csv(r"C:\Users\ADMIN\AI-ML\Pandas\movies.csv", index_col = "release_year")

df.rename(columns = {"title": "Title"}, inplace = True)
print(df["Title"])

df["industry"] = df["industry"].map({"Bollywood": True, "Hollywood": False})
print(df["industry"])
