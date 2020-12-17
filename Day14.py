def read_file(filename):
    with open(filename) as f:
        istructions = []
        l = [x.split() for x in f]

        for ll in l:
            if ll[0] == 'mask':
                istructions.append((ll[0], ll[2]))
            elif ll[0].__contains__('mem'):
                istructions.append((ll[0][2], ll[0][4:len(ll[0]) - 1], int(ll[2])))

    return istructions


def write_mem(istruction):
    mem = {}
    mask_or = 0
    mask_and = 0
    for istruction in istructions:
        if istruction[0] == 'mask':
            mask_or = int(istruction[1].replace('X', '0'), 2)
            mask_and = int(istruction[1].replace('X', '1'), 2)
        elif istruction[0] == 'm':
            mem[istruction[1]] = (istruction[2] & mask_and) | mask_or

    return mem


def return_adresses(string):
    adress_list = []
    for x in list(string):
        if x == 'X':
            adress_list.extend(return_adresses(string.replace('X', '0', 1)))
            adress_list.extend(return_adresses(string.replace('X', '1', 1)))
            break

    if adress_list == []:
        adress_list = [int(string, 2)]

    return adress_list

def write_mem_dec2(istructions):
    mem = {}
    address_list = []
    mask = ''
    for instruction in istructions:
        if instruction[0] == 'mask':
            mask = instruction[1]
        elif instruction[0] == 'm':
            address_list = return_adresses(decode_address( list(str(bin(int(instruction[1])))[2:].zfill(36)), list(mask)))
            for address in address_list:
                mem[address] = (instruction[2])

    return mem

def decode_address(adrress, mask):
    for idx, i in enumerate(mask, 0):
        if i == 'X' or i == '1':
            adrress[idx] = i

    return ''.join(adrress)

istructions = read_file('inputDayFourteen.txt')
mem = write_mem(istructions)
print(sum(mem.values()))
mem = write_mem_dec2(istructions)
print(sum(mem.values()))