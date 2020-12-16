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


sum = 0
for ticket in nearby_tickets:
    for value in ticket:
        print(f"value={value}")
        is_valid = False
        for field_name, rules in fields.items():
            print(f"field_name={field_name} rules={rules}")
            print(type(rules))
            if is_value_valid(value, rules):
                is_valid = True
                break
        if not is_valid:
            sum += value
print(f"sum={sum}")

