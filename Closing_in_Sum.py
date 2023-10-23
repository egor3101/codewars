"""Create a function that returns the sum of the digits formed from the first and last digits, all the way to the center of the number.

Worked Example
2520 ➞ 72

# The first and last digits are 2 and 0.
# 2 and 0 form 20.
# The second digit is 5 and the second to last digit is 2.
# 5 and 2 form 52.

# 20 + 52 = 72
Examples
121 ➞ 13
# 11 + 2

1039 ➞ 22
# 19 + 3

22225555 ➞ 100
# 25 + 25 + 25 + 25
Notes
If the number has an odd number of digits, simply add on the single-digit number in the center (see example #1).
Any number which is zero-padded counts as a single digit (see example #2)."""


n  = 1213
string_num = str(n)
mapObject = map(int, string_num)
separate_digit_list = list(mapObject)
lenght_start_number = len(separate_digit_list)
total = 0
if lenght_start_number % 2 != 0:
    y = separate_digit_list.pop(lenght_start_number // 2)
    total = y
    lenght_start_number = len(separate_digit_list)


#print(separate_digit_list)

start_count = -1
end_count = 0
i = 1
list_for_summ = []
while i != lenght_start_number/2 + 1:
    start_count += 1
    end_count -= 1
    i += 1

    start_numer = str (separate_digit_list[start_count])
    end_number = str (separate_digit_list[end_count])
    rigt_nubmer = start_numer + end_number
    number_for_summ_1 = int (rigt_nubmer)
    print(number_for_summ_1)

    list_for_summ.append(number_for_summ_1)




for number in list_for_summ:
    total += number


