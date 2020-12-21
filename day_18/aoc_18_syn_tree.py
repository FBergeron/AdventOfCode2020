import sys

input_data_filename = "problems_data_very_short.txt"
# input_data_filename = "problems_data_short.txt"
# input_data_filename = "problems_data.txt"

problems = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        line = line.strip()
        if line.startswith('#'):
            continue
        if '#' in line:
            line = line[:line.index('#')]
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


def build_tree_rec(tree, chars, level=0, parent_chars=[]):
    print(f"build_tree_rec tree={tree} chars={chars} level={level} parent_chars={parent_chars}")
    if chars == None or len(chars) == 0:
        return tree

    c = chars[len(chars) - 1]
    
    if level == 0:
        if c.isdigit():
            return build_tree_rec([int(c)], chars[:-1], level)

        elif c == '+':
            return [c, build_tree_rec([], chars[:-1], level, parent_chars), tree] 
        elif c == '-':
            return [c, build_tree_rec([], chars[:-1], level, parent_chars), tree] 
        elif c == '*':
            return [c, build_tree_rec([], chars[:-1], level, parent_chars), tree] 
        elif c == '/':
            return [c, build_tree_rec([], chars[:-1], level, parent_chars), tree] 
    if c == ')':
        # return build_tree_rec([], chars[:-1], level + 1, parent_chars)
        return build_tree_rec(tree, chars[:-1], level + 1, parent_chars)
    elif c == '(':
        print(f"( found parent_chars={parent_chars}")
        # subtree = build_tree_rec([], parent_chars, level - 1)
        subtree = build_tree_rec(tree, parent_chars)
        print(f"subtree={subtree}")
        return build_tree_rec(subtree, chars[:-1], level - 1)
    else:
        parent_chars = [c] + parent_chars
        return build_tree_rec(tree, chars[:-1], level, parent_chars)

def evaluate_tree_rec(tree):
    if tree is None or len(tree) == 0:
        return 0

    value = tree[0]
    # print(type(value))
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
    print(f"tree={tree}\n\n")
    res = evaluate_tree_rec(tree)
    print(f"res={res}\n\n")
    sum += res
print(f"sum={sum}")
