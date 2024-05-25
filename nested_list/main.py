# Read data from the file
with open('inputs.in', 'r') as file:
    lines = file.readlines()

# Initialize an empty list to hold name-score pairs
arr = []

# Start reading from the second line (index 1)
input_count = 1
for _ in range(int(lines[0].strip())):
    name = lines[input_count].strip()  # Get the name and strip any whitespace
    input_count += 1
    score = float(lines[input_count].strip())  # Get the score and convert to float
    input_count += 1
    arr.append([name, score])  # Add the name-score pair to the list

# Sort the list by the score
sorted_arr = sorted(arr, key=lambda x: x[1])

# Extract all unique scores and sort them
all_scores = [score for _, score in sorted_arr]
set_scores = sorted(set(all_scores))  # Sort the unique scores
allnames = []

# Check if there is a second smallest score
if len(set_scores) > 1:
    second_smallest_score = set_scores[1]
    for name, score in sorted_arr:
        if score == second_smallest_score:
            allnames.append(name)
sortednames = sorted(allnames) 
for h in sortednames:
    print(str(h))
