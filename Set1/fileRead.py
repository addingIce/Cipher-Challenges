 f = open('ciphertext.txt')
 s = []
 line = f.readline()
 while(line):
     line = f.readline()
     s.append(line)
 f.close()
