def read_input(filename):
    with open('inputDayTwelve.txt') as f:
        return [(x[0], int(x[1:len(x)-1])) for x in f]

def travel(actions):
    forward_dir = 1
    pos_n = 0
    pos_e = 0
    for action in actions:
        if action[0] == 'N':
            pos_n += action[1]
        elif action[0] == 'S':
            pos_n -= action[1]
        elif action[0] == 'E':
            pos_e += action[1]
        elif action[0] == 'W':
            pos_e -= action[1]
        elif action[0] == 'L':
            forward_dir -= action[1] / 90
            forward_dir %= 4
        elif action[0] == 'R':
            forward_dir += action[1] / 90
            forward_dir %= 4
        elif action[0] == 'F':
            if forward_dir == 0:
                pos_n += action[1]
            elif forward_dir == 1:
                pos_e += action[1]
            elif forward_dir == 2:
                pos_n -= action[1]
            elif forward_dir == 3:
                pos_e -= action[1]
    return pos_n, pos_e

def travel_waypoint(actions):
    ship_pos = 0
    waypoint = 10 + 1j

    for action in actions:
        if action[0] == 'N':
            waypoint += action[1]*1j
        elif action[0] == 'S':
            waypoint -= action[1]*1j
        elif action[0] == 'E':
            waypoint += action[1]
        elif action[0] == 'W':
            waypoint -= action[1]
        elif action[0] == 'L':
            waypoint *= 1j**(action[1] / 90)
        elif action[0] == 'R':
            waypoint /= 1j**(action[1] / 90)
        elif action[0] == 'F':
            ship_pos += action[1] * waypoint

    return ship_pos

instructions = read_input('inputDayTwelve.txt')
cord = travel(instructions)
print(abs(cord[0]) + abs(cord[1]))
ship_pos = travel_waypoint(instructions)
print(abs(ship_pos.real) + abs(ship_pos.imag))
