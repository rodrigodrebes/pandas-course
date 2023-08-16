import numpy as np
import pandas as pd

# Create a 2D numpy array
array_data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Convert the numpy array to a DataFrame
df = pd.DataFrame(array_data, columns=["Column_A", "Column_B", "Column_C"])

# Print the DataFrame
print(df)
