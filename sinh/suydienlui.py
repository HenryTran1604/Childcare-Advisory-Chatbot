import re
f = open('sinh/src_lui.txt', 'r')
out = open('sinh/out_lui.txt', 'w')

cnt1, cnt2 = 65, 1
for pos, line in enumerate(f.readlines()):
    s = re.split(r',|\t', line.strip())
    print(s)
    for i in range(len(s) - 1):
        x = s[i].strip()
        if x.isnumeric():
            x = 'SY' + x
        if x[0] == 'S' and x[1].isnumeric() and len(x) <= 3:
            x = 'SY' + x[1:]
        out.write(f"('{x}', '{s[-1].strip()}', 'RU{cnt2}'),\n")
    cnt2 += 1