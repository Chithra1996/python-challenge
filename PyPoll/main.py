import os
import csv
#Resource file

poll_csv = os.path.join("Resources", "election_data.csv")


#Initial Lists
candidate = []
unique_candidate = []
candidate_vote = 0.0
candidate_vote_count = []
candidate_vote_percent = []

total_vote_count = 0
candidate_percent = 0.0


with open(poll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
# Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
#Print the header row
    print(f"Header: {csv_header}")

#get the total number of votes and candidate list    
    for row in csv_reader:
        
        total_vote_count = total_vote_count + 1
        candidate.append(row[2])

#get unique candidate and their counts and percentage    
    for x in set(candidate):
        unique_candidate.append(x)
        candidate_vote = candidate.count(x)
        candidate_vote_count.append(candidate_vote)

        candidate_percent = round((candidate_vote/total_vote_count)*100,2)
        candidate_vote_percent.append(candidate_percent)
#get the winning candidate
    winning_vote_count = max(candidate_vote_count)    
    winning_candidate = unique_candidate[candidate_vote_count.index(winning_vote_count)]

#print on console/terminal
    print("-------------------------")
    print("Election Results")   
    print("-------------------------")
    print("Total Votes :" + str(total_vote_count))    
    print("-------------------------")
    for p in range(len(unique_candidate)):
                print(unique_candidate[p] + ": " + str(candidate_vote_percent[p]) +"% (" + str(candidate_vote_count[p])+ ")")
    print("-------------------------")
    print("The winner is: " + winning_candidate)
    print("-------------------------")

#write on file. 
    output_path = "Analysis/election_results.txt"
    with open(output_path, 'w') as text:

        text.write("-------------------------\n")
        text.write("Election Results \n")   
        text.write("-------------------------\n")
        text.write("Total Votes :" + str(total_vote_count)+ "\n")    
        text.write("-------------------------\n")
        for p in range(len(unique_candidate)):
                    text.write(unique_candidate[p] + ": " + str(candidate_vote_percent[p]) +"% (" + str(candidate_vote_count[p])+ ")"+ "\n")
        text.write("-------------------------\n")
        text.write("The winner is: " + winning_candidate+ "\n")
        text.write("-------------------------\n")

