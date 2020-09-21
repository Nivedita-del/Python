def pretty(fufu):
    def inner():
        print(" got makeuped")
        fufu()
    return inner
def order():
    print(" just woke up")
