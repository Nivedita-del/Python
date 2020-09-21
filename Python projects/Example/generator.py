def fun():
    a = 1
    print("1")
    yield a

    a +=1
    print("2")
    yield a

    a +=1
    print("2")
    yield a

    a +=1
    print("2")
    yield a

for num in fun():
    print(num)
    
