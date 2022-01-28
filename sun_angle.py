from typing import Union


def sun_angle(time: str) -> Union[float, str]:
    # replace this for solution
    h, m = time.split(':')
    if float(f'{h}.{m}') < 6 or float(f'{h}.{m}') > 18:
        return "I don't see the sun!"
    return (int(h) - 6) * 15 + int(m) * 0.25


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")