def read_starting_numbers(filename):
    with open(filename) as f:
        return [int(y) for y in [x.split(',') for x in f][0]]


def play(numbers, n):
    count = len(numbers)
    spoken_nums = {}
    last_spoken = numbers[len(numbers) - 1]
    last_spoken_turn = len(numbers)

    for idx, num in enumerate(numbers[0:len(numbers) - 1], 1):
        spoken_nums[num] = idx

    while count < n:
        count += 1
        if last_spoken not in spoken_nums:
            spoken_nums[last_spoken] = last_spoken_turn
            last_spoken = 0
            last_spoken_turn = count
        else:
            tmp = last_spoken_turn - spoken_nums[last_spoken]
            spoken_nums[last_spoken] = last_spoken_turn
            last_spoken = tmp
            last_spoken_turn = count

    return last_spoken


num = read_starting_numbers('inputDayFifteen.txt')
print(play(num, 2020))
print(play(num, 30000000))
