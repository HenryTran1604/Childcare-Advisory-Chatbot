f = open('sinh\src_tien.txt', 'r')
out = open('sinh\out_tien.txt', 'w')
for i, line in enumerate(f.readlines()):
    s = line.strip().split()
    out.write(f"('SY{s[0][1:]}', '{s[1]}', 'RU{i+1}'),\n")