import pandas as pd

df = pd.read_csv(r"C:\Users\ADMIN\AI-ML\Pandas\survey_results_public.csv", index_col = "ResponseId") #set index as 'release year'
print(df)

filt = (df["Country"] == "India")
india_df = df.loc[filt]
print(india_df.head())

#creating new csv file
india_df.to_csv(r"C:\Users\ADMIN\AI-ML\Pandas\DummyCsv\modified.csv")
#creating new tsv file
india_df.to_csv(r"C:\Users\ADMIN\AI-ML\Pandas\DummyCsv\modified.tsv", sep = '\t') #creating a tab limited file where content is separated by tabs instead of commas

#EXCEL
india_df.to_excel(r"C:\Users\ADMIN\AI-ML\Pandas\DummyCsv\modified.xlsx")
test = pd.read_excel(r"C:\Users\ADMIN\AI-ML\Pandas\DummyCsv\modified.xlsx", index_col = "ResponseId")
print(test.head())

#JSON
india_df.to_json(r"C:\Users\ADMIN\AI-ML\Pandas\DummyCsv\modified.json")
india_df.to_json(r"C:\Users\ADMIN\AI-ML\Pandas\DummyCsv\modified.json", orient = "records", lines = True) #organises content in list like format instead of the default dictionary format and lines = True means it will be more readable
test = pd.read_json(r"C:\Users\ADMIN\AI-ML\Pandas\DummyCsv\modified.json", orient = "records", lines = True)
print(test.head())

#JSON By URL
post_df = pd.read_json('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Flask_Blog/snippets/posts.json')
print(post_df.head())

#SQL
from sqlalchemy import create_engine
import psycopg2

engine = create_engine("postgresql://postgres:tanmay143459!@localhost:5432/test")
india_df.to_sql("sample_table", engine, if_exists = "replace") #create table in test database by the name sample_table

sql_df = pd.read_sql("sample_table", engine, index_col = "ResponseId")
print(sql_df.head())

sql_df = pd.read_sql_query("SELECT * FROM sample_table", engine, index_col = "ResponseId")
print(sql_df.head())