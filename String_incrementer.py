"""Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered."""

# Проблема в том, что при переходе из str в int(переменная int_num) отбрасываются все нули из-за того, что в Python
# число не может начинаться с нуля. Также в коде не написано про то что, если это не первое, а например второе число.

# Не детектит ноль как символ для проверки!


strng = "dad0890898sadsd00101"
invers_strng = strng[::-1]
list_for_strng = list(invers_strng)
str_for_num = ""
for simbols in list_for_strng:
    if simbols.isdigit():
        str_for_num += simbols
    else:
        break

for_plus_one_1 = int(str_for_num[::-1]) + 1
for_plus_one_2 = (str(for_plus_one_1)[::-1])
for_plus_one = int(for_plus_one_2)

for simbols in list_for_strng:
    if simbols.isdigit():
        list_for_strng.remove(simbols)
for x in (str(for_plus_one)[::-1]):
    # list_for_strng.append(x)
    list_for_strng.insert(0, x)

answer = ''.join(list_for_strng[::-1])

print(for_plus_one)
# print(list_for_strng[::-1])
print(answer)
# print(invers_strng)

