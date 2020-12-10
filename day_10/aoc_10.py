from itertools import combinations
import sys

input_data_filename = "voltages.txt"

joltages = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        joltages.append(int(line.strip()))
print(joltages)

# Part 1.

joltage_diffs = {}

curr_joltage = 0
while len(joltages) > 0:
    next_joltage = min(joltages)
    diff = next_joltage - curr_joltage
    if diff not in joltage_diffs:
        joltage_diffs[diff] = 1
    else:
        joltage_diffs[diff] += 1
    joltages.remove(next_joltage)
    curr_joltage = next_joltage
next_joltage = curr_joltage + 3
diff = next_joltage - curr_joltage
if diff not in joltage_diffs:
    joltage_diffs[diff] = 1
else:
    joltage_diffs[diff] += 1
curr_joltage = next_joltage
print(f"curr_joltage={curr_joltage} joltage_diffs={joltage_diffs}")
print(f"answer={joltage_diffs[1] * joltage_diffs[3]}")

