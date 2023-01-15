import os
import csv

print("Election Results")
print("-------------------------")

total_votes = 0
with open("Resources/election_data.csv") as data_file:
    csv_reader = csv.reader(data_file)
    next(csv_reader)

    for row in csv_reader:
        total_votes += 1

print(f"Total Votes Cast: {total_votes}")
print("-------------------------")