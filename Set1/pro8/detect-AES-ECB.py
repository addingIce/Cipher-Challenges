
f = open('ECBciphertext.txt')
s = []
line = f.readline()
while(line):
    line = f.readline()
    s.append(line[0:len(line)-1])
f.close()


for m in s:
    if len(m)%2 != 0:
        continue
    t = []
    for i in range(0,len(m)-len(m)/32):
        t.append(m[i:i+32])
        i = i+32
    for j in t:
        if t.count(j) > 1:
            print '-----'+m
            break
