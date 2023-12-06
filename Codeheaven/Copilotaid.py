import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(r'C:\Users\aciftcioglu\Downloads\Datasets\bankmarketing_train.csv')

# Example of a for loop
items = []
for item in df['loan']:
    # Add each item to the array
    items.append(item)

# Print the array
print(items)





