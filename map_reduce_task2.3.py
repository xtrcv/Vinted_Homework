data = {}

# Open the 'output.txt' file in read mode and loop through each line in the file
with open('output.txt', 'r') as f:
    for line in f:
        # Split each line into two parts based on the comma and store the parts in the 'key' and 'value'
        key, value = line.strip().split(', ')
        
        # Check if the 'key' already exists in the 'data' dictionary
        if key in data:
            # If it exists, append the 'value' to the existing list for that key
            data[key].append(int(value))
        else:
            # If it doesn't, create a new list with the 'value' for that key
            data[key] = [int(value)]

output = {}

# Loop through each key-value pair in the 'data' dictionary
for key, value in data.items():
    # Create a new key in the 'output' dictionary by concatenating the 'key' with the first value in the 'value' list
    # and set the value to a list with the count of the first value in the 'value' list
    output[f"{key}:{value[0]}"] = [value.count(value[0])]

# Open the 'final_result.txt' file in write mode and loop through each key-value pair in the 'output' dictionary
with open("final_result.txt", "w") as f:
    for key, value in output.items():
        # Write each key-value pair to a new line in the file in the format 'key:value\n'
        f.write(f"{key}:{value[0]}\n")
