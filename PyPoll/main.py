import os
import csv

print("Election Results")
print("-------------------------")

total_votes = 0
candidate_pool = []
election_winner = "No Name"
with open("Resources/election_data.csv") as data_file:
    csv_reader = csv.reader(data_file)
    next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        if(row[2] not in candidate_pool):
            candidate_pool.append(row[2])
print(f"Total Votes Cast: {total_votes}")
print("-------------------------")
print(candidate_pool)
print("-------------------------")
print(f"Winner: {election_winner}")
print("-------------------------")