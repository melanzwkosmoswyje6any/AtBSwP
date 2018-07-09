grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def rowtocol(grid1):
    # Nr of elements of inner list eg 0 - 6 -> 5 times
    for i in range(len(grid1[0])):
        # Nr of elements of outer list eg 0 - 9 -> 8 times
        for j in range(len(grid1)):
            print(grid1[j][i], end='')
        print('')
            # a[i2][i1] = grid1[i1][i2]
    # print(a)


rowtocol(grid)