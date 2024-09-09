degree = 7

start_number = 10 ** degree
answer = 100
# list_for_number = []  # Возможно перенести в if
now_number = 110

# x = 0  # First index
# y = 1  # Second index

if degree >= 3: #if start_number > 109:

    while now_number <= start_number:
        x = 0  # First index
        y = 1  # Second index
        x_2 = 0  # First index
        y_2 = 1  # Second index
        checker = 0

        list_for_number = list(map(int, str(now_number)))  # list with numbers
        #  Оставить только уникальные элементы в списке, а если список состоит из 1 символа, то +1 к ответу

        # Возрастающее
        if list_for_number[y] >= list_for_number[x]:
            while y != len(list_for_number):
                if list_for_number[y] < list_for_number[x]:
                    # now_number += 1  # Increase
                    break  # Можно заменить на переключатель
                x += 1
                y += 1
            else:
                answer += 1
                #now_number += 1  # Increase
                checker = 1
                print(now_number, "Возрастающее")

        # Убывающее
        if (list_for_number[y_2] <= list_for_number[x_2]) and (checker == 0):
            while y_2 != len(list_for_number):
                if list_for_number[y_2] > list_for_number[x_2]:
                    #now_number += 1  # Increase
                    break
                x_2 += 1
                y_2 += 1
            else:
                #now_number += 1  # Increase
                answer += 1
                print(now_number, "Убывающее")
        now_number += 1  # Increase

        print(list_for_number)
    print(answer )

elif degree == 2:
    answer = 100
elif degree == 1:
    answer = 10
elif degree == 0:
    answer = 1

