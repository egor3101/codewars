"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once."""


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

