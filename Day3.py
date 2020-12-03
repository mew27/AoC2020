def read_map(filename):
    with open(filename) as f:
        return [list(x) for x in f]


    f.close()

X = read_map('inputDayThree.txt')

for f in X:
    del f[len(f) - 1]

slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
tree_mul = 1

for slope in slopes:
    print(slope)
    pos_x = 0
    pos_y = 0
    n_tree = 0
    while pos_y < len(X):
        if X [pos_y % len(X)] [pos_x % len(X[0])] == '#':
            n_tree += 1
        pos_y += slope[0]
        pos_x += slope[1]
    print(n_tree)
    tree_mul *= n_tree

print(tree_mul)