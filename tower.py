def rotate_cube(cube):
    t = '1324|56'

    list_rot_cube = [cube,
                     f'{cube[1]}{cube[2]}{cube[3]}{cube[0]}{cube[4]}{cube[5]}',
                     f'{cube[2]}{cube[3]}{cube[0]}{cube[1]}{cube[4]}{cube[5]}',
                     f'{cube[3]}{cube[0]}{cube[1]}{cube[2]}{cube[4]}{cube[5]}',

                     f'{cube[5]}{cube[1]}{cube[2]}{cube[4]}{cube[0]}{cube[3]}',
                     f'{cube[1]}{cube[2]}{cube[4]}{cube[5]}{cube[0]}{cube[3]}',
                     f'{cube[2]}{cube[4]}{cube[5]}{cube[1]}{cube[0]}{cube[3]}',
                     f'{cube[4]}{cube[5]}{cube[1]}{cube[2]}{cube[0]}{cube[3]}',

                     f'{cube[3]}{cube[1]}{cube[2]}{cube[0]}{cube[5]}{cube[4]}',
                     f'{cube[1]}{cube[2]}{cube[0]}{cube[3]}{cube[5]}{cube[4]}',
                     f'{cube[2]}{cube[0]}{cube[3]}{cube[1]}{cube[5]}{cube[4]}',
                     f'{cube[0]}{cube[3]}{cube[1]}{cube[2]}{cube[5]}{cube[4]}',

                     f'{cube[4]}{cube[1]}{cube[2]}{cube[5]}{cube[3]}{cube[0]}',
                     f'{cube[1]}{cube[2]}{cube[5]}{cube[4]}{cube[3]}{cube[0]}',
                     f'{cube[2]}{cube[5]}{cube[4]}{cube[1]}{cube[3]}{cube[0]}',
                     f'{cube[5]}{cube[4]}{cube[1]}{cube[2]}{cube[3]}{cube[0]}',

                     f'{cube[4]}{cube[0]}{cube[3]}{cube[5]}{cube[1]}{cube[2]}',
                     f'{cube[0]}{cube[3]}{cube[5]}{cube[4]}{cube[1]}{cube[2]}',
                     f'{cube[3]}{cube[5]}{cube[4]}{cube[0]}{cube[1]}{cube[2]}',
                     f'{cube[5]}{cube[4]}{cube[0]}{cube[3]}{cube[1]}{cube[2]}',

                     f'{cube[4]}{cube[3]}{cube[0]}{cube[5]}{cube[2]}{cube[1]}',
                     f'{cube[3]}{cube[0]}{cube[5]}{cube[4]}{cube[2]}{cube[1]}',
                     f'{cube[0]}{cube[5]}{cube[4]}{cube[3]}{cube[2]}{cube[1]}',
                     f'{cube[5]}{cube[4]}{cube[3]}{cube[0]}{cube[2]}{cube[1]}',

                     ]

    list_rot_cube2 = [cube[:4],
                      f'{cube[1]}{cube[2]}{cube[3]}{cube[0]}',
                      f'{cube[2]}{cube[3]}{cube[0]}{cube[1]}',
                      f'{cube[3]}{cube[0]}{cube[1]}{cube[2]}',

                      f'{cube[5]}{cube[1]}{cube[2]}{cube[4]}',
                      f'{cube[1]}{cube[2]}{cube[4]}{cube[5]}',
                      f'{cube[2]}{cube[4]}{cube[5]}{cube[1]}',
                      f'{cube[4]}{cube[5]}{cube[1]}{cube[2]}',

                      f'{cube[3]}{cube[1]}{cube[2]}{cube[0]}',
                      f'{cube[1]}{cube[2]}{cube[0]}{cube[3]}',
                      f'{cube[2]}{cube[0]}{cube[3]}{cube[1]}',
                      f'{cube[0]}{cube[3]}{cube[1]}{cube[2]}',

                      f'{cube[4]}{cube[1]}{cube[2]}{cube[5]}',
                      f'{cube[1]}{cube[2]}{cube[5]}{cube[4]}',
                      f'{cube[2]}{cube[5]}{cube[4]}{cube[1]}',
                      f'{cube[5]}{cube[4]}{cube[1]}{cube[2]}',

                      f'{cube[4]}{cube[0]}{cube[3]}{cube[5]}',
                      f'{cube[0]}{cube[3]}{cube[5]}{cube[4]}',
                      f'{cube[3]}{cube[5]}{cube[4]}{cube[0]}',
                      f'{cube[5]}{cube[4]}{cube[0]}{cube[3]}',

                      f'{cube[4]}{cube[3]}{cube[0]}{cube[5]}',
                      f'{cube[3]}{cube[0]}{cube[5]}{cube[4]}',
                      f'{cube[0]}{cube[5]}{cube[4]}{cube[3]}',
                      f'{cube[5]}{cube[4]}{cube[3]}{cube[0]}',

                      ]
    # tlist = ['1234|56', '2341', '3412','4123'
    #          '6235|14', '2356', '3562', '5623'
    #          '4231|65', '2314', '3142', '1423'
    #          '5236|41', '2365', '3652', '6523'
    #
    #          '5146|23', '1465', '4651', '6514'
    #          '5416|32', '4165', '1654', '6541']
    return set(list_rot_cube2)


def tower(cubes):
    # replace this for solution
    list_cubes = list(map(rotate_cube, cubes))
    list_tower = list()
    for i, cube1 in enumerate(list_cubes):
        d = 1
        for j, cube2 in enumerate(list_cubes):
            if i != j:
                y = cube1 & cube2
                if cube1 & cube2:
                    d += 1
        list_tower.append(d)

    return max(list_tower)

if __name__ == '__main__':
    print("Example:")
    print(tower(['GYVABW', 'AOCGYV', 'CABVGO', 'OVYWGA']))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert tower(['GYVABW', 'AOCGYV', 'CABVGO', 'OVYWGA']) == 3
    # assert tower(['ABCGYW', 'CAYRGO', 'OCYWBA', 'ACYVBR', 'GYVABW']) == 1
    # assert tower(['GYCABW', 'GYCABW', 'GYCABW', 'GYCABW', 'GYCABW']) == 5
    # print("Coding complete? Click 'Check' to earn cool rewards!")
