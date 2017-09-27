def hamming(a,b):
    m = []
    for i in range(0,len(a)):
        m.append(ord(a[i])^ord(b[i]))

    t = ''.join(bin(i).replace('0b','') for i in m)
    n = 0
    for i in t:
        if i == '1':
            n = n+1
    print n
