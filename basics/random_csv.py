import pandas as pd
import random

# record number
num_records = 1000

# random name samples
names = ["Vitor", "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Igor", "Jill", "Mary", "Paulo", "Sandro", "Rodrigo", "Tiago"]

# generating random data
data = {
    "Name": [random.choice(names) for _ in range(num_records)],
    "Age": [random.randint(18, 70) for _ in range(num_records)],
    "Salary": [random.randint(2000, 50000) for _ in range(num_records)]
}

# converting into dataframe
df = pd.DataFrame(data)

# saving as csv
df.to_csv("random_data.csv", index=False)
