import os 
import csv

#File Path
csvpath = os.path.join('documents', 'pypoll.csv')

# Declaring the Variables 
total_votes = 0
candidates = {}
candidate_percent = {}
winner_count = 0
winner = ""

# Read CSV 
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    for row in csvreader:
        # Determine Total Votes
        total_votes += 1
        # Find candidate list
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        # percentages for each candidate pulled from candidate dictionary
        # candidates dictionary: key = Name value = the number of votes
        for key, value in candidates.items():
            candidate_percent[key] = round((value/total_votes) * 100, 1)

        # Determine winner using candidate dictionary
        for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]


# Print results
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidate_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

#Path to Output File
output_file = os.path.join("documents","pypoll.txt")

# Print on Text File
with open(output_file, 'w') as file:
    file.write("Election Results \n")
    file.write("------------------------------------- \n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("------------------------------------- \n")
    for key, value in candidates.items():
        file.write(key + ": " + str(candidate_percent[key]) + "% (" + str(value) + ") \n")
    file.write("------------------------------------- \n")
    file.write("Winner: " + winner + "\n")
    file.write("------------------------------------- \n")