def isometric_strings(a, b):
    # your code here
    if len(a) == len(b):
        d = dict()
        for a1, b1 in zip(a, b):
            d[a1] = b1
    l = list(d[i] for i in a)
    return l == list(b)



if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("add", "egg"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings("add", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    assert isometric_strings("gogopy", "doodle") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
