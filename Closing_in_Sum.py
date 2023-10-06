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


