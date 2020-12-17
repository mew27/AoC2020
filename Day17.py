import copy


def read_file(filename):
    with open(filename) as f:
        valid_coord = []
        x = 0
        y = 0
        for q in f:
            for j in q:
                if j == '#':
                    valid_coord.append([x, y, 0])
                y += 1
            x += 1
            y = 0
    return valid_coord


def simulate(cubes, round):

    for i in range(0, round):
        next_cubes = copy.deepcopy(cubes)

        x_min = min([x[0] for x in cubes]) - 1
        x_max = max([x[0] for x in cubes]) + 1

        y_min = min([x[1] for x in cubes]) - 1
        y_max = max([x[1] for x in cubes]) + 1

        z_min = min([x[2] for x in cubes]) - 1
        z_max = max([x[2] for x in cubes]) + 1

        for k in range(z_min, z_max + 1):
            for i in range(x_min, x_max + 1):
                for j in range(y_min, y_max + 1):
                    if [i, j, k] not in cubes:
                        neighbor = [x for x in cubes if abs(x[0] - i) <= 1 and abs(x[1] - j) <= 1 and abs(x[2] - k) <= 1]
                        if len(neighbor) == 3:
                            next_cubes.append([i, j, k])
                    else:
                        neighbor = [x for x in cubes if abs(x[0] - i) <= 1 and abs(x[1] - j) <= 1 and abs(x[2] - k) <= 1 and x != [i, j, k]]
                        if len(neighbor) < 2 or len(neighbor) > 3:
                            next_cubes.remove([i, j, k])
        cubes = next_cubes
    return cubes

def read_file4d(filename):
    with open(filename) as f:
        valid_coord = []
        x = 0
        y = 0
        for q in f:
            for j in q:
                if j == '#':
                    valid_coord.append([x, y, 0, 0])
                y += 1
            x += 1
            y = 0
    return valid_coord

def simulate4d(cubes, round):

    for i in range(0, round):
        next_cubes = copy.deepcopy(cubes)

        x_min = min([x[0] for x in cubes]) - 1
        x_max = max([x[0] for x in cubes]) + 1

        y_min = min([x[1] for x in cubes]) - 1
        y_max = max([x[1] for x in cubes]) + 1

        z_min = min([x[2] for x in cubes]) - 1
        z_max = max([x[2] for x in cubes]) + 1

        w_min = min([x[3] for x in cubes]) - 1
        w_max = max([x[3] for x in cubes]) + 1

        for w in range(w_min, w_max + 1):
            for k in range(z_min, z_max + 1):
                for i in range(x_min, x_max + 1):
                    for j in range(y_min, y_max + 1):
                        if [i, j, k, w] not in cubes:
                            neighbor = [x for x in cubes if abs(x[0] - i) <= 1 and abs(x[1] - j) <= 1 and abs(x[2] - k) <= 1 and abs(x[3] - w) <= 1]
                            if len(neighbor) == 3:
                                next_cubes.append([i, j, k, w])
                        else:
                            neighbor = [x for x in cubes if abs(x[0] - i) <= 1 and abs(x[1] - j) <= 1 and abs(x[2] - k) <= 1 and abs(x[3] - w) <= 1 and x != [i, j, k, w]]
                            if len(neighbor) < 2 or len(neighbor) > 3:
                                next_cubes.remove([i, j, k, w])
        cubes = next_cubes
    return cubes


cubes = read_file('inputDaySeventeen.txt')
print(len(simulate(cubes, 6)))
cubes = read_file4d('inputDaySeventeen.txt')
print(len(simulate4d(cubes, 6)))
