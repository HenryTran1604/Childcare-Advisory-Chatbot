from forward_chaining import ForwardChaining
symp = []
for i in range(5):
    x = int(input("Nhập triệu chứng: "))
    symp.append(f'SY{x}')

fc = ForwardChaining()
print(fc.forward_chaining(symp))


