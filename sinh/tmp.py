f = open('sinh/tmp.txt', 'r')
for i, line in enumerate(f.readlines()):
    s = line.strip().split(",")
    print(f'({1 if i < 25 else 0}, {", ".join(s)}),')