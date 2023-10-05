number = 10
if number <=0:
    sum = 0
else:
    list_of_number = []
    list_for_sum = []
    x = 0
    sum = 0
    while x != (number-1):
        x += 1
        list_of_number.append(x)
    for y in list_of_number:
        if y % 3 == 0 or y % 5 == 0:
            list_for_sum.append(y)

    for z in list_for_sum:
        sum += z

print(sum)

