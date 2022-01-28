def split_pairs(a):
    # your code here
    lop = list([f'{a[i-1]}{a[i]}' for i in range(1, len(a), 2)])
    if len(a)% 2:
        lop.append(f'{a[-1]}_')

    return lop


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcdf')))

    # # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
