def read_input(filename):
    with open(filename) as f:
        rules = {}
        for x in f:
            rule = {}
            splitted = x.split()
            if len(splitted[4:]) // 4 != 0:
                for i in range(0, len(splitted[4:]) // 4):
                    rule[splitted[4 + 4 * i + 1] + ' ' + splitted[4 + 4 * i + 2]] = int(splitted[4 + 4 * i])
            rules[splitted[0] + ' ' + splitted[1]] = rule
    return rules


def count_shiny_gold(rules, rule):
    if rule == 'shiny gold':
        return 1
    else:
        subrules = rules[rule]
        for subrule in subrules.keys():
            if count_shiny_gold(rules, subrule) == 1:
                return 1
        return 0


def count_sub_bags(rules, rule):
    n_bags = 0
    for subrule in rules[rule]:
        n_bags += rules[rule][subrule] * count_sub_bags(rules, subrule)
    return n_bags + 1


rules = read_input('inputDaySeven.txt')
count = 0

for rule in rules:
    if rule != 'shiny gold':
        count += count_shiny_gold(rules, rule)
print(count)
print(count_sub_bags(rules, 'shiny gold') - 1)
