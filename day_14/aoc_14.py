input_data_filename = "init_prog.txt"

mask = None
or_mask = None
and_mask = None

memory = {}
addresses_used = set()

with open(input_data_filename, 'r') as input_file:
    for index, line in enumerate(input_file):
        line = line.strip()
        if line.startswith("mask"):
            mask = line[line.index('=') + 2:]
            or_mask = int(mask.replace("X", "0"), 2)
            and_mask = int(mask.replace("1", "X").replace("X", "1"), 2)
            print(f"mask={mask} or={or_mask} and={and_mask}")
        else:
            mem_addr = int(line[line.index('[') + 1:line.index(']')])
            mem_value = int(line[line.index('=') + 1:])
            addresses_used.add(mem_addr)
            print(f"orig_value={mem_value} after masking={mem_value | or_mask | and_mask}")
            memory[mem_addr] = ((mem_value | or_mask) & and_mask)
            print(f"mem[{mem_addr}] = {memory[mem_addr]}")

sum = 0
for address in addresses_used:
    sum += memory[address]
print(sum)
