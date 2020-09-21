a = 65534
b = 65535
c =  65536
d = 2998302

with open("Binary2",'bw') as bin_file:
    bin_file.write(a.to_bytes(2,'big'))
    bin_file.write(b.to_bytes(2,'big'))
    bin_file.write(b.to_bytes(4, 'big'))
    bin_file.write(b.to_bytes(4, 'big'))
    bin_file.write(b.to_bytes(4, 'little'))

with open('binary2','br')as binFile:
    e = int.from_bytes(binFile.read(2),'big')
    print(e)
    f = int.from_bytes(binFile.read(2), 'big')
    print(f)
    g = int.from_bytes(binFile.read(4), 'big')

    h = int.from_bytes(binFile(4), 'big')
    i = int.from_bytes(binFile(4), 'big')
