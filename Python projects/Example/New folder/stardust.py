def star(fun):
    def outer(*args, **kwargs):
        print("$"* 100)
        fun(*args, **kwargs)
        print("$"*100)
    return outer


def dust(fun):
    def outer(*args, **kwargs):
        print("{}"* 100)
        fun(*args, **kwargs)
        print("{}"*100)
    return outer

@star
@dust
def scan(msg):
    print(msg)
scan("yo whatsup?")
