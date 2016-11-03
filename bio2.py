import time
start = time.perf_counter()
import collections
f = open('outputv2.txt')
f1 = open('ighv.fa.txt')
#f2 = open('D://projects/goto_authumn/output2.txt', 'w+')
gen = []
ar_count_mismatches_coord = []
for i in range(6):
    f1.readline()
    strr = ''
    for j in range(5):
        strr += f1.readline().strip()
    gen.append(strr)
gen_mis_count = []
for i in range(6):
    gen_mis_count.append([collections.Counter() for i in range(6)])

print(gen[0])
while True:
    f.readline()
    line = f.readline()
    line = line.split("\n")[0]
    if line == "":
        break

    gl_mis = []
    mis = [collections.Counter() for i in range(6)]  #[gen[ [i,j] ] ]
    c = -1
    mis_m = [0,0,0,0,0,0]
    for n_gen in gen:
        c+=1
        max_sovp = [0, 0, 0]
        m = [[[0] * 3 for i in range(len(line))] for j in range(len(n_gen))]  # [ [ [ x, ip, jp ] ] ]

        for i in range(1, len(line)):
            for j in range(1, len(n_gen)):
                maxx = 0
                if line[i - 1] == n_gen[j - 1]:
                    maxx = m[i - 1][j - 1][0] + 1
                    m[i][j][0] = maxx
                    m[i][j][1] = i - 1
                    m[i][j][2] = j - 1
                else:
                    maxx = m[i - 1][j - 1][0] - 1
                    if maxx >= 0:
                        m[i][j][0] = maxx
                        m[i][j][1] = i - 1
                        m[i][j][2] = j - 1
                        mis[j]+=1
                        mis_m[c]+=1
                        #print(i,j,mis_m)

                if m[i - 1][j][0] - 1 > maxx:
                    maxx = m[i - 1][j][0] - 1
                    if maxx >= 0:
                        m[i][j][0] = maxx
                        m[i][j][1] = i - 1
                        m[i][j][2] = j

                if m[i][j - 1][0] - 1 > maxx:
                    maxx = m[i - 1][j][0] - 1
                    if maxx >= 0:
                        m[i][j][0] = maxx
                        m[i][j][1] = i
                        m[i][j][2] = j - 1
                if maxx >= max_sovp[0]:
                    max_sovp[0] = maxx
                    max_sovp[1] = i
                    max_sovp[2] = j
        gl_mis.append(mis)

    max = [0, 0]
    for i in range(6):
        if mis_m[i] > max[0]:
            max = [mis_m[i], i]

    max_gen = mis_m[max[1]]
    for k,v in gl_mis[max_gen].items():
        gen_mis_count[k] = v;

import numpy as N
import matplotlib.pyplot as P
k,v = gen_mis_count[0].items()
P.hist(v, bins=10)
P.show()


#f2.close()

print(time.perf_counter() - start)