import sys

input_data_filename = "initial_state_short.txt"
# input_data_filename = "initial_state.txt"


def display_hypercube(hypercube):
    for w in range(len(hypercube)):
        print("w={w}, ", end='')
        display_cube(hypercube[w])

def display_cube(cube):
    for z in range(len(cube)):
        print(f"z={z}")
        for y in range(len(cube[z])):
            for x in range(len(cube[z][y])):
                print(cube[z][y][x], end='')
            print("")
        print("")


def count_surrounding_active_neighbors(x, y, z, cube):
    # print(f"count_surrounding_active_neighbors x={x} y={y} z={z} len(cube)={len(cube)}")
    count = 0
    for zz in range(max(z - 1, 0), min(z + 2, len(cube))):
        # print(f"zz={zz}")
        for yy in range(max(y - 1, 0), min(y + 2, len(cube[zz]))):
            # print(f"yy={yy}")
            for xx in range(max(x - 1, 0), min(x + 2, len(cube[zz][yy]))):
                # print(f"xx={xx}")
                if xx == x and yy == y and zz == z:
                    continue
                else:
                    if cube[zz][yy][xx] == '#':
                        count += 1
    return count


def count_active_units(hypercube):
    count = 0
    for ww in range(len(hypercube)):
        for zz in range(len(hypercube[ww])):
            for yy in range(len(hypercube[ww][zz])):
                for xx in range(len(hypercube[ww][zz][yy])):
                    if hypercube[ww][zz][yy][xx] == '#':
                        count += 1
    return count


def expand_cube(cube):
    z_layer_count = len(cube)
    y_layer_count = len(cube[0])
    x_layer_count = len(cube[0][0])

    def build_empty_larger_layout():
        layer = []
        for y in range(y_layer_count + 2):
            layer.append(list("." * (x_layer_count + 2)))
        return layer

    new_cube = []
    new_cube.append(build_empty_larger_layout())
    for z in range(z_layer_count):
        layer = []
        layer.append(list("." * (x_layer_count + 2)))
        for y in range(y_layer_count):
            line = []
            line.append(".")
            for x in range(x_layer_count):
                line.append(cube[z][y][x])
            line.append(".")
            layer.append(line)

        layer.append(list("." * (x_layer_count + 2)))

        new_cube.append(layer)
    new_cube.append(build_empty_larger_layout())

    return new_cube


def make_copy(cube):
    new_cube = []
    for z in range(len(cube)):
        layer = []
        for y in range(len(cube[z])):
            line = []
            for x in range(len(cube[z][y])):
                line.append(cube[z][y][x])
            layer.append(line)
        new_cube.append(layer)
    return new_cube

hypercube = []
cube = []
layer = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        line = line.strip()
        layer.append(list(line))
cube.append(layer)
hypercube.append(cube)

print(f"Before any cycles:")
display_hypercube(hypercube)
active_count = count_active_units(hypercube)
print(f"active_count={active_count}")

cycle = 0
while cycle < 6:
   
    # hypercube = expand_hypercube(hypercube)
    # new_cube = make_copy(cube)

    # for z in range(len(cube)):
    #     for y in range(len(cube[z])):
    #         for x in range(len(cube[z][y])):
    #             c = count_surrounding_active_neighbors(x, y, z, cube)
    #             # print(f"{cube[z][y][x]} x={x} y={y} z={z} c={c}")
    #             if cube[z][y][x] == '#':
    #                 if c not in [2, 3]:
    #                     new_cube[z][y][x] = "."
    #             else:
    #                 if c == 3:
    #                     new_cube[z][y][x] = "#"

    cycle += 1

    print(f"After {cycle} cycles")
    display_cube(new_cube)

    active_count = count_active_units(new_cube)
    print(f"active_count={active_count}")

    cube = new_cube
