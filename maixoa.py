out = open('out.txt', 'w')
for i in range(1, 213):
    pi = 0 if i < 49 else 1
    out.write(f"('RU{i}', {pi}),\n")