def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]
    f.close()

a = read_integers("inputDayOne.txt")

for i,val_i in enumerate(a):
    for j, val_j in enumerate(a[i:len(a)]):
        for k, val_k in enumerate(a[j:len(a)]):
            if val_i + val_j + val_k == 2020:
                print("Il valore è", val_i*val_j*val_k)