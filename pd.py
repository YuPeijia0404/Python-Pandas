import pandas as pd
# Special character sequences
import re

df = pd.read_csv('pokemon_data.csv')

print(df.loc[df["Type 1"] == "Fire"])

print(df.describe())

df['Total'] = df['HP'] + df['Attack'] + df['Defense']
print(df)
df = df.drop(columns=['Total'])
print(df)

df.to_csv('modified.csv', index = False)

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
print(new_df)
new_df.reset_index(drop=True, inplace=True)
print(new_df)

# Column "Type 1" contains "Fire" or "Grass"
df = df.loc[df["Type 1"].str.contains('Fire|Grass', regex=True)]
df = df.loc[df["Type 1"].str.contains('fire|grass', flags=re.I, regex=True)]
print(df)

# "^" -> the first letter, "*" -> zero to many
df = df.loc[df["Name"].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
print(df)
