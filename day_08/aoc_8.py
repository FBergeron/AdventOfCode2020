# input_data_filename = "program_short.txt"
input_data_filename = "program.txt"

instructions = []
with open(input_data_filename, 'r') as input_file:
    for line in input_file:
        oper, modif = line.strip().split()
        modif = int(modif)
        instructions.append((oper, modif))
print(instructions)


def run(instructions, trace=True):
    pc = 0
    acc = 0
    accum_pc = []
    if trace:
        print(f"acc={acc}")
    while pc < len(instructions) and pc not in accum_pc:
        accum_pc += [pc]
        curr_inst = instructions[pc]
        oper, modif = curr_inst
        if trace:
            print(f"{pc}: {oper} {modif}", end='')

        if oper == "acc":
            acc += modif
            pc += 1
        elif oper == "jmp":
            pc += modif
        elif oper == "nop":
            pc += 1

        if trace:
            print(f" | acc={acc}")
    if pc >= len(instructions):
        if trace:
            print("Program terminated normally.")
        return 0
    else:
        if trace:
            print("Infinite loop found. Forced stop.")
            print(f"accum_pc={accum_pc}")
        return 1


# Part 1.
res = run(instructions)
print(res)


# Part 2.

i = 0
while True:
    print(f"i={i} ", end='')
    instructions_copy = instructions.copy()
    instr = instructions_copy[i]
    oper, modif = instr
    if oper == 'jmp':
        new_oper = 'nop'
        instructions_copy[i] = (new_oper, modif)
    elif oper == 'nop':
        new_oper = 'jmp'
        instructions_copy[i] = (new_oper, modif)
    else:
        print("")
        i += 1
        continue

    res = run(instructions_copy, trace=False)
    print(f"res={res}")
    if res == 0:
        break
    i += 1
print(f"END i={i}")
