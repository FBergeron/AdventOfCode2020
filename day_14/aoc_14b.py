input_data_filename = "init_prog.txt"
# input_data_filename = "init_prog_short_2.txt"

def setXBitsAs(mask, value):
    bin_value = bin(value)[2:]
    # print(f"bin_value={bin_value}")
    bin_value = list(bin_value)
    #print(f"bin_value={bin_value}")
    bin_value.reverse()
    mask = list(mask)
    mask.reverse()
    new_value = []
    i = 0
    for c in range(len(mask)):
        if mask[c] == 'X':
            new_value.append(bin_value[i] if i < len(bin_value) else '0')
            i += 1
        else:
            new_value.append(mask[c])
    new_value.reverse()
    # print(f"new_value={new_value}")
    return int(''.join(new_value), 2)


def apply_mask(addr, mask):
    addresses = []
    # print(f"apply_mask addr={addr} mask={mask}")
    bin_addr = bin(addr)[2:]
    bin_addr = (36 - len(bin_addr)) * '0' + bin_addr
    # print(f"v={bin_addr}")
    # print(f"m={mask}")
    and_mask = mask.replace('0', '1').replace('X', '1')
    # print(f"a={and_mask}")
    or_mask = mask.replace('X', '0')
    # print(f"o={or_mask}")
    res = addr & int(and_mask, 2) | int(or_mask, 2)
    res_bin_addr = bin(res)[2:]
    res_bin_addr = (36 - len(res_bin_addr)) * '0' + res_bin_addr
    # print(f"r={res_bin_addr}")
    res_mask = []
    chars = list(res_bin_addr)
    bit_count = 0
    for c in range(len(res_bin_addr)):
        if mask[c] == 'X':
            res_mask.append('X')
            bit_count += 1
        else:
            res_mask.append(chars[c])
    res_mask_str = ''.join(res_mask)
    # print(f"r={res_mask_str}")
    # print(f"bit_count={bit_count}")
    for i in range(2 ** bit_count):
        addresses.append(setXBitsAs(res_mask_str, i))

    return addresses


memory = {}
instructions = []
with open(input_data_filename, 'r') as input_file:
    for index, line in enumerate(input_file):
        line = line.strip()
        if line.startswith('mask'):
            mask_str = line[line.index('=') + 2:]
            # print(f"mask_str={mask_str}")
        else:
            addr = int(line[line.index('[') + 1:line.index(']')])
            value = int(line[line.index('=') + 2:])
            # print(f"addr={addr} value={value}")
            addresses = apply_mask(addr, mask_str)
            # print(f"addresses={addresses}")
            for address in addresses:
                # print(f"memory[{address}]={value}")
                memory[address] = value
sum = 0
for addr in memory:
    sum += memory[addr]
print(f"answer={sum}")
