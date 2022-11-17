# Create a Python script that analyzes the votes and calculates each of the following:
    # Total number of votes cast
    # Complete list of candidates who received votes
    # Percentage of votes each candidate won
    # Total number of votes each candidate won
    # Winner of the election (popular votes)

# import os and csv
import os
import csv

# Path to collect data 
csvpath=os.path.join("C:/Users/msmar/OneDrive/Desktop/python_challenge/PyPoll/Resources/election_data.csv")

# Lists to store data
ballot=[]
candidates_list=[]
county=[]
candidate=[]
percentage=[]

# Read csv
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter = ',')
    csv_header=next(csvreader)
    for row in csvreader:
        # Add votes
        ballot.append(row[0])

        # Add candidates
        candidates_list.append(row[2])
    
    # Total number of votes cast
    total_votes=len(ballot)
        
    # Sort candidates
    for x in candidates_list:
        if x not in candidate:
            candidate.append(x)
            print(x)
    votes_ccs=candidates_list.count(candidate[0])
    print(votes_ccs)
    votes_dd=candidates_list.count(candidate[1])
    print(votes_dd)
    votes_rad=candidates_list.count(candidate[2])
    print(votes_rad)
    
    # Candidate's vote percentage
    p_ccs=round((votes_ccs/total_votes)*100,3)
    print(p_ccs)
    p_dd=round((votes_dd/total_votes)*100,3)
    print(p_dd)
    p_rad=round((votes_rad/total_votes)*100,3)
    print(p_rad)
    
# Winner
votes=[votes_ccs, votes_dd,votes_rad]
vote_count=max(votes)
winner=candidate[votes.index(vote_count)]

# Print results
print("Election Results")
print("---------------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------------")
print(f"{candidate[0]}: {p_ccs}% ({votes_ccs})")
print(f"{candidate[1]}: {p_dd}% ({votes_dd})")
print(f"{candidate[2]}: {p_rad}% ({votes_rad})")
print("---------------------------------------")
print(f"Winner: {winner}")
print("---------------------------------------")

# Write Analysis file
with open("C:/Users/msmar/OneDrive/Desktop/python_challenge/PyPoll/analysis/election_results", "w") as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("---------------------------------------\n")
    text.write(f"{candidate[0]}: {p_ccs}% ({votes_ccs})\n")
    text.write(f"{candidate[1]}: {p_dd}% ({votes_dd})\n")
    text.write(f"{candidate[2]}: {p_rad}% ({votes_rad})\n")
    text.write("---------------------------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write("---------------------------------------\n")