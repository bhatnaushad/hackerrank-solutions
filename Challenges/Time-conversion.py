def timeConversion(s):
    # 07:05:45PM
    # 0123456789

    initial = s[0:2]
    last = s[-2:]

    new_str = ''

    if last == 'AM':
        if initial == '12':
            new_str = '00'+s[2:-2]
        else:
            new_str = s[0:-2]

    elif last == "PM":
        if initial == '12':
            new_str = '12'+s[2:-2]
        else:
            x = int(initial)
            x += 12

            new_str = str(x) + s[2:8]
    else:
        assert False
    return new_str


input = input().strip()

print(timeConversion(input))


