import sys

input_data_filename = "map.txt"

board = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        board.append(line.strip())
print(board)

# Part 1.
tree_count = 0
x = y = 0
width = len(board[0])
while y < len(board):
    print(f"coord=({x},{y})->{board[y][x]}")
    if board[y][x] == '#':
        tree_count += 1
    x = (x + 3) % width
    y += 1
print(tree_count)

# Part 2.
transformations = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

tree_count_per_transformation = []
for transformation in transformations:
    tree_count = 0
    x = y = 0
    width = len(board[0])
    while y < len(board):
        print(f"coord=({x},{y})->{board[y][x]}")
        if board[y][x] == '#':
            tree_count += 1
        x = (x + transformation[0]) % width
        y += transformation[1]
    print(tree_count)
    tree_count_per_transformation.append(tree_count)

prod = 1
for val in tree_count_per_transformation:
    prod *= val
print(prod)

