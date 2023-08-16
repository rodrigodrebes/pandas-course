import pandas as pd

# create a dataframe
df = pd.read_csv('random_data.csv')

# .head() = read specific number of rows
print(df.head(5))

# .tail() = last rows
print(df.tail())

# .columns = all the columns of the file
print(df.columns)

# . dtypes = the types of columns
print(df.dtypes)

# .describe() summary statistics of data
print(df.describe())

# [''] or [['','']] = access specific column
print(df['Age'])
print(df[['Name', 'Age']])

# .unique = unique values
print(df['Age'].unique())

# filtering specific row value
print(df[df['Age'] == 33])
print(df[(df['Name'] == "Rodrigo") & (df['Age'] == 34)])