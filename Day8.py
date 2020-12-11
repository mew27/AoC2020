def load_code(filename):
    with open(filename) as f:
        code = []
        for x in f:
            # print(x.split())
            code.append([x.split(), 0])
        return code

def has_terminated(code):
    acc = 0
    pc = -1
    while True:
        if pc + 1 > len(code):
            return acc, False
        elif pc + 1 == len(code):
            return acc, True
        pc += 1
        instruction = code[pc]
        opcode = instruction[0]
        n_exec = instruction[1]

        if n_exec > 0:
            return acc, False
        else:
            if opcode[0] == 'acc':
                acc += int(opcode[1])
            elif opcode[0] == 'jmp':
                pc += int(opcode[1]) - 1
        instruction[1] += 1

def check_corupted(code):
    for instruction in code:
        if instruction[0][0] == 'jmp':
            instruction[0][0] = 'nop'
            acc, terminated = has_terminated(code)
            if terminated:
                return acc
            else:
                instruction[0][0] = 'jmp'
        elif instruction[0][0] == 'nop':
            instruction[0][0] = 'jmp'
            acc, terminated = has_terminated(code)
            if terminated:
                return acc
            else:
                instruction[0][0] = 'nop'
        for instruction_n in code:
            instruction_n[1] = 0


code = load_code('inputDayEight.txt')
print(has_terminated(code))

for instruction_n in code:
    instruction_n[1] = 0

acc = check_corupted(code)
print(acc)