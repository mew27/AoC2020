import re

def listToDict(lst):
    op = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return op

def read_passports(filename):
    y = []
    z = ''
    with open(filename) as f:
       for x in f:
           if x == '\n':
                y.append(z)
                z = ''
           else:
               z = z + ' ' + x[0:len(x)-1];
    Y = []
    for x in y:
        yy = []
        for z in x.split():
            yy = yy + z.split(':')
        Y.append(yy)

    passportsList = []
    for x in Y:
        passportsList.append(listToDict(x))
    return passportsList

passportsList = read_passports('inputDayFour.txt')

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

num_valid = 0


def check_valid(passport, field):
        return True


for passport in passportsList:
    num_fields = 0
    valid_fields = 0

    for field in fields:
        if check_valid(passport, field):
            valid_fields += 1

        if field in passport:
            num_fields += 1

    if num_fields == len(fields) and valid_fields == len(fields):
        num_valid += 1

print(num_valid)
