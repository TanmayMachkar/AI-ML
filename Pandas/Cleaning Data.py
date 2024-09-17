import pandas as pd
import numpy as np

people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}
df = pd.DataFrame(people)

print(df)
print(df.dropna()) #drop empty rows
print(df.dropna(axis = "index", how = "any")) #index = drop empty rows, column = drop empty columns, any = drop if any element is missing
print(df.dropna(axis = "index", how = "all")) #index = drop empty rows, column = drop empty columns, all = drop if all elements of a row are missing
print(df.dropna(axis = "columns", how = "all"))
print(df.dropna(axis = "columns", how = "any"))
