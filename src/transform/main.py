import pandas as pd
import sqlite3
from datetime import datetime

df = pd.read_json('../data/data.jsonl', lines=True)

pd.options.display.max_columns = None

df['_source'] = "https://lista.mercadolivre.com.br/chinelo-masculino"

df['_data_coleta'] = datetime.now()

df['Old_Price'] = df['Old_Price'].fillna(0).astype(float)
df['Old_Cents'] = df['Old_Cents'].fillna(0).astype(float)
df['New_Price'] = df['New_Price'].fillna(0).astype(float)
df['New_Cents'] = df['New_Cents'].fillna(0).astype(float)
df["Reviews_Rating"] = df["Reviews_Rating"].fillna(0).astype(float)

df['Old_Price_Total'] = df['Old_Price'] + df['Old_Cents'] / 100
df['New_Price_Total'] = df['New_Price'] + df['New_Cents'] / 100

df['Reviews_Total'] = df['Reviews_Total'].str.replace(r'[\(\)]', '', regex=True)
df['Reviews_Total'] = df['Reviews_Total'].fillna(0).astype(int)

df = df.drop(columns=['Old_Price', 'Old_Cents', 'New_Price','New_Cents'])

conn = sqlite3.connect('../data/mercadolivre.db')

df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

conn.close()

print(df.head())

#%%
print(df.columns())
# %%
