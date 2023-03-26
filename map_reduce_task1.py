import pandas as pd

# Read CSV file
data = pd.read_csv("part-001.csv")

# Convert column data to list of dictionaries
new_lists = [{value: 1} for value in data['date'].tolist()]

# Aggregate counts of each unique date value
aggregated_dict = {}
for new_dict in new_lists:
    key = list(new_dict.keys())[0]
    value = list(new_dict.values())[0]
    if key in aggregated_dict:
        aggregated_dict[key].append(value)
    else:
        aggregated_dict[key] = [value]

# Sum values for each key
for key in aggregated_dict.keys():
    aggregated_dict[key] = sum(aggregated_dict[key])

# Sort values
reversed(aggregated_dict)

# Write results to a .txt file
with open('results.txt', 'w') as f:
    for key, value in aggregated_dict.items():
        f.write(f"{key}: [{value}]\n")

