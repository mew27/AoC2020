def read_file(filename):
    with open(filename) as f:
        return [int(x) for x in f]

def allowed_num(preamble):
    nums = []
    for idx, x in enumerate(preamble):
        for idy, y in enumerate(preamble[idx + 1:]):
            nums.append(x+y)
    return nums

def get_first_not_sum_num(XMAS):
    preamble = XMAS[:25]

    for num in XMAS[25:]:
        if num not in allowed_num(preamble):
            return num
        del preamble[0]
        preamble.append(num)

def get_encrypt_weakness(XMAS, weaknum):
    for idx, x in enumerate(XMAS):
        sum = x
        for idy, y in enumerate(XMAS[idx + 1:]):
            sum += y
            if sum == weaknum:
                return min(XMAS[idx:idy + idx + 1]) + max(XMAS[idx:idy + idx + 1])

XMAS = read_file('inputDayNine.txt')
weaknum = get_first_not_sum_num(XMAS)
print(weaknum)
print(get_encrypt_weakness(XMAS, weaknum))