import pandas as pd

df = pd.read_csv(r"C:\Users\ADMIN\AI-ML\Pandas\movies.csv")
print(df)
print(df.shape) #gives numbers of rows and columns
print(df.info())
pd.set_option("display.max_columns", 10)
print(df)

print(df.head()) #prints first 5 rows
print(df.head(10))

print(df.tail(10)) #prints last 10 rows