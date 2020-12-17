import copy


def read_file(filename):
    with open(filename) as f:
        count = 0
        rules = []
        fields = []
        myticket = []
        for x in f:
            count += 1
            if count < 21:
                l = x.split()
                if l[0] == 'departure' or l[0] == 'arrival':
                    rules.append((l[2], l[4]))
                else:
                    rules.append((l[1], l[3]))
            if count == 23:
                myticket.extend([int(z) for z in x.split(',')])

            if count >= 26:
                subfield = []
                for z in x.split(','):
                    subfield.append(int(z))
                fields.append(subfield)
    return rules, fields, myticket


def get_invalid_sum(rules, fields):
    invalid_count = 0
    v_fields = copy.deepcopy(fields)

    for ticket in fields:
        for field in ticket:
            invalid = True
            for rule in rules:
                a1 = int(rule[0].split('-')[0])
                b1 = int(rule[0].split('-')[1])
                a2 = int(rule[1].split('-')[0])
                b2 = int(rule[1].split('-')[1])

                if (a1 <= field <= b1) or (a2 <= field <= b2):
                    invalid = False
                    break
            if invalid:
                invalid_count += field

    return invalid_count


def remove_invalid(rules, fields):
    invalid_count = 0
    v_fields = copy.deepcopy(fields)

    for ticket in fields:
        for field in ticket:
            invalid = True
            for rule in rules:
                a1 = int(rule[0].split('-')[0])
                b1 = int(rule[0].split('-')[1])
                a2 = int(rule[1].split('-')[0])
                b2 = int(rule[1].split('-')[1])

                if (a1 <= field <= b1) or (a2 <= field <= b2):
                    invalid = False
                    break
            if invalid:
                v_fields.remove(ticket)
                invalid_count += field
                break

    return v_fields


def get_fields(rules, valid_tickets):
    order_field = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    count = 0
    for rule in rules:
        a1 = int(rule[0].split('-')[0])
        b1 = int(rule[0].split('-')[1])
        a2 = int(rule[1].split('-')[0])
        b2 = int(rule[1].split('-')[1])

        for i in range(0, len(valid_tickets[0])):
            invalid = False
            for j in range(0, len(valid_tickets)):
                if (valid_tickets[j][i] < a1 or valid_tickets[j][i] > b1) and (
                        valid_tickets[j][i] < a2 or valid_tickets[j][i] > b2):
                    invalid = True
                    break
            if not invalid:
                order_field[count].append(i + 1)
        count += 1
    return order_field


def guess(order_field):
    guess_fields = [[idx, x] for idx, x in enumerate(order_field)]
    guess_fields.sort(key=lambda x: len(x[1]))

    for i in range(0, len(guess_fields) - 1):
        for field in guess_fields[i + 1:]:
            field[1] = [x for x in field[1] if x not in guess_fields[i][1]]

    guess_fields.sort(key=lambda x: x[0])

    return [x[1][0] for x in guess_fields]


rules, fields, myticket = read_file('inputDaySixteen.txt')
# print(rules, fields)
print(get_invalid_sum(rules, fields))
valid_tickets = remove_invalid(rules, fields)
# print(valid_tickets)
order_fields = get_fields(rules, valid_tickets)
guess_fields = guess(order_fields)
ordered_list = [myticket[i - 1] for i in guess_fields]
mul = 1
for i in ordered_list[:6]:
    mul *= i
print(mul)
