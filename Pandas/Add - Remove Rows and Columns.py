import pandas as pd

people = {
    "first": ["Corey", "Jane", "John"],
    "last": ["Schafer", "Doe", "Doe"],
    "email": ["coreschafer@gmail.com", "JaneDoe@gmail.com", "JohnDoe@gmail.com"]
}
df = pd.DataFrame(people)

df["full_name"] = df["first"] + " " + df["last"]
print(df)
print(df.drop(columns = ["first", "last"], inplace = True))
print(df)

df[["first", "last"]] = df["full_name"].str.split(" ", expand = True)
print(df)

print(df._append({"first": "Tony"}, ignore_index = True))

people = {
    "first": ["Tony", "Steve"],
    "last": ["Stark", "Rogers"],
    "email": ["IronMan@avenge.com", "Cap@avenge.com"]
}
df2 = pd.DataFrame(people)
print(df2)

df = df._append(df2, ignore_index = True)
print(df)

print(df.drop(index = 4))
filt = df["last"] == "Doe"
print(df.drop(index = df[filt].index))