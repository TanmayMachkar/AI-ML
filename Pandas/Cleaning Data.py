import pandas as pd
import numpy as np

people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}
df = pd.DataFrame(people)

df.replace("NA", np.nan, inplace= True)
df.replace("Missing", np.nan, inplace= True)

print(df)
print(df.dropna()) #drop empty rows
print(df.dropna(axis = "index", how = "any")) #index = drop empty rows, column = drop empty columns, any = drop if any element is missing
print(df.dropna(axis = "index", how = "all")) #index = drop empty rows, column = drop empty columns, all = drop if all elements of a row are missing
print(df.dropna(axis = "columns", how = "all"))
print(df.dropna(axis = "columns", how = "any"))
print(df.dropna(axis = "index", how = "any", subset = ["email"])) #subset = "email" returns rows that have atleast their email content filled in 
print(df.dropna(axis = "index", how = "all", subset = ["last","email"])) #subset = "last","email" returns rows that have atleast their email or last content filled in

print(df.isna())
print(df.fillna("MISSING"))
print(df.fillna(0))

print(df.dtypes)
print(type(np.nan))

df["age"] = df["age"].astype(float) #converting to float since datatype of nan is float
print(df["age"].mean())


na_vals = ["NA", "Missing"]
df = pd.read_csv(r"C:\Users\ADMIN\AI-ML\Pandas\movies.csv", index_col = "release_year") #set index as 'release year'
df["revenue"].replace(['more than 20', 'more  than 20'], 0, inplace= True)
df["revenue"] = df["revenue"].astype(float) #convert to float
print(df["revenue"].mean())
print(df["revenue"].median())