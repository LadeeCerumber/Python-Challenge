import csv

file_path = r"C:\Users\LabUser\Desktop\Classwork\Challenges\Python-Challenge\PyPoll\Resources\election_data.csv"

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Open the input file and read the data
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)  # Skip the header row
    for row in csvreader:
        candidate = row[2]
        total_votes += 1

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

output_file = "election_results.txt"

# Exporting the results to a text file
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")

    for candidate, vote_count in candidates.items():
        vote_percentage = vote_count / total_votes * 100
        file.write(f"{candidate}: {vote_percentage:.3f}% ({vote_count})\n")

        if vote_count > winner_votes:
            winner = candidate
            winner_votes = vote_count

    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

# Print the results to the console
with open(output_file, "r") as file:
    print(file.read())
