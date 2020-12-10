import sys

# input_data_filename = "joltages.txt"
input_data_filename = "joltages_short.txt"
# input_data_filename = "joltages_very_short.txt"

joltages = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        joltages.append(int(line.strip()))
# joltages.append(1)
# joltages.append(2)
# joltages.append(3)
# joltages.append(4)
# joltages.append(5)
# joltages.append(6)
# print(joltages)

# The simplest cases are as follow:
#
# [] -> [ [0,3] ]
# [1] -> [ [0,1,4] ]
# [1,2] -> [ [0,1,2,5], [0,2,5] ]
#
# [] -> [ a ]
# [1] -> [ b ]
# [1,2] -> [ d, e ]
#

def find_next_joltages(curr_joltage, joltages):
    joltages_copy = joltages.copy()
    res = []
    if len(joltages_copy) == 0:
        return res
    while True:
        if len(joltages_copy) == 0:
            break
        next_joltage = min(joltages_copy)
        if next_joltage - curr_joltage > 3:
            break
        res.append(next_joltage)
        joltages_copy.remove(next_joltage)
    return res



# This function find only one chain.
# def find_joltage_chain_rec(chain, curr_joltage, joltages):
#     joltages_copy = joltages.copy()
#     if len(joltages_copy) == 0:
#         chain.append(curr_joltage + 3)
#         return chain
#     next_joltage = min(joltages_copy)
#     joltages_copy.remove(next_joltage)
#     chain.append(next_joltage)
#     return find_joltage_chain_rec(chain, next_joltage, joltages_copy)
#
# x = find_joltage_chain_rec([0], 0, joltages)
# print(f"x={x}")
# print(f"joltages={joltages}")

# Add last joltage.
if len(joltages) == 0:
    joltages.append(3)
else:
    joltages.append(max(joltages) + 3)
joltages.sort()

def find_all_joltage_chains_rec(all_chains, joltages):
    # print(f"find_all_joltage_chains_rec all_chains={len(all_chains)} joltages={len(joltages)}")
    print(f"find_all_joltage_chains_rec all_chains={all_chains} joltages={joltages}")
    if len(joltages) == 0:
        return all_chains

    next_joltage = min(joltages)
    joltages.remove(next_joltage)

    new_chains = []
    for chain in all_chains:
        if len(chain) > 1:
            if next_joltage - chain[-2] <= 3:
                new_chain = chain[:-1] + [next_joltage]
                new_chains.append(new_chain)
        if chain[-1] - next_joltage <= 3:
            chain.append(next_joltage)
    for new_chain in new_chains:
        all_chains.append(new_chain)
    return find_all_joltage_chains_rec(all_chains, joltages)

all_chains = [[0]]
find_all_joltage_chains_rec(all_chains, joltages)
# print(f"all_chains={all_chains}")
print(f"total={len(all_chains)}")

# This solution works for small data sets but consumes too much memory for large data sets.
# Instead of acuumulating arrays, building a tree should be more efficient.
# Once I get the tree, it's easy to count the paths, I think.
# count_rec(node) => sum(count-rec(node-child-1), count-rec(node-child-2), ..., count-rec(node-child-3))

