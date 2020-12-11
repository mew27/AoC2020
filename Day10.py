def read_file(filename):
    with open(filename) as f:
        return [int(x) for x in f]


def get_extra_adapter(adapter_list):
    return max(adapter_list) + 3


def get_usable_adapers(jolt, adapter_list):
    usable_adapters = []
    for adapter in adapter_list:
        if adapter > jolt and adapter - jolt <= 3:
            usable_adapters.append(adapter)
    return usable_adapters


def get_jolt_chain(adapter_list):
    remaining_adapters = adapter_list.copy()
    remaining_adapters.append(get_extra_adapter(adapter_list))
    difference_list = []
    jolt = 0
    while remaining_adapters:
        usable_adapters = get_usable_adapers(jolt, remaining_adapters)
        adapter = min(usable_adapters)
        difference_list.append(adapter - jolt)
        jolt = adapter
        remaining_adapters.remove(adapter)
    return difference_list


def get_jolt_differences(difference_list):
    diff_1 = 0
    diff_3 = 0

    for diff in difference_list:
        if diff == 1:
            diff_1 += 1
        elif diff == 3:
            diff_3 += 1
    return diff_1, diff_3


def get_combinations(adapter_list):
    total_adapters = adapter_list.copy()
    total_adapters.append(get_extra_adapter(adapter_list))
    total_adapters.sort()
    total_adapters.insert(0, 0)
    total_comb = 1
    diff_list = []
    for id, adapter in enumerate(total_adapters[1:len(total_adapters)], 1):
        diff_list.append(adapter - total_adapters[id - 1])
    cont_ones = 0
    for diff in diff_list:
        if diff == 1:
            cont_ones += 1
        elif diff == 3:
            if cont_ones == 2:
                total_comb *= 2
            elif cont_ones == 3:
                total_comb *= 4
            elif cont_ones == 4:
                total_comb *= 7
            cont_ones = 0

    return total_comb

    print(total_adapters)

adapter_list = read_file('inputDayTen.txt')
jolt_diff1, jolt_diff2 = get_jolt_differences(get_jolt_chain(adapter_list))
print(jolt_diff1 * jolt_diff2)
comb = get_combinations(adapter_list)
print(comb)
