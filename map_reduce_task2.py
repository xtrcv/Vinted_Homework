import os
import csv

# Specify the directory where the csv files are located
directory = '/home/unserun/Desktop/Vinted Homework/data/users'

# Iterate over all files in the directory with the .csv extension
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename)
        with open(filepath, newline='') as csvfile:
            # Read the CSV file
            reader = csv.DictReader(csvfile)
            # Create an empty list to store the IDs that match the condition
            id_list = []
            # Loop over each row in the CSV file
            for row in reader:
                # Check if the 'country' column has a value of 'LT'
                if row['country'] == 'LT':
                    # If it does, append the value of the 'id' column to the list
                    id_list.append(row['id'])
            # Write the matching IDs to a text file
            with open('LT_IDs.txt', 'a') as outfile:
                outfile.write('\n'.join(id_list) + '\n')

