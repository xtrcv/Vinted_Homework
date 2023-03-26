import os
import csv

with open('LT_IDs.txt') as f:
    integers = [line.strip() for line in f]

# Open the output file to write results
with open('output.txt', 'w') as f_out:
    # Loop through each CSV file in the specified directory
    for filename in os.listdir('/home/unserun/Desktop/Vinted Homework/data/clicks'):
        if filename.endswith('.csv'):
            # Open the CSV file
            with open(os.path.join('/home/unserun/Desktop/Vinted Homework/data/clicks', filename)) as f_csv:
                # Read the CSV file
                csv_reader = csv.reader(f_csv)
                next(csv_reader)  # skip header row

                # Loop through each row in the CSV file
                for row in csv_reader:
                    # Check if the ID matches any of the integers
                    if row[1] in integers:
                        # Write the matching row to the output file
                        f_out.write(f"{row[0]}, {row[1]}\n")
