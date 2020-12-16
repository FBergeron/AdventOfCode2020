import sys

input_data_filename = "ticket_data.txt"
# input_data_filename = "ticket_data_short.txt"

fields = {}
my_ticket = []
nearby_tickets = []

line_is_rule = True
line_is_my_ticket = False
line_is_nearby_ticket = False

with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        line = line.strip()
     
        print(f"line={line}")

        if line == "your ticket:":
            line_is_rule = False
            line_is_my_ticket = True
            continue

        if line == "nearby tickets:":
            line_is_my_ticket = False
            line_is_nearby_tickets = True
            continue

        if line == "":
            continue

        if line_is_rule:
            field_name = line[:line.index(":")]
            # print(f"field_name={field_name}")
            field_range_1 = line[line.index(":") + 2:line.index("or ") - 1]
            # print(f"field_range_1={field_range_1}")
            field_range_1 = [int(x) for x in field_range_1.split('-')]
            field_range_2 = line[line.index("or ") + 3:]
            # print(f"field_range_2={field_range_2}")
            field_range_2 = [int(x) for x in field_range_2.split('-')]
            fields[field_name] = [field_range_1, field_range_2]
        elif line_is_my_ticket:
            my_ticket = [int(x) for x in line.split(",")]
        elif line_is_nearby_tickets:
            nearby_tickets.append([int(x) for x in line.split(",")])
print(f"fields={fields}")
print(f"my_ticket={my_ticket}")
print(f"nearby_tickets={nearby_tickets}")


def is_value_valid(value, rules):
    for rule in rules:
        min, max = rule
        if value >= min and value <= max:
            return True
    return False 


def is_over():
    count = 0
    for p in range(len(field_positions)):
        if len(field_positions[p]) == 1 and field_positions[p][0].startswith('departure'):
            count += 1
    return count == 6


invalid_tickets = []
for ticket in nearby_tickets:
    for value in ticket:
        is_valid = False
        for field_name, rules in fields.items():
            if is_value_valid(value, rules):
                is_valid = True
                break
        if not is_valid:
            invalid_tickets.append(ticket)

print(f"before len={len(nearby_tickets)}")
print(f"{len(invalid_tickets)} invalid tickets have been found.")
for ticket in invalid_tickets:
    nearby_tickets.remove(ticket)
print(f"after len={len(nearby_tickets)}")

field_positions = []
for p in range(len(fields)):
    print(f"p={p}")
    valid_fields = sorted(fields.keys())
   
    # print(f"valid_fields={valid_fields}")
    for ticket in nearby_tickets:
        value = ticket[p]
        for field in list(valid_fields):
            if not is_value_valid(value, fields[field]):
                valid_fields.remove(field)
                # print(f"valid_fields={valid_fields}")
                break
    
    field_positions.append(valid_fields)
for pos, fields in enumerate(field_positions):
    print(f"Pos {pos}: {fields}")

i = 0
while not is_over():
    print(f"Pass {i}")
    sure_positions = []
    for p in range(len(field_positions)):
        if len(field_positions[p]) == 1:
            sure_positions.append(field_positions[p][0])
    for q in range(len(field_positions)):
        if len(field_positions[q]) > 1:
            for pos in sure_positions:
                if pos in field_positions[q]:
                    field_positions[q].remove(pos)
    i += 1
for pos, fields in enumerate(field_positions):
    print(f"Pos {pos}: {fields}")

prod = 1
for p in range(len(field_positions)):
    if len(field_positions[p]) == 1 and field_positions[p][0].startswith('departure'):
        print(f"p={p} my_ticket={my_ticket[p]}")
        prod *= my_ticket[p]
print(f"prod={prod}")
