import copy


def read_seats(filename):
    with open(filename) as f:
        return [list(x[0:len(x) - 1]) for x in f]


def get_occupied_adiacent_seats(seats, idx, idy):
    count = 0
    if idx > 0:
        if seats[idx - 1][idy] == '#':
            count += 1
    if idx < len(seats) - 1:
        if seats[idx + 1][idy] == '#':
            count += 1
    if idy > 0:
        if seats[idx][idy - 1] == '#':
            count += 1
    if idy < len(seats[idx]) - 1:
        if seats[idx][idy + 1] == '#':
            count += 1
    if idx > 0 and idy > 0:
        if seats[idx - 1][idy - 1] == '#':
            count += 1
    if idx < len(seats) - 1 and idy > 0:
        if seats[idx + 1][idy - 1] == '#':
            count += 1
    if idx > 0 and idy < len(seats[idx]) - 1:
        if seats[idx - 1][idy + 1] == '#':
            count += 1
    if idx < len(seats) - 1 and idy < len(seats[idx]) - 1:
        if seats[idx + 1][idy + 1] == '#':
            count += 1
    return count

def get_occupied_adiacent_seats2(seats, idx, idy):
    count = 0

    found = 0
    iidx = idx
    iidy = idy
    while iidx > 0 and found == 0:
        iidx -= 1
        if seats[iidx][iidy] == '#':
            count += 1
            found = 1
        elif seats[iidx][iidy] == 'L':
            found = 1

    found = 0
    iidx = idx
    iidy = idy
    while iidx < len(seats) - 1 and found == 0:
        iidx += 1
        if seats[iidx][iidy] == '#':
            count += 1
            found = 1
        elif seats[iidx][iidy] == 'L':
            found = 1

    found = 0
    iidx = idx
    iidy = idy
    while iidy > 0 and found == 0:
        iidy -= 1
        if seats[iidx][iidy] == '#':
            count += 1
            found = 1
        elif seats[iidx][iidy] == 'L':
            found = 1

    found = 0
    iidx = idx
    iidy = idy
    while iidy < len(seats[idx]) - 1 and found == 0:
        iidy += 1
        if seats[iidx][iidy] == '#':
            count += 1
            found = 1
        elif seats[iidx][iidy] == 'L':
            found = 1

    found = 0
    iidx = idx
    iidy = idy
    while iidx > 0 and iidy > 0 and found == 0:
        iidx -= 1
        iidy -= 1
        if seats[iidx][iidy] == '#':
            count += 1
            found = 1
        elif seats[iidx][iidy] == 'L':
            found = 1

    found = 0
    iidx = idx
    iidy = idy
    while iidx < len(seats) - 1 and iidy > 0 and found == 0:
        iidx += 1
        iidy -= 1
        if seats[iidx][iidy] == '#':
            count += 1
            found = 1
        elif seats[iidx][iidy] == 'L':
            found = 1

    found = 0
    iidx = idx
    iidy = idy
    while iidx > 0 and iidy < len(seats[idx]) - 1 and found == 0:
        iidx -= 1
        iidy += 1
        if seats[iidx][iidy] == '#':
            count += 1
            found = 1
        elif seats[iidx][iidy] == 'L':
            found = 1

    found = 0
    iidx = idx
    iidy = idy
    while iidx < len(seats) - 1 and iidy < len(seats[idx]) - 1 and found == 0:
        iidx += 1
        iidy += 1
        if seats[iidx][iidy] == '#':
            count += 1
            found = 1
        elif seats[iidx][iidy] == 'L':
            found = 1
    return count


def simulate(seats):
    changed = 1
    while changed == 1:
        changed = 0
        next_seats = copy.deepcopy(seats)
        for idx, j in enumerate(seats):
            for idy, z in enumerate(j):
                if z == 'L':
                    if get_occupied_adiacent_seats(seats, idx, idy) == 0:
                        next_seats[idx][idy] = '#'
                        changed = 1
                elif z == '#':
                    if get_occupied_adiacent_seats(seats, idx, idy) >= 4:
                        next_seats[idx][idy] = 'L'
                        changed = 1
        seats = next_seats

    return seats

def simulate2(seats):
    changed = 1
    while changed == 1:
        changed = 0
        next_seats = copy.deepcopy(seats)
        for idx, j in enumerate(seats):
            for idy, z in enumerate(j):
                if z == 'L':
                    if get_occupied_adiacent_seats2(seats, idx, idy) == 0:
                        next_seats[idx][idy] = '#'
                        changed = 1
                elif z == '#':
                    if get_occupied_adiacent_seats2(seats, idx, idy) >= 5:
                        next_seats[idx][idy] = 'L'
                        changed = 1
        seats = next_seats

    return seats


seats = read_seats('inputDayEleven.txt')
seats = simulate(seats)

counts = 0
for line in seats:
    counts += line.count('#')
print(counts)

seats = read_seats('inputDayEleven.txt')
seats = simulate2(seats)

counts = 0
for line in seats:
    counts += line.count('#')
print(counts)