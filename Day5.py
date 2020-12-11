def read_file(filename):
    with open(filename) as f:
        X = []
        for x in f:
            X.append([x[0:7], x[7:10]])
        return X


def get_binary(board, r_o_c):
    val = 0
    if r_o_c == 'row':
        for idx, x in enumerate(board, 0):
            if x == 'B':
                val += 2 ** (6 - idx)
    elif r_o_c == 'column':
        for idx, x in enumerate(board, 0):
            if x == 'R':
                val += 2 ** (2 - idx)

    return val

def get_id(board):
    return get_binary(board[0], 'row') * 8 + get_binary(board[1], 'column')

def get_max_id(boardList):
    max_id = 0
    for board in boardList:
        id = get_id(board)
        # print(board, get_binary(board[0], 'row'), get_binary(board[1], 'column'), id)
        if id > max_id:
            max_id = id
    return max_id

def get_your_seat(boardList):
    boardList.sort(key=get_id)
    for idx, x in enumerate(boardList):
        if get_id(boardList[idx + 1]) != get_id(x) + 1:
            return get_id(x) + 1

X = read_file('inputDayFive.txt')
print(get_max_id(X))
print(get_your_seat(X))