input_data_filename = "boardingpass_data.txt"

boarding_passes = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        boarding_passes.append(line.strip())

# Part 1

all_seats = []
highest_seat_id = 0;
for boarding_pass in boarding_passes:
    row = boarding_pass[:7]
    col = boarding_pass[7:]
    row_in_binary_str = row.replace('F', '0').replace('B', '1')
    col_in_binary_str = col.replace('L', '0').replace('R', '1')
    row_in_decimal = int(f"0b{row_in_binary_str}", 2)
    col_in_decimal = int(f"0b{col_in_binary_str}", 2)
    seat_id = row_in_decimal * 8 + col_in_decimal
    all_seats.append(seat_id)
    print(f"row={row} bin={row_in_binary_str} dec={row_in_decimal} col={col} bin={col_in_binary_str} dec={col_in_decimal} seat_id={seat_id}")
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id
print(f"highest_seat_id={highest_seat_id}")
print(f"total seats={len(all_seats)}")

# Part 2
i = None
my_seat = None
for seat in sorted(all_seats):
    if i is None:
        i = seat
    print(f"seat={seat} vs i={i} ==? {i==seat}")
    if i == seat:
        i += 1
    else:
        my_seat = i
        break
print(f"my_seat={my_seat}")
