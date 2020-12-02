f = open('inputDayTwo.txt')
valid = 0

for i in f:
    position = i.split()[0].split('-')
    letter = i.split()[1]
    password = i.split()[2]

    if (password[int(position[0]) - 1] == letter[0]) and (password[int(position[1]) - 1] != letter[0]):
        valid += 1
    if (password[int(position[0]) - 1] != letter[0]) and (password[int(position[1]) - 1] == letter[0]):
        valid += 1

print(valid)