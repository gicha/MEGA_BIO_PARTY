import time
start = time.perf_counter()
import collections
f = open('test_fa/test2.fasta')
fw = open('D://projects/goto_authumn/test_fa/output_graf_test2.dot', 'w+')
g = {}   #g = { AT: {TG:1, TC:8} }
compl = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
k = 25
str_to_int = {}

while True:
    f.readline()
    line = f.readline().strip()
    f.readline()
    f.readline()
    if line == "":
        break
    reverse_line = ''.join([compl[ch] for ch in line[::-1]])
    #print(reverse_line)
    for i in range(k, len(line)):
        edge = line[i-k:i+1]
        a = line[i-k:i]
        b = line[i-k+1:i+1]
        #print(a,b,edge)
        if a not in g.keys():
            g[a] = {}
            g[a][b] = [edge, 1]
        elif b not in g[a].keys():
            g[a][b] = [edge, 1]
        else:
            g[a][b][1] += 1

    for i in range(k, len(reverse_line)):
        edge = reverse_line[i-k:i+1]
        a = reverse_line[i-k:i]
        b = reverse_line[i-k+1:i+1]
        #print(a, b, edge)
        if a not in g.keys():
            g[a] = {}
            g[a][b] = [edge, 1]
        elif b not in g[a].keys():
            g[a][b] = [edge, 1]
        else:
            g[a][b][1] += 1
gi = {}
for a, v0 in g.items():
    for b, v in v0.items():
        if b not in gi:
            gi[b] = {}
        gi[b][a] = v


# zip
print('====================================')

izmen = 1
while izmen:
    izmen = 0
    g_del = []
    g_del_in = []
    print('---------')
    for a, v0 in g.items():   #a = TG
        if a not in gi:
            continue
        if len(v0) == 1 and len(gi[a]) == 1:
            b, v = list(v0.items())[0]
            ki, vi = list(gi[a].items())[0]
            if ki in gi and b in gi[ki]:
                continue
            izmen += 1

            g[ki][b] = v
            g_del.append([ki, a, b])

            new_edge = g[ki][a][0] + v[0][k:]
            # print(ki, a, b, v[0], v[0][len(v[0]) - 1:len(v[0])], new_edge)
            #print(ki, a, b, v[0], new_edge)
            #print(v[1], v[0], g[ki][b][1], g[ki][a][0])
            g[ki][b][0] = new_edge
            g[ki][b][1] = (v[1]*(len(v[0])-k+1) + g[ki][b][1]*(len(g[ki][a][0])-k+1)) / (len(v[0])-k+1 + len(g[ki][a][0])-k+1)

            print(ki, a, b, new_edge)
            gi[b][ki] = gi[a][ki]
            gi[b][ki][0] = new_edge
            gi[b][ki][1] = (v[1]*(len(v[0])-k+1) + gi[b][ki][1]*(len(gi[b][a][0])-k+1)) / (len(v[0])-k+1 + len(gi[b][a][0])-k+1)
    for a, b, c in g_del:
        if a in g:
            del g[a][b]
        if c in gi:
            del gi[c][b]
        del g[b]
        del gi[b]

# for i in g_del:
#     del g[i[0]][i[1]]
# for i in g_del_in:
#     del gi[i[0]][i[1]]


#print(g['TTTGGTCGAAAAAAAAAGCCCGCAC'])
#print(g)
print(time.perf_counter() - start)
print('digraph G {', file=fw)


for a, v in g.items():
    for b, v1 in v.items():
        # if a not in str_to_int.keys():
        #     str_to_int[a] = len(str_to_int.keys())
        # if b not in str_to_int.keys():
        #     str_to_int[b] = len(str_to_int.keys())
        #print(a,v,b,v1)
        print('\t', a, ' -> ', b, ' [label="', len(v1[0]), '"];', sep='', file=fw)
print('}', file=fw)