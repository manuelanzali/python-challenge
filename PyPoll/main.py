
import os
import csv


# Path to collect data from Resources folder
electiondata_csv = os.path.join('Resources', 'election_data.csv')
file_to_create = os.path.join('analysis', 'election_analysis.text')

# Define the function and have it accept the 'election_data' as the sole parameter
def print_votes(election_data) :

    Ballot_ID = int(election_data[0])
    county = str(election_data[1])
    candidate = str(election_data[2])

    # return all variables
    return Ballot_ID, county, candidate


# Calculate the Total Number of Votes included in the data set: define file, open, skip header
def total_number_votes (csv_file) :
    with open(csv_file,'r') as csv_file :
        csvreader = csv.reader(csv_file, delimiter=",")
        next(csvreader)
        total_votes = sum(1 for row in csvreader)
    return total_votes

total_votes = total_number_votes(electiondata_csv)

# Create a list of candidates who received votes
def candidates_with_votes(csv_file):
    candidates_list = []
    with open(csv_file, 'r') as csvfile :
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)

        for row in csvreader :
            _, _, candidate = print_votes(row)
            if candidate not in candidates_list:
                candidates_list.append(candidate)
        return candidates_list
    # print ("candidates who received votes:", candidates_list)

candidates_list = candidates_with_votes(electiondata_csv)


# To calculate the percentage of votes : start with number of votes per candidate
def calculate_votes_per_candidate(csv_file):
    candidate_number_of_votes= {}
    with open(csv_file, 'r') as csv_file :
        csvreader = csv.reader(csv_file, delimiter=",")
        next(csvreader)

        for row in csvreader :
            _, _, candidate = print_votes(row)
            if candidate not in candidate_number_of_votes:
                candidate_number_of_votes[candidate] = 1
            else:
                candidate_number_of_votes[candidate] += 1
    return candidate_number_of_votes

candidate_number_of_votes = calculate_votes_per_candidate(electiondata_csv)

# Find winner of the election based on popular vote
winner = ""
max_popular_votes = 0
for candidate, votes in candidate_number_of_votes.items():
    if votes > max_popular_votes:
        max_popular_votes = votes
        winner = candidate


#Print to text file
with open(file_to_create, "w") as txt_file:


# Print "Election Results", "Total Votes", candidates with percentages and votes, and "winner"


    print("Election Results")
    txt_file.write("Election Results\n")


    print("----------------------------")
    txt_file.write("----------------------------\n")

    total_votes_text = f"Total Votes: {total_votes}"
    print(total_votes_text)
    txt_file.write(total_votes_text + "\n")
    #print(f"Total Votes: {total_votes}")

    print("----------------------------")
    txt_file.write("----------------------------\n")



    for candidate in candidates_list:
        votes = candidate_number_of_votes.get(candidate, 0)
        percentage_of_votes = (votes / total_votes) * 100
        txt_file.write(f"{candidate}: {percentage_of_votes:.3f}% ({votes})\n")
        print(f"{candidate}: {percentage_of_votes:.3f}% ({votes})")

    print("----------------------------")
    txt_file.write("----------------------------\n")

    winner_text = f"Winner: {winner}"
    print(winner_text)
    txt_file.write(winner_text + "\n")
    #print(f"Winner: {winner}")

    print("----------------------------")
    txt_file.write("----------------------------\n")


