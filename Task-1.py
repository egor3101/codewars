n = 1234
binary_num = format(n, 'b')
x = [int(i) for i in str(binary_num)]
counter = 0
for number in x:
    if number == 1:
        counter += 1

print(counter)