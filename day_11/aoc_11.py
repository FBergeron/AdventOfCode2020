# input_data_filename = "seat_layout_short.txt"
input_data_filename = "seat_layout.txt"

def display_layout(seat_layout):
    for y in range(len(seat_layout)):
        print(seat_layout[y])

def get_occupied_adjacent_seats(x, y, seat_layout):
    count = 0
    if y > 0:
        # Top left.
        if x > 0 and seat_layout[y - 1][x - 1] == '#':
            count += 1

        # Top middle.
        if seat_layout[y - 1][x] == '#':
            count += 1

        # Top right. 
        if x < len(seat_layout[0]) - 1 and seat_layout[y - 1][x + 1] == '#':
            count += 1

    # Left.
    if x > 0 and seat_layout[y][x - 1] == '#':
        count += 1

    # Right.
    if x < len(seat_layout[0]) - 1 and seat_layout[y][x + 1] == '#':
        count += 1

    if y < len(seat_layout) - 1:
        # Bottom left.
        if x > 0 and seat_layout[y + 1][x - 1] == '#':
            count += 1

        # Bottom middle.
        if seat_layout[y + 1][x] == '#':
            count += 1

        # Bottom right. 
        if x < len(seat_layout[0]) - 1 and seat_layout[y + 1][x + 1] == '#':
            count += 1

    return count

def apply_rules(seat_layout, debug=False):
    x = y = 0
    width = len(seat_layout[0])
    new_seat_layout = []
    for y in range(len(seat_layout)):
        new_seat_layout.append(list(' ' * width))

    for y in range(len(seat_layout)):
        for x in range(width):
            occupied_adjacent_seats = get_occupied_adjacent_seats(x, y, seat_layout)
            if debug:
                new_seat_layout[y][x] = get_occupied_adjacent_seats(x, y, seat_layout)
            else:
                if seat_layout[y][x] == 'L' and occupied_adjacent_seats == 0:
                    new_seat_layout[y][x] = '#'
                elif seat_layout[y][x] == '#' and occupied_adjacent_seats >= 4:
                    new_seat_layout[y][x] = 'L'
                else:
                    new_seat_layout[y][x] = seat_layout[y][x]
    return new_seat_layout

def is_equal(seat_layout_1, seat_layout_2):
    for y in range(len(seat_layout_1)):
        for x in range(len(seat_layout_1[0])):
            if seat_layout_1[y][x] != seat_layout_2[y][x]:
                return False
    return True

def get_occupied_seats_count(seat_layout):
    count = 0
    for y in range(len(seat_layout)):
        for x in range(len(seat_layout[0])):
            if seat_layout[y][x] == '#':
                count += 1
    return count

seat_layout = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        seat_layout.append(list(line.strip()))
display_layout(seat_layout)

# Part 1.

iteration = 0
while True:
    print(f"iteration={iteration}")
    new_seat_layout = apply_rules(seat_layout)
    if is_equal(seat_layout, new_seat_layout):
        break
    iteration += 1
    seat_layout = new_seat_layout
print(f"iterations={iteration + 1}")
count = get_occupied_seats_count(new_seat_layout)
print(f"total occupied seats={count}")
