import pandas as pd

# create a dataframe
df = pd.read_csv('random_data.csv')

# retrieve the total of null rows
print(df.isnull().sum())

#drop the null values of rows
df.dropna(inplace=True)

#creating new column and updating all values
df["New Column"] = "value for all rows"
print(df)

#creating new columns 
df["Calculated Column"] = df['Age']+df['Salary']
print(df)

#updating a single value using iloc
df.iloc[0,-2] = "value updated for specific row"
print(df)