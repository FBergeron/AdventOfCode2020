import sys

# input_data_filename = "initial_state_short.txt"
input_data_filename = "initial_state.txt"


def display_hypercube(hypercube):
    for w in range(len(hypercube)):
        print(f"w={w}, ", end='')
        display_cube(hypercube[w])

def display_cube(cube):
    for z in range(len(cube)):
        print(f"z={z}")
        for y in range(len(cube[z])):
            for x in range(len(cube[z][y])):
                print(cube[z][y][x], end='')
            print("")
        print("")


def count_surrounding_active_neighbors(x, y, z, w, hypercube):
    # print(f"count_surrounding_active_neighbors x={x} y={y} z={z} len(hypercube)={len(hypercube)}")
    count = 0
    for ww in range(max(w -1, 0), min(w + 2, len(hypercube))):
        for zz in range(max(z - 1, 0), min(z + 2, len(hypercube[ww]))):
            # print(f"zz={zz}")
            for yy in range(max(y - 1, 0), min(y + 2, len(hypercube[ww][zz]))):
                # print(f"yy={yy}")
                for xx in range(max(x - 1, 0), min(x + 2, len(hypercube[ww][zz][yy]))):
                    # print(f"xx={xx}")
                    if ww == w and xx == x and yy == y and zz == z:
                        continue
                    else:
                        if hypercube[ww][zz][yy][xx] == '#':
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


def expand_hypercube(hypercube):
    w_dim_count = len(hypercube)
    z_dim_count = len(hypercube[0])
    y_dim_count = len(hypercube[0][0])
    x_dim_count = len(hypercube[0][0][0])

    def build_empty_larger_layout():
        layer = []
        for y in range(y_dim_count + 2):
            layer.append(list("." * (x_dim_count + 2)))
        return layer

    def build_empty_larger_cube():
        cube = []
        for z in range(z_dim_count + 2):
            cube.append(build_empty_larger_layout())
        return cube
            
    new_hypercube = []
    new_hypercube.append(build_empty_larger_cube())

    for w in range(w_dim_count):
        cube = []
        cube.append(build_empty_larger_layout())

        for z in range(z_dim_count):
            layer = []
            layer.append(list("." * (x_dim_count + 2)))
            for y in range(y_dim_count):
                line = []
                line.append(".")
                for x in range(x_dim_count):
                    line.append(hypercube[w][z][y][x])
                line.append(".")
                layer.append(line)
            layer.append(list("." * (x_dim_count + 2)))
            cube.append(layer)

        cube.append(build_empty_larger_layout())
        new_hypercube.append(cube)

    new_hypercube.append(build_empty_larger_cube())
    
    return new_hypercube


def make_copy(hypercube):
    new_hypercube = []
    for w in range(len(hypercube)):
        cube = []
        for z in range(len(hypercube[w])):
            layer = []
            for y in range(len(hypercube[w][z])):
                line = []
                for x in range(len(hypercube[w][z][y])):
                    line.append(hypercube[w][z][y][x])
                layer.append(line)
            cube.append(layer)
        new_hypercube.append(cube)
    return new_hypercube


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
   
    hypercube = expand_hypercube(hypercube)
    # display_hypercube(hypercube)
    new_hypercube = make_copy(hypercube)
    # display_hypercube(new_hypercube)

    for w in range(len(hypercube)):
        for z in range(len(hypercube[w])):
            for y in range(len(hypercube[w][z])):
                for x in range(len(hypercube[w][z][y])):
                    c = count_surrounding_active_neighbors(x, y, z, w, hypercube)
                    # print(f"{hypercube[z][y][x]} x={x} y={y} z={z} c={c}")
                    if hypercube[w][z][y][x] == '#':
                        if c not in [2, 3]:
                            new_hypercube[w][z][y][x] = "."
                    else:
                        if c == 3:
                            new_hypercube[w][z][y][x] = "#"

    cycle += 1

    print(f"After {cycle} cycles")
    display_hypercube(new_hypercube)

    active_count = count_active_units(new_hypercube)
    print(f"active_count={active_count}")

    hypercube = new_hypercube
