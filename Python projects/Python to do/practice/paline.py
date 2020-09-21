import numpy

def pal(str):
    strlen = len(str)
    for i in range (0, strlen):
        if str[i] != str[strlen-i-1]:
            return False
    return True

str = "madam"
strrev = pal(str)

if(strrev):
    print("its a panlidrom")
else:
        print("no it is not")

elif c == 'sub':
    sub(a,b)
elif c == 'mul':
    mul(a,b)
elif c == 'div':
    div(a,b)