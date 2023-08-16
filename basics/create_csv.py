import pandas as pd

# create a dataframe
df = pd.read_csv('random_data.csv')

# .head() = read specific number of rows
print(df.head(5))

# .tail() = last rows
print(df.tail())

# .columns = all the columns of the file
print(df.columns)