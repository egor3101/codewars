"""A twin prime is a prime number that is either 2 less or 2 more than another prime number—for example, either member of the twin prime pair (41, 43). In other words, a twin prime is a prime that has a prime gap of two. Sometimes the term twin prime is used for a pair of twin primes; an alternative name for this is prime twin or prime pair. (from wiki https://en.wikipedia.org/wiki/Twin_prime)

Your mission, should you choose to accept it, is to write a function that counts the number of sets of twin primes from 1 to n.

If n is wrapped by twin primes (n-1 == prime && n+1 == prime) then that should also count even though n+1 is outside the range.

Ex n = 10

Twin Primes are (3,5) (5,7) so your function should return 2!"""

num = 100000
list_with_primal = []

i = 2
x = 0  # индекс первого элемента в списке для сравнения
y = 1  # индекс следующего элемента в списке для сравнения
answer = 0
if num > 3:
    list_with_primal.append(3)
    while i != num + 2:
        out = int(i // 2 + 1)
        for z in range(2, out):
            if i % z == 0:
                pass
                break
            elif z == out - 1:
                list_with_primal.append(i)
        #print(out)
        i += 1
    while x != len(list_with_primal) - 1:
        if list_with_primal[x] + 2 == list_with_primal[y]:
            answer += 1
        x += 1
        y += 1
    print(list_with_primal)

elif num == 3:
    answer = 1
print(answer)


    #print(list_with_primal)


