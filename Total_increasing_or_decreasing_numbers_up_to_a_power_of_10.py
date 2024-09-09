"""Let's define increasing numbers as the numbers whose digits, read from left to right, are never less than the previous ones: 234559 is an example of increasing number.

Conversely, decreasing numbers have all the digits read from left to right so that no digits is bigger than the previous one: 97732 is an example of decreasing number.

You do not need to be the next Gauss to figure that all numbers with 1 or 2 digits are either increasing or decreasing: 00, 01, 02, ..., 98, 99 are all belonging to one of this categories (if not both, like 22 or 55): 101 is indeed the first number which does NOT fall into either of the categories. Same goes for all the numbers up to 109, while 110 is again a decreasing number.

Now your task is rather easy to declare (a bit less to perform): you have to build a function to return the total occurrences of all the increasing or decreasing numbers below 10 raised to the xth power (x will always be >= 0).

To give you a starting point, there are a grand total of increasing and decreasing numbers as shown in the table:

Total	Below
1	    1
10	    10
100	    100
475	    1000
1675	10000
4954	100000
12952	1000000
This means that your function will have to behave like this:

total_inc_dec(0)==1
total_inc_dec(1)==10
total_inc_dec(2)==100
total_inc_dec(3)==475
total_inc_dec(4)==1675
total_inc_dec(5)==4954
total_inc_dec(6)==12952
Tips: efficiency and trying to figure out how it works are essential: with a brute force approach, some tests with larger numbers may take more than the total computing power currently on Earth to be finished in the short allotted time.

To make it even clearer, the increasing or decreasing numbers between in the range 101-200 are: [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 122, 123, 124, 125, 126, 127, 128, 129, 133, 134, 135, 136, 137, 138, 139, 144, 145, 146, 147, 148, 149, 155, 156, 157, 158, 159, 166, 167, 168, 169, 177, 178, 179, 188, 189, 199, 200], that is 47 of them. In the following range, 201-300, there are 41 of them and so on, getting rarer and rarer.

Trivia: just for the sake of your own curiosity, a number which is neither decreasing of increasing is called a bouncy number, like, say, 3848 or 37294; also, usually 0 is not considered being increasing, decreasing or bouncy, but it will be for the purpose of this kata"""

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

