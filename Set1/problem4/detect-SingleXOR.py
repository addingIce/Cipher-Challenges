

f = open('SingleXOR.txt')
s = []
line = f.readline()
while(line):
    line = f.readline()
    s.append(line[:len(line)-1])
f.close()


for m in s:
    if len(m)<60:
        continue
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
