m = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
m = m.decode('hex')
for i in range(65,100):
    t = ''
    flag = 1
    for j in range(0,len(m)):
        temp = i^ord(m[j])
        if 32<=temp<=122:
            t = t+chr(temp)
            continue
        else:
            flag = 0
            break
    if flag == 1:
        print t
for i in range(97,123):
    t = ''
    for j in range(0,len(m)):
        temp = i^ord(m[j])
        if 32<=temp<=122:
            t = t+chr(temp)
            continue
        else:
            flag = 0
            break
    if flag == 1:
        print t
