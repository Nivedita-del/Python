def strrev(str):
    reverse = ''.join(reversed(str))

    if (str == reverse):
        return True
    return False

str = "madam"
st = strrev(str)

if (st):
    print ("yeah it can be reversed")
else:ok
    print ("are you insane")


def sub(val1, val2):
    b = val1 - val2
    print(b)


def mul(val1, val2):
    c = val1 * val2
    print(c)


def div(val1, val2):
    d = val1 / val2
    print(d)