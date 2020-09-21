a = [2,3,4]
b = iter(a)

print(next(b))
print(next(b))

print(b.__next__())

next(b)
