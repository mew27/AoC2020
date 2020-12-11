def read_input(filename):
    with open(filename) as f:
        group_list = [];
        group = {'n_group': 0}
        for x in f:
            if x == '\n':
                group_list.append(group)
                group = {'n_group': 0}
            else:
                for l in x:
                    if l != ' ' and l != '\n':
                        if l in group:
                            group[l] += 1
                        else:
                            group[l] = 1
                    elif l == '\n':
                        group['n_group'] += 1
        return group_list


group_list = read_input('inputDaySix.txt')

count = 0
for group in group_list:
    for key in group:
        if group[key] == group['n_group'] and key != 'n_group':
            count += 1

print(count)