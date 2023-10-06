lst = [3, 1, 4, 1, 5, 9, 2, 6]
now_thee = 0
now_thee_for_rev = 0
new_lst = []
new_lst_for_reverse = []
reverse_list = lst[::-1]
for number in lst:
    if number > now_thee:
        new_lst.append(number)
        now_thee = number
for numberrev in reverse_list:
    if numberrev> now_thee_for_rev:
        new_lst_for_reverse.append(numberrev)
        now_thee_for_rev = numberrev
if len(new_lst)>len(new_lst_for_reverse):
    print("left")
else:
    print("right")
print("left", len(new_lst))
print("right", len(new_lst_for_reverse))
