# input_data_filename = "instructions_short.txt"
input_data_filename = "instructions.txt"

instructions = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        line = line.strip()
        oper = line[0]
        modif = int(line[1:])
        instructions.append((oper, modif))
print(instructions)


def turn(modif):
    orientations = ['N', 'E', 'S', 'W'] if modif > 0 else ['N', 'W', 'S', 'E']
    i = orientations.index(orientation)
    new_i = (i + int((abs(modif) / 90))) % 4
    print(f"modif={modif} i={i} new_i={new_i}")
    return orientations[new_i]


def move(direction, modif):
    if direction == 'N':
        return x, y + modif
    elif direction == 'S':
        return x, y - modif
    elif direction == 'E':
        return x + modif, y
    elif direction == 'W':
        return x - modif, y
    else:
        print(f"direction={direction}")

x = y = 0
orientation = 'E'
for instruction in instructions:
    print(f"instruction={instruction}")
    oper, modif = instruction

    if oper in ['N', 'S', 'E', 'W']:
        new_x, new_y = move(oper, modif)
    elif oper == 'F':
        new_x, new_y = move(orientation, modif)
    elif oper == 'L':
        new_orientation = turn(-1 * modif)
        orientation = new_orientation
    elif oper == 'R':
        new_orientation = turn(modif)
        orientation = new_orientation

    x = new_x
    y = new_y

print(f"x={x} y={y}")
print(f"manhattan={abs(x) + abs(y)}")
