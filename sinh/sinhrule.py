out = open('sinh/out_rule.txt', 'w')

for i in range(1, 228):
    if i < 112:
        out.write(f"('RU{i}', 0),\n")
    else:
        out.write(f"('RU{i}', 1),\n")