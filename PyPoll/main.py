import csv
import os

input_file_path = os.path.join('Resources', 'election_data.csv')
output_file_path = 'analysis.txt'

total_votes = 0
candidates = {}

with open(input_file_path) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for record in reader:
        # The total number of votes cast
        total_votes = total_votes + 1
        name = record[2]
        # A complete list of candidates who received votes
        if name in candidates:
            candidates[name] = candidates[name] + 1
        else:
            candidates[name] = 0

        print(candidates)

output_path = "analysis.txt"
txt_file = open('analysis.txt', 'w')

print('Total votes:', total_votes, file = txt_file)

for name in candidates:
    vote_count = candidates[name]
    percentage = (vote_count / total_votes) * 100
    print(name, vote_count, "%{:.3f}".format(percentage), file = txt_file)

