def buttons(ceiling):
    # replace this for solution
    l = ceiling[1:].split('\n')
    l2 = list([list(i) for i in l])
    d = list()
    r = list()
    for i in range(len(l2)):
        q = list()
        for j in range(len(l2[i])):
            num = int(l2[i][j])
            if num != 0:
                q.append(num)
            else:
                if q:
                    d.append(q)
                q = list()
        else:
            if q:
                d.append(q)
            r.append(d)
            d = list()


    print(r)
    return 0


if __name__ == '__main__':
    print("Example:")
    print(buttons('''
001203
023001
100220'''))
#
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert buttons('''
# 001203
# 023001
# 100220''') == [8, 4, 4, 1]
#
#     assert buttons('''
# 000000
# 000055
# 000055''') == [20]
#
#     assert buttons('''
# 908070
# 060504
# 302010''') == [9, 8, 7, 6, 5, 4, 3, 2, 1]
#     print("Coding complete? Click 'Check' to earn cool rewards!")
