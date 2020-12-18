import sys

input_data_filename = "problems_data_very_short.txt"
# input_data_filename = "problems_data_short.txt"
# input_data_filename = "problems_data.txt"

problems = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        line = line.strip()
        problems.append(line.replace(' ', ''))
print(problems)


def build_tree(chars):
    tree = build_tree_rec([], chars)
    return tree


# def build_tree_rec(tree, chars):
#     print(f"build_tree_rec tree={tree} chars={chars}")
#     if chars == None or len(chars) == 0:
#         return tree
# 
#     c = chars[0]
#     
#     if c.isdigit():
#         return build_tree_rec([int(c)], chars[1:])
# 
#     elif c == '+':
#         return [c, tree, build_tree_rec([], chars[1:])] 
#     elif c == '-':
#         return [c, tree, build_tree_rec([], chars[1:])] 
#     elif c == '*':
#         return [c, tree, build_tree_rec([], chars[1:])] 
#     elif c == '/':
#         return [c, tree, build_tree_rec([], chars[1:])] 


def build_tree_rec(tree, chars):
    print(f"build_tree_rec tree={tree} chars={chars}")
    if chars == None or len(chars) == 0:
        return tree

    c = chars[len(chars) - 1]
    
    if c.isdigit():
        return build_tree_rec([int(c)], chars[:-1])

    elif c == '+':
        return [c, build_tree_rec([], chars[:-1]), tree] 
    elif c == '-':
        return [c, build_tree_rec([], chars[:-1]), tree] 
    elif c == '*':
        return [c, build_tree_rec([], chars[:-1]), tree] 
    elif c == '/':
        return [c, build_tree_rec([], chars[:-1]), tree] 


def evaluate_tree_rec(tree):
    if tree is None or len(tree) == 0:
        return 0

    value = tree[0]
    print(type(value))
    if value == '+':
        return evaluate_tree_rec(tree[1]) + evaluate_tree_rec(tree[2])
    elif value == '-':
        return evaluate_tree_rec(tree[1]) - evaluate_tree_rec(tree[2])
    elif value == '*':
        return evaluate_tree_rec(tree[1]) * evaluate_tree_rec(tree[2])
    elif value == '/':
        return evaluate_tree_rec(tree[1]) / evaluate_tree_rec(tree[2])
    else:
        return value


sum = 0
for problem in problems:
    chars = list(problem)
    tree = build_tree(chars)
    print(f"tree={tree}")
    res = evaluate_tree_rec(tree)
    sum += res
print(f"sum={sum}")
