import sys

# input_data_filename = "starting_numbers_short.txt"
input_data_filename = "starting_numbers.txt"

def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1

numbers = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        numbers += [int(x) for x in line.strip().split(",")]
print(numbers)


last_index = {}
orig_length = len(numbers)
i = 0
while i < 30000000:
# while i < 2020:
# while i < 12:
    if i % 100000 == 0:
        print(i)
    if i < orig_length:
        n = numbers[i]
        last_index[n] = i
    else:
        n = numbers[-1]
        if n in last_index:
            index = last_index[n]
            next_number = i - index - 1
            numbers.append(next_number)
            last_index[n] = i - 1
        # elif n not in numbers[:-1]:
        else:
            numbers.append(0)
            last_index[n] = i -1
    i += 1
print(f"answer={numbers[-1]}")
