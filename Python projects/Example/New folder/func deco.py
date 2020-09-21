def brain(sucks):
    def neuron(a,b):
        print("divding on process",a,"and",b)
        if b == 0:
            print("whoops! i really suck cant divide")
            return
        return sucks(a,b)
    return neuron

@brain
def div(a,b):
    return a/b
