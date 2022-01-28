def safe_pawns(pawns: set) -> int:
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    safe = 0
    for pawn in pawns:
        letter, number = list(pawn)
        number_protection = int(number) - 1
        index_first_letter_protect = abc.index(letter) - 1 if abc.index(letter) - 1 >= 0 else None
        index_second_letter_protect = abc.index(letter) + 1 if abc.index(letter) + 1 <= 7 else None
        l1 = f'{abc[index_first_letter_protect]}{number_protection}' if index_first_letter_protect is not None else None
        l2 = f'{abc[index_second_letter_protect]}{number_protection}' if index_second_letter_protect else None
        if l1 in pawns or l2 in pawns:
            safe += 1

    return safe


files = 'abcdefgh?'  # an extra character for h-pawns to check; they won't find it


def safe_pawns2(pawns: set) -> int:
    # a pawn is safe if there is another pawn to the lower left or lower right
    # i.e. rank (number) - 1 and file (letter) +/- 1
    safe = 0
    for pawn in pawns:
        good_rank = str(int(pawn[1]) - 1)  # convert rank to int, subtract 1, then convert back to string
        file_index = files.find(pawn[0])  # essentially convert the letter to a number
        good_files = (files[file_index - 1], files[file_index + 1])  # then use that number to find two more letters
        p1 = good_files[0] + good_rank
        p2 = good_files[1] + good_rank
        if p1 in pawns or p2 in pawns:
            safe += 1
    return safe


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(safe_pawns(["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"]))
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
