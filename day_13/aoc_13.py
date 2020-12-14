# input_data_filename = "bus_data_short.txt"
input_data_filename = "bus_data.txt"

earliest_timestamp = None
bus_ids = []
with open(input_data_filename, 'r') as input_file:
    for index, line in enumerate(input_file):
        line = line.strip()
        if index == 0:
            earliest_timestamp = int(line)
        elif index == 1:
            bus_ids_list = line.split(",")
            for bus_id in bus_ids_list:
                if bus_id != 'x':
                    bus_ids.append(int(bus_id))


def find_next_earliest_timestamp(earliest_timestamp, bus_id):
    modulo = earliest_timestamp % bus_id
    if modulo == 0:
        return earliest_timestamp
    else:
        return earliest_timestamp - modulo + bus_id


next_timestamps = [find_next_earliest_timestamp(earliest_timestamp, bus_id) for bus_id in bus_ids]
best_bus_index = next_timestamps.index(min(next_timestamps))
best_bus = bus_ids[best_bus_index]
minutes_to_wait = next_timestamps[best_bus_index] - earliest_timestamp
print(f"best_bus={best_bus} minutes_to_wait={minutes_to_wait} res={best_bus * minutes_to_wait}")


