from itertools import combinations
import sys

# input_data_filename = "joltages.txt"
input_data_filename = "joltages_very_short.txt"

joltages = []
# with open(input_data_filename, 'r') as input_file:
#     for line in input_file:
#         joltages.append(int(line.strip()))
joltages.append(1)
# joltages.append(4)
# joltages.append(5)
# joltages.append(6)
print(joltages)

# Part 1.

# joltage_diffs = {}
#
# curr_joltage = 0
# while len(joltages) > 0:
#     next_joltage = min(joltages)
#     diff = next_joltage - curr_joltage
#     if diff not in joltage_diffs:
#         joltage_diffs[diff] = 1
#     else:
#         joltage_diffs[diff] += 1
#     joltages.remove(next_joltage)
#     curr_joltage = next_joltage
# next_joltage = curr_joltage + 3
# diff = next_joltage - curr_joltage
# if diff not in joltage_diffs:
#     joltage_diffs[diff] = 1
# else:
#     joltage_diffs[diff] += 1
# curr_joltage = next_joltage
# print(f"curr_joltage={curr_joltage} joltage_diffs={joltage_diffs}")
# print(f"answer={joltage_diffs[1] * joltage_diffs[3]}")

# Part 2.

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
# I want a function that take a list of joltages and return a list of all chains.
#
# But I think that I would also need a function that return 1 chain.
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
def find_joltage_chain_rec(chain, curr_joltage, joltages):
    joltages_copy = joltages.copy()
    if len(joltages_copy) == 0:
        chain.append(curr_joltage + 3)
        return chain
    next_joltage = min(joltages_copy)
    joltages_copy.remove(next_joltage)
    chain.append(next_joltage)
    return find_joltage_chain_rec(chain, next_joltage, joltages_copy)

x = find_joltage_chain_rec([0], 0, joltages)
print(f"x={x}")
print(f"joltages={joltages}")


# def find_all_joltage_chains_rec(all_chains, curr_chains, curr_joltage, joltages):
#     print(f"find_all_joltage_chains_rec all_chains={all_chains} curr_chains={curr_chains} curr_joltage={curr_joltage} joltages={joltages}")
#     if len(joltages) == 0:
#         for chain in curr_chains:
#             chain.append(curr_joltage + 3)
#             all_chains.append(chain)
#         return all_chains
#     res = []
#     next_joltages = find_next_joltages(curr_joltage, joltages)
#     print(f"next_joltages={next_joltages}")
#     for next_joltage in next_joltages:
#         joltages_copy = joltages.copy()
#         joltages_copy.remove(next_joltage)
#         for chain in curr_chains:
#             chain.append(next_joltage)
#         chains = find_all_joltage_chains_rec(all_chains, curr_chains, next_joltage, joltages_copy)
#         print(f"chains={chains}")
#         res.append(chains)
#     return(res)
#
#     # while (True):
#     #     if len(joltages) == 0:
#     #         break
#
#     #     next_joltage = min(joltages)
#     #     print(f"next_joltage={next_joltage}")
#     #     if (next_joltage - curr_joltage > 3):
#     #         break
#
#     #     joltages.remove(next_joltage)
#     #     for chain in curr_chains:
#     #         chain.append(next_joltage)
#     #     find_all_joltage_chains_rec(all_chains, curr_chains, next_joltage, joltages)
#
# all_chains = []
# res = find_all_joltage_chains_rec(all_chains, [[0]], 0, joltages)
# print(f"all_chains={all_chains}")
# print(f"res={res}")
