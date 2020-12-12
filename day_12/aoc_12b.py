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


def turn_wp(wp_dx, wp_dy, modif):
    next_signs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    iter_count = int(abs(modif) / 90) % 4
    for i in range(iter_count):
        signs = (1 if wp_dx > 0 else -1, 1 if wp_dy > 0 else -1)
        sign_for_dx, sign_for_dy = next_signs[(next_signs.index(signs) + 1) % 4] if modif > 0 else next_signs[(next_signs.index(signs) - 1) % 4]

        tmp = wp_dx
        wp_dx = abs(wp_dy) * sign_for_dx
        wp_dy = abs(tmp) * sign_for_dy

    return wp_dx, wp_dy

x = y = 0
wp_dx = 10
wp_dy = 1
for instruction in instructions:
    print(f"instruction={instruction}")
    oper, modif = instruction

    if oper == 'N':
         wp_dy += modif
    elif oper =='S':
         wp_dy -= modif
    elif oper == 'E':
         wp_dx += modif
    elif oper == 'W':
         wp_dx -= modif
    elif oper == 'R':
        wp_dx, wp_dy = turn_wp(wp_dx, wp_dy, modif)
    elif oper == 'L':
        wp_dx, wp_dy = turn_wp(wp_dx, wp_dy, -modif)
    elif oper == 'F':
        x += (wp_dx * modif)
        y += (wp_dy * modif)

    print(f"x={x} y={y} wp_dx={wp_dx} wp_dy={wp_dy}")

print(f"x={x} y={y}")
print(f"manhattan={abs(x) + abs(y)}")
