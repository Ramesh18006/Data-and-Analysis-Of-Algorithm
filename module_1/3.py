import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv("Class.csv")

# Step 2: Go through each cell
for i in range(len(df)):             # rows
    for j in range(len(df.columns)): # columns
        value = str(df.iloc[i, j])   # get the cell value as string
        if 'ai' in value.lower():    # check if 'ai' is inside
            print(f"Row {i}, Column {j} → {value}")
