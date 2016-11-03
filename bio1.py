import time

f = open('1.fq.txt')
f1 = open('2.fq.txt')
f2 = open('D://projects/goto_authumn/output.txt', 'w+')

compl = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
while True:
    max_sovp = [0, 0, 0]
    start = time.perf_counter()
    m = [[[0] * 4 for i in range(300)] for j in range(300)]  # [ [ [ x, ip, jp ] ] ]
    name = f.readline()
    line = f.readline()
    line = line.split("\n")[0]
    # line = 'AAAATTCCCCGGG' ##
    f.readline()
    qual1 = f.readline()
    if line == "":
        break
    f1.readline()
    reverse_line = f1.readline()
    # reverse_line = 'GGCCCAAAAACCC'
    start_reverse_line = reverse_line
    reverse_line = reverse_line.split("\n")[0]
    f1.readline()
    qual2 = f1.readline()[::-1]
    reverse_line = ''.join([compl[ch] for ch in reverse_line[::-1]])
    for i in range(1, len(line)):
        for j in range(1, len(reverse_line)):
            maxx = 0
            if line[i - 1] == reverse_line[j - 1]:
                maxx = m[i - 1][j - 1][0] + 1
                m[i][j][0] = maxx
                m[i][j][1] = i - 1
                m[i][j][2] = j - 1
                m[i][j][3] = False  # is_mis
            else:
                maxx = m[i - 1][j - 1][0] - 1
                if maxx >= 0:
                    m[i][j][0] = maxx
                    m[i][j][1] = i - 1
                    m[i][j][2] = j - 1
                    m[i][j][3] = True

            if m[i - 1][j][0] - 1 > maxx:
                maxx = m[i - 1][j][0] - 1
                if maxx >= 0:
                    m[i][j][0] = maxx
                    m[i][j][1] = i - 1
                    m[i][j][2] = j
                    m[i][j][3] = False

            if m[i][j - 1][0] - 1 > maxx:
                maxx = m[i - 1][j][0] - 1
                if maxx >= 0:
                    m[i][j][0] = maxx
                    m[i][j][1] = i
                    m[i][j][2] = j - 1
                    m[i][j][3] = False
            if maxx >= max_sovp[0]:
                max_sovp[0] = maxx
                max_sovp[1] = i
                max_sovp[2] = j

    # print(time.perf_counter() - start)

    i = max_sovp[1]
    j = max_sovp[2]
    rl_list = []
    while (m[i][j][0] != 0):
        i = m[i][j][1]
        j = m[i][j][2]
        if m[i][j][3]:
            if qual1[i] > qual2[j]:
                rl_list.append(line[i])
            else:
                rl_list.append(reverse_line[j])
        else:
            rl_list.append(line[i])

    # print(i,j, max_sovp, j+1, len(reverse_line), mis_i_coor)

    min_sovp = [i, j]
    end_line = line[:i]
    end_line += ''.join(rl_list)
    end_line += reverse_line[j + 1 + len(rl_list):]
    # print(len(line), len(reverse_line))


    # end_line = ''.join(list_end_line)
    # print(min_sovp, max_sovp, i,j, end_line)
    print(name.replace('300', str(len(end_line))), '\n', end_line, '\n', file=f2)

f2.close()
