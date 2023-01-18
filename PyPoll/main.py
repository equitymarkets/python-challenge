#imports python modules
import os
import csv

#declares and initializes working variables
total_votes = 0
candidate_raw_list = []
candidate_pool = []
vote_pool = []

#Input Path is based upon running terminal session from PyBank/ folder. Adjust accordingly
with open("Resources/election_data.csv") as data_file:
    #Set the reader
    csv_reader = csv.reader(data_file)
    #Determines months in set, extreme values, and PnL changes
    print(csv_reader)
    next(csv_reader)
    #Determines months in set, extreme values, and PnL changes
    for row in csv_reader:
        total_votes += 1
        candidate_raw_list.append(row[2])
        if(row[2] not in candidate_pool):
            candidate_pool.append(row[2])
    for row in candidate_pool:
        vote_pool.append(candidate_raw_list.count(row))
    #Alerts user to empty set
    if(total_votes == 0):
        print("Your data set is empty. Please check your data.")
        exit()
    election_winner = candidate_pool[vote_pool.index(max(vote_pool))]



#writes csv file to PyPoll/analysis/voting_analysis.csv with votes for candidate, all votes, percentage, and winner
output_path = os.path.join("analysis", "voting_analysis.csv")
with open(output_path, 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(["Candidate", "Votes", "Total","Percentage", "Win/Lose"])
    i = 0
    for candidate in candidate_pool:
        csv_writer.writerow([candidate, vote_pool[i], total_votes, '{:,.3%}'.format(vote_pool[i]/total_votes), "Winner" if candidate == election_winner else "Loser"])
        i += 1

#Terminal output = total votes for anyone cast, votes per candidate, percentage for each, and winner. 
print("Election Results")
print("-------------------------")
print(f"Total Votes Cast: {total_votes}")
print("-------------------------")
i = 0
for candidate in candidate_pool:
    vote_share_per_candidate = vote_pool[i]/total_votes
    print(f"{candidate}: {vote_share_per_candidate:,.3%} {vote_pool[i]}")
    i += 1
print("-------------------------")
print(f"Winner: {election_winner}")
print("-------------------------")

