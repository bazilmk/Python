menu = True

while menu:

    string = input('Select a character combination from M, U or I: ')
    string = string.upper()

    rule = input('Select a rule (1-4) or q to quit: ')

    for b in string:
        if b == 'M' or b == 'I' or b == 'U' in string:
            pass
        else:
            string = input('Select a character combination from M, U or I: ')
            string = string.upper()

    if rule == '1':
        if string[-1] == 'I':
            string = string + 'U'
            print(string)

    elif rule == '2':
        if string[0] == 'M':
            string = string + (string[1:])
            print(string)
            break

    elif rule == '3':
        if 'III' in string:
            pos = int(input('Enter position of III: '))
            if string[pos: pos+3] == 'III':
                string = string[:pos] + 'U' + string[pos+3:]
            print(string)

    elif rule == '4':
        if 'UU' in string:
            pos = int(input('Enter position of UU: '))
            if string[pos:pos+2] == 'UU':
                string = string[:pos] + 'I' + string[pos+2:]
            print(string)

    if rule == 'q':
        menu = False
