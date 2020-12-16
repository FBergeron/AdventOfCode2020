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

while len(numbers) < 2020:
    i = len(numbers)
    if i % 100 == 0:
        print(i)
    n = numbers[-1]
    # print(f"numbers={numbers} i={i} n={n}")
    if n not in numbers[:-1]:
        numbers.append(0)
    else:
        index = rindex(numbers[:-1], n)
        print(f"index={index}")
        numbers.append(i - index - 1)
print(f"answer={numbers[-1]}")
