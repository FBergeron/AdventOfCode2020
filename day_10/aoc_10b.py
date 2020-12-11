input_data_filename = "joltages.txt"
# input_data_filename = "joltages_short.txt"
# input_data_filename = "joltages_very_short.txt"

joltages = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        joltages.append(int(line.strip()))
joltages.append(0)
# Add last joltage.
if len(joltages) == 0:
    joltages.append(3)
else:
    joltages.append(max(joltages) + 3)
joltages.sort()


# Build a tree that represents all the joltage chains.
def build_chains(joltages):
    chains = {}
    for i in range(1, len(joltages)):
        next_joltage = joltages[i]
        print(f"i={i} next_joltage={next_joltage}")
        for j in range(max(0, i-3), i):
            if joltages[j] in chains and next_joltage - joltages[j] <= 3:
                chains[joltages[j]].append(next_joltage)
        chains[joltages[i-1]] = [next_joltage]
    return chains


def count_rec(i, memoization_table={}):
    print(f"count_rec i={i}")
    if i in memoization_table:
        return memoization_table[i]

    if i not in chains:
        memoization_table[i] = 1
        return 1
    sum = 0
    for child in chains[i]:
        sum += count_rec(child, memoization_table)
    memoization_table[i] = sum
    return sum


chains = build_chains(joltages)
# print(chains)

count = count_rec(0) 
print(f"res={count}")
