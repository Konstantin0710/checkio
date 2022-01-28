from copy import deepcopy


def make_list(grid, i, j, check_path, n, list_make):
    id_stop_i = len(grid) - 1
    id_stop_j = len(grid[0]) - 1
    list_make2 = deepcopy(list_make)
    if 0 <= i <= id_stop_i and 0 <= j <= id_stop_j:
        list_make2.append([i, j])
        n -= 1

        if i == id_stop_i and j == id_stop_j and n == 0:
            check_path.append(list_make2)

        check_p = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j - 1], [i, j + 1], [i + 1, j - 1], [i + 1, j],
                   [i + 1, j + 1]]
        for a, b in check_p:
            if n > 0:
                if [a, b] not in list_make2 and (0 <= a <= id_stop_i and 0 <= b <= id_stop_j):
                    make_list(grid, a, b, check_path, n, list_make2)
    return check_path


def g_key(grid, path):
    n = path
    row = len(grid)
    column = len(grid[0])

    # special case
    if path == row*column:
        temp = 0
        for i in grid:
            temp += sum(i)
        return temp
    a = max(make_list(grid, 0, 0, [], n, []), key=lambda x: sum(grid[i][j] for i, j in x))
    return sum(grid[i][j] for i, j in a)


if __name__ == '__main__':
    print("Example:")
    print(g_key([[2, 5, 4, 1, 8],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 1]], 6))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert g_key([[1, 6, 7, 2, 4],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 0]], 9) == 46
    # #
    assert g_key([[2, 5, 4, 1, 8],
                  [0, 4, 9, 5, 3],
                  [7, 2, 5, 1, 4],
                  [3, 3, 2, 2, 9],
                  [2, 6, 1, 4, 1]], 6) == 27
    # #
    assert g_key([[1, 2, 3, 4, 5],
                  [2, 3, 4, 5, 1],
                  [3, 4, 5, 1, 2],
                  [4, 5, 1, 2, 3],
                  [5, 1, 2, 3, 4]], 25) == 75
    # #
    assert g_key([[1, 6],
                  [5, 1]], 2) == 2

    print("Coding complete? Click 'Check' to earn cool rewards!")
