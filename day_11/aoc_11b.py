# input_data_filename = "seat_layout_short.txt"
input_data_filename = "seat_layout.txt"

def display_layout(seat_layout):
    for y in range(len(seat_layout)):
        print(seat_layout[y])

def get_occupied_visible_seats_for_line(x, y, trans_x, trans_y, seat_layout):
    new_x = x + trans_x
    new_y = y + trans_y
    if new_x < 0 or new_x >= len(seat_layout[0]) or new_y < 0 or new_y >= len(seat_layout):
        return 0

    if seat_layout[new_y][new_x] == '#':
        return 1
    elif seat_layout[new_y][new_x] == 'L':
        return 0
    else:
        return get_occupied_visible_seats_for_line(new_x, new_y, trans_x, trans_y, seat_layout) 

def get_occupied_visible_seats(x, y, seat_layout):
    count = 0

    # Top left line.
    count += get_occupied_visible_seats_for_line(x, y, -1, -1, seat_layout)    

    # Top line.
    count += get_occupied_visible_seats_for_line(x, y, 0, -1, seat_layout)    

    # Top right line.
    count += get_occupied_visible_seats_for_line(x, y, 1, -1, seat_layout)    

    # Left line.
    count += get_occupied_visible_seats_for_line(x, y, -1, 0, seat_layout)    
    
    # Right line.
    count += get_occupied_visible_seats_for_line(x, y, 1, 0, seat_layout)    
    
    # Bottom left line.
    count += get_occupied_visible_seats_for_line(x, y, -1, 1, seat_layout)    
    
    # Bottom line.
    count += get_occupied_visible_seats_for_line(x, y, 0, 1, seat_layout)    
    
    # Bottom right line.
    count += get_occupied_visible_seats_for_line(x, y, 1, 1, seat_layout)    

    return count


def apply_rules(seat_layout, debug=False):
    x = y = 0
    width = len(seat_layout[0])
    new_seat_layout = []
    for y in range(len(seat_layout)):
        new_seat_layout.append(list(' ' * width))

    for y in range(len(seat_layout)):
        for x in range(width):
            occupied_visible_seats = get_occupied_visible_seats(x, y, seat_layout)
            if debug:
                new_seat_layout[y][x] = get_occupied_visible_seats(x, y, seat_layout)
            else:
                if seat_layout[y][x] == 'L' and occupied_visible_seats == 0:
                    new_seat_layout[y][x] = '#'
                elif seat_layout[y][x] == '#' and occupied_visible_seats >= 5:
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

iteration = 0
while True:
    print(f"iteration={iteration}")
    new_seat_layout = apply_rules(seat_layout)
    if is_equal(seat_layout, new_seat_layout):
        break
    iteration += 1
    seat_layout = new_seat_layout
    # display_layout(seat_layout)
print(f"iterations={iteration + 1}")
# display_layout(new_seat_layout)
count = get_occupied_seats_count(new_seat_layout)
print(f"total occupied seats={count}")

