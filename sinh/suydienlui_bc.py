import re
f = open('sinh/src_lui.txt', 'r')
out = open('sinh/out_lui_bc.txt', 'w')

cnt1, cnt2 = 65, 39

for line in f.readlines():
    tmp = []
    s = re.split(r',|\t', line.strip())
    for i in range(len(s) - 1):
        x = s[i].strip()
        if x.isnumeric():
            x = 'SY' + x
        if x[0] == 'S' and x[1].isnumeric() and len(x) == 3:
            x = 'SY' + x[1:]
        tmp.append(x)
    out.write(f"{' + '.join(tmp)} -> {s[-1]}\n")
    cnt2 += 1