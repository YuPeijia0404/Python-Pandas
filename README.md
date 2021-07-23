# Python-Pandas
### Open the file
* `df = pd.read_csv(file_name)`
* `print(df.head(3))` (Get the first n-th rows)
* `print(df.tail(3))` (Get the last n-th rows)
### Reading Data in Pandas
#### Read Headers
* `df.columns`
#### Read each Column
* `df[column_name]`
#### Read each Row
* `df.head(number)`
* `df.iloc[start:end]`
#### Read a specific location
* `df.iloc[row,column]`
#### Read all Row
* `df.iterrows()`
### Sorting/ Describing Data
#### Get the information of some columns
* `df.describe()`
#### Sort by some columns
* `df.sort_values(column_names_array, ascending=[])`
#### Make changes to data
* Assign values to a new column
* `df.drop(columns=[column_name])` to remove a column
* `df[column_name] = df.iloc[start:end, start:end].sum(axis=0/1)`
### Filter Data
#### Conditions
* `df.loc[df[key] == value]`
* `df.loc[~df[key] == value]` -> the condition is not True
#### Reset index after filter the data
* `df.reset_index(grop=True)`
### Conditional changes
* `df.loc[df[condition], modifying column] = modifying value`
### Aggregate Statistics (Groupby)
`df.groupby(column_name).attr`
### Work with large amounts of data
`for df in pd.read_csv(csv_name, chunksize=num)`