f = open('sinh/tmp.txt', 'r', encoding='utf8')
o = open('sinh/tmp1.txt', 'w', encoding='utf8')
for i, line in enumerate(f.readlines()):
    s = line.strip().split(",")
    o.write(f"('A{i+1}', '{line.strip()}'),\n")