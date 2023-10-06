"""Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case"""

n = 1234
binary_num = format(n, 'b')
x = [int(i) for i in str(binary_num)]
counter = 0
for number in x:
    if number == 1:
        counter += 1

print(counter)