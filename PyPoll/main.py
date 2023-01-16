import os
import csv

print("Election Results")
print("-------------------------")

total_votes = 0
candidate_raw_list = []
candidate_pool = []
vote_pool = []


with open("Resources/election_data.csv") as data_file:
    csv_reader = csv.reader(data_file)
    next(csv_reader)

    for row in csv_reader:
        total_votes += 1
        candidate_raw_list.append(row[2])
        if(row[2] not in candidate_pool):
            candidate_pool.append(row[2])
    for row in candidate_pool:
        vote_pool.append(candidate_raw_list.count(row))
    election_winner = candidate_pool[vote_pool.index(max(vote_pool))]
#Alerts user to empty set
if(total_votes == 0):
    print("Your data set is empty.")

print(f"Total Votes Cast: {total_votes}")
print("-------------------------")
#print(candidate_pool)
i = 0
for candidate in candidate_pool:
    vote_share_per_candidate = vote_pool[i]/total_votes
    print(f"{candidate}: {vote_share_per_candidate:,.3%} {vote_pool[i]}")

    i += 1
print("-------------------------")
print(f"Winner: {election_winner}")
print("-------------------------")

