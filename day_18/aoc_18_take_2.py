import sys

input_data_filename = "problems_data_short.txt"
# input_data_filename = "problems_data.txt"

problems = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        line = line.strip()
        problems.append(line.replace(' ', ''))
print(problems)


def add_parenthesis_rec(chars):
    if chars == None or len(chars) == 0:
        return None

    if len(chars) == 1:
        return chars[0]

    arg1 = None
    oper = None
    i = len(chars) - 1
    while i > 0:
        c = chars[i]
        if c.isdigit():
            arg1 = c
        elif c == '+':
            return ['(', arg1, c, add_parenthesis_rec(chars[i + 1:]), ')']
        elif c == '-':
            return ['(', arg1, c, add_parenthesis_rec(chars[i + 1:]), ')']
        elif c == '*':
            return ['(', arg1, c, add_parenthesis_rec(chars[i + 1:]), ')']
        elif c == '/':
            return ['(', arg1, c, add_parenthesis_rec(chars[i + 1:]), ')']
        elif c == '(':
            pass #arg1 = [c, add_parenthesis_rec(chars[i + 1:])
        elif c == ')':
            pass #return arg1

        i += 1


sum = 0
for problem in problems:
    chars = list(problem)
    # chars.reverse()
    res = add_parenthesis_rec(chars)
    print(f"problem={problem} res={res}")
    # sum += res
    break
print(f"sum={sum}")

