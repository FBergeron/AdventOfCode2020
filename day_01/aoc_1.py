import sys

input_data_filename = "my_numbers.txt"

numbers = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        numbers.append(int(line.strip()))

for x in range(len(numbers) - 1):
    for y in range(x, len(numbers) -1):
        if numbers[x] + numbers[y] == 2020:
            print(f"{numbers[x]} * {numbers[y]} = {numbers[x] * numbers[y]}")
            sys.exit()

