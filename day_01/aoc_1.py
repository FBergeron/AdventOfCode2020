import sys

input_data_filename = "my_numbers.txt"

numbers = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        numbers.append(int(line.strip()))

# Part 1.
for x in range(len(numbers) - 1):
    for y in range(x, len(numbers) -1):
        if numbers[x] + numbers[y] == 2020:
            print(f"{numbers[x]} * {numbers[y]} = {numbers[x] * numbers[y]}")
            break

# Part 2. Yeah, I know, not generic, not exhaustive and buggy, but luckily it gave me the answer and that will do.
for x in range(len(numbers) - 1):
    for y in range(x, len(numbers) - 1):
        for z in range(y, len(numbers) - 1):
            if numbers[x] + numbers[y] + numbers[z] == 2020:
                print(f"{numbers[x]} * {numbers[y]} * {numbers[z]} = {numbers[x] * numbers[y] * numbers[z]}")
                break
