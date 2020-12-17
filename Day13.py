def read_file(filename):
    with open(filename) as f:
        list = [x.split(',') for x in f]
    ll = []
    for idx, l in enumerate(list[1], 0):
        if l != 'x':
            ll.append(int(list[1][idx]))
    return (int(list[0][0]), ll)


def read_with_x(filename):
    with open(filename) as f:
        list = [x.split(',') for x in f]
    ll = []
    for idx, l in enumerate(list[1], 0):
        if l != 'x':
            ll.append(int(list[1][idx]))
        else:
            ll.append(list[1][idx])
    return (int(list[0][0]), ll)


def get_bus(times):
    l = [x - times[0] % x for x in times[1]]
    return min(l) * times[1][l.index(min(l))]


times = read_file('inputDayThirteen.txt')
print(get_bus(times))

times_with_x = read_with_x('inputDayThirteen.txt')
mult = 1
for i in times_with_x[1]:
    if i != 'x':
        mult *= i

bus_id = [times_with_x[1][0]]
remainders = [0]
plus_rem = 1
for time in times_with_x[1][1:]:
    if time != 'x':
        bus_id.append(time)
        remainders.append((time - plus_rem)%time)
    plus_rem += 1

cycle = max(bus_id)
remaining = bus_id.copy()
remaining.remove(cycle)
i = remainders[bus_id.index(max(bus_id))]
del remainders[bus_id.index(max(bus_id))]

count = 0
while i < mult and remaining != []:
    i += cycle
    count += 1
    for idx, x in enumerate([i % z for z in remaining]):
        if x == remainders[idx]:
            cycle *= remaining[idx]
            del remaining[idx]
            del remainders[idx]
            break

    if count % 1000 == 0:
            print('Iterazione ', count, ' dimensione rimanenti ', len(remaining))
print(i)
