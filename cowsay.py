COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


def cowsay(text):
    while text.find('  ') != -1:
        text = text.replace('  ', ' ')
    if len(text) < 40:
        len_str1 = len(text)
        top = f' {"_" * (len_str1 + 2)}'
        bot = f' {"-" * (len_str1 + 2)}'
        t7 = f'< {text} >'
        t8 = '\n'.join([top, t7, bot])
        return rf'''
{t8}
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    list_text = list()
    while text:
        if len(text) >= 40:
            t = text[:40]
            n = t.rfind(' ') if t.rfind(' ') != -1 else 39
            t = t[:n].strip()
            list_text.append(t)
            text = text[len(t):].strip()
        else:
            list_text.append(text)
            text = None
    len_str = len(max(list_text, key=lambda x: len(x)))
    first_line = f"/ {list_text[0].ljust(len_str, ' ')} \\"
    last_line = f"\\ {list_text[-1].strip().ljust(len_str, ' ')} /"
    list_middle_lines = list()
    for i in list_text[1:-1]:
        list_middle_lines.append(f"| {i.ljust(len_str, ' ')} |")
        print(len(f"{i.ljust(len_str, ' ')}"))
        print(len_str)
    top = f' {"_"* (len_str+2)}'
    bot = f' {"-" * (len_str+2)}'
    middle_lines = '\n'.join(list_middle_lines)
    strings = '\n'.join([top, first_line, middle_lines, last_line, bot]) if middle_lines else '\n'.join([top, first_line, last_line, bot])
    return rf'''
{strings}
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines


    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                                'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    print(expected_cowsay_many_lines)
    print(cowsay_many_lines)
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
