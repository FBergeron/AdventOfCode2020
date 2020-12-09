from itertools import combinations
import sys

input_data_filename = "numbers.txt"

numbers = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        numbers.append(int(line.strip()))
print(numbers)


# Part 1.

window_size = 25

def is_valid(numbers, total):
    comb = combinations(numbers, 2)
    for c in comb:
        if c[0] + c[1] == total:
            return True
    return False

for i in range(window_size, len(numbers) + 1):
    window_start = i - window_size 
    window_end = i
    window = numbers[window_start:window_end]
    # print(f"window_start={window_start} end={window_end} window={window}")
    if not is_valid(window, numbers[i]):
        print(f"i={i} number={numbers[i]}")
        break

max_index = i
total = numbers[i]

# Part 2.

for l in range(2,25):
    for i in range(0, max_index - l):
        print(f"l={l} i={i} numbers={numbers[i:i+l]} sum={sum(numbers[i:i+l])}")
        res = sum(numbers[i:i+l])
        if res == total:
            print(f"res has been found: {res}")
            print(f"min={min(numbers[i:i+l])}")
            print(f"max={max(numbers[i:i+l])}")
            print(f"sum={min(numbers[i:i+l]) + max(numbers[i:i+l])}")
            sys.exit()

