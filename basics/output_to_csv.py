import pandas as pd

values = [
    {'Name': "Notebook I5 16GB 500SSD", 'Price': 800, 'Quantity': 1},
    {'Name': "Desktop I7 32GB 1TB SSD", 'Price': 1200, 'Quantity': 3},
    {'Name': "Tablet 4GB 128GB", 'Price': 300, 'Quantity': 5},
    {'Name': "Smartphone 4GB 64GB", 'Price': 400, 'Quantity': 10}
]

df=pd.DataFrame(values)

# .to_csv(archivename.csv)
df.to_csv('output.csv', index=False)

newdf = pd.read_csv('output.csv')
print(newdf)

