out = open('sinh/out_rule.txt', 'w')

for i in range(1, 186):
    if i < 40:
        out.write(f"('RU{i}', 0),\n")
    else:
        out.write(f"('RU{i}', 1),\n")