out = open('sinh/out_rule.txt', 'w')

for i in range(1, 257):
    if i < 39:
        out.write(f"('RU{i}', 0),\n")
    else:
        out.write(f"('RU{i}', 1),\n")