import re
f = open('tmp.txt', 'r')
out = open('out.txt', 'w')
def convert(s):
    try:
        tmp = int(s[-2:0])
        print(tmp)
        return s
    except:
        return s[:-1] + '0' + s[-1]
cnt1, cnt2 = 65, 86
for line in f.readlines():
    s = re.split(r',|\t', line.strip())
    print(s)
    for i in range(len(s) - 1):
        x = s[i].strip()
        out.write(f"('{x.strip()}', '{s[-1].strip()}', 'RU{cnt2}'),\n")
        cnt1 += 1
    cnt2 += 1

#f = open('inference.txt')
#out = open('out.txt', 'w')
#i = 1
#for line in f.readlines():
#    s = line.strip().split()
#    print(s[0])
#    out.write(f"('{s[0][0]}Y{s[0][1:]}', '{s[1]}', 'RU{i}'),\n")
#    i += 1
