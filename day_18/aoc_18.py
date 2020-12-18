import sys

input_data_filename = "problems_data_short.txt"
# input_data_filename = "problems_data.txt"

problems = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        line = line.strip()
        problems.append(line.replace(' ', ''))
print(problems)


# The calculation order is reversed.
# 
# def evaluate_problem_rec(chars):
#     if chars == None or len(chars) == 0:
#         return 0
# 
#     if len(chars) == 1:
#         return int(chars[0])
# 
#     arg1 = None
#     oper = None
#     i = 0
#     while i < len(chars):
#         c = chars[i]
#         if c.isdigit():
#             arg1 = int(c)
#         elif c == '+':
#             return arg1 + evaluate_problem_rec(chars[i + 1:])
#         elif c == '-':
#             return arg1 - evaluate_problem_rec(chars[i + 1:])
#         elif c == '*':
#             return arg1 * evaluate_problem_rec(chars[i + 1:])
#         elif c == '/':
#             return arg1 / evaluate_problem_rec(chars[i + 1:])
#         elif c == '(':
#             arg1 = evaluate_problem_rec(chars[i + 1:])
#         elif c == ')':
#             return arg1
#         i += 1
#     return 0

# The parenthesis expressions cut the computation process.
# 
# def evaluate_problem_rec(chars):
#     if chars == None or len(chars) == 0:
#         return 0
# 
#     if len(chars) == 1:
#         return int(chars[0])
# 
#     arg = None
#     oper = None
#     i = len(chars) - 1
#     while i > 0:
#         c = chars[i]
#         if c.isdigit():
#             arg = int(c)
#         elif c == '+':
#             return evaluate_problem_rec(chars[:i]) + arg
#         elif c == '-':
#             return evaluate_problem_rec(chars[:i]) - arg
#         elif c == '*':
#             return evaluate_problem_rec(chars[:i]) * arg 
#         elif c == '/':
#             return evaluate_problem_rec(chars[:i]) / arg
#         elif c == '(':
#             return arg
#         elif c == ')':
#             arg = evaluate_problem_rec(chars[:i])
#         i -= 1
#     return arg

def evaluate_problem_rec(chars, end_pos):
    print(f"evaluate_problem_rec chars={chars}, end_pos={end_pos}")
    if chars == None or len(chars) == 0:
        return 0

    if len(chars) == 1:
        return int(chars[0])

    arg = None
    oper = None
    i = len(chars) - 1
    while i > 0:
        c = chars[i]
        if c.isdigit():
            arg = int(c)
        elif c == '+':
            return evaluate_problem_rec(chars[:i], end_pos) + arg
        elif c == '-':
            return evaluate_problem_rec(chars[:i], end_pos) - arg
        elif c == '*':
            return evaluate_problem_rec(chars[:i], end_pos) * arg
        elif c == '/':
            return evaluate_problem_rec(chars[:i], end_pos) / arg
        elif c == '(':
            print(f"i={i} end_pos={end_pos} arg={arg}")
            print(f"return {arg, end_pos -i}")
            return arg, end_pos - i
        elif c == ')':
            res = evaluate_problem_rec(chars[:i], end_pos)
            if isinstance(res, tuple):
                print(f"res={res}")
                arg, delta = res
                i -= delta
            else:
                arg = res
        i -= 1
    return arg, end_pos - i

sum = 0
for problem in problems:
    chars = list(problem)
    # chars.reverse()
    res = evaluate_problem_rec(chars, len(chars) - 1)
    print(f"problem={problem} res={res}")
    sum += res
print(f"sum={sum}")
