input_data_filename = "decl_form_data.txt"

# Part 1.

groups = []
with open(input_data_filename, 'r') as input_file:
    group = set()
    for line in input_file:
        if line == "\n":
            groups.append(group)
            group = set()
        else:
            line = line.strip()
            for c in line:
                group.add(c)
groups.append(group)
print(groups)

sum = 0
for group in groups:
    sum += len(group)
print(sum)


# Part 2.

groups = []
group_lines = []
with open(input_data_filename, 'r') as input_file:
    group = {}
    line_count = 0
    for line in input_file:
        if line == "\n":
            groups.append(group)
            group_lines.append(line_count)
            group = {}
            line_count = 0
        else:
            line = line.strip()
            for c in line:
                if c in group:
                    group[c] += 1
                else:
                    group[c] = 1
            line_count += 1
groups.append(group)
group_lines.append(line_count)

sum = 0
for index, group in enumerate(groups):
    print(group)
    for c in group:
        if group[c] == group_lines[index]:
            sum += 1
print(sum)
