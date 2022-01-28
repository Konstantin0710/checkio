def find_letter(point, n, lower_grid):
    id_stop_i = len(lower_grid) - 1
    id_stop_j = len(lower_grid[0]) - 1
    i, j = point
    word = 'hypercube'
    hypercube = False
    letter = word[n]
    check_point = [[i - 1, j], [i, j - 1], [i, j + 1], [i + 1, j]]
    for p in check_point:
        a, b = p
        if 0 <= a <= id_stop_i and 0 <= b <= id_stop_j and lower_grid[a][b] == letter:
            if n < len(word) - 1:
                hypercube = find_letter(p, n + 1, lower_grid)
            else:
                return True
    return hypercube


def hypercube(grid):
    # replace this for solution
    lower_grid = list([[j.lower() for j in i] for i in grid])
    list_h = [(n, x.index('h')) for n, x in enumerate(lower_grid) if 'h' in x]
    answer = False
    for h in list_h:
        answer = find_letter(h, 1, lower_grid)
    return answer


if __name__ == '__main__':
    print("Example:")
    print(hypercube(
        [["J", "a", "t", "s", "x"],
         ["a", "s", "p", "u", "z"],
         ["a", "a", "q", "G", "f"],
         ["x", "x", "x", "N", "h"],
         ["z", "z", "z", "z", "R"]]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert hypercube([
        ['g', 'f', 'H', 'Y', 'v'],
        ['z', 'e', 'a', 'P', 'u'],
        ['s', 'B', 'T', 'e', 'y'],
        ['k', 'u', 'c', 'R', 't'],
        ['l', 'O', 'k', 'p', 'r']]) == True
    assert hypercube([
        ['H', 'a', 't', 's', 'E'],
        ['a', 'Y', 'p', 'u', 'B'],
        ['a', 'a', 'P', 'y', 'U'],
        ['x', 'x', 'x', 'E', 'C'],
        ['z', 'z', 'z', 'z', 'R']]) == False
    assert hypercube(
        [["J", "a", "t", "s", "x"],
         ["a", "s", "p", "u", "z"],
         ["a", "a", "q", "G", "f"],
         ["x", "x", "x", "N", "h"],
         ["z", "z", "z", "z", "R"]]) == False
    # print("Coding complete? Click 'Check' to earn cool rewards!")
