"""        The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return

[F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(n) being the smallest one such as F(n) * F(n+1) > prod.

Some Examples of Return:
(depend on the language)

productFib(714) # should return (21, 34, true),
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return (34, 55, false),
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
-----
productFib(714) # should return [21, 34, true],
productFib(800) # should return [34, 55, false],
-----
productFib(714) # should return {21, 34, 1},
productFib(800) # should return {34, 55, 0},
-----
productFib(714) # should return {21, 34, true},
productFib(800) # should return {34, 55, false},
Note:
You can see examples for your language in "Sample Tests"."""
def productFib(prod):
    fib_sequence = [1]
    check_prod = 1
    first_nuber_for_sum = 0
    next_number_for_sum = 1
    first_nuber_for_multiplicatiom = 0
    next_nuber_for_multiplicatiom = 1
    sum = 0
    multiplication = 0
    check_true = False
    answer = []
    if prod == 1:
        check_true = True
        answer = [1, 1, check_true]
    elif prod == 0:
        check_true = True
        answer = [0, 1, check_true]

    else:
        while check_prod <= prod:  # or only <
            fib_sequence.append(check_prod)
            sum = fib_sequence[first_nuber_for_sum] + fib_sequence[next_number_for_sum]
            check_prod = sum
            first_nuber_for_sum += 1
            next_number_for_sum += 1
            # print(fib_sequence)
        length = len(fib_sequence)
        while next_nuber_for_multiplicatiom != length:
            multiplication = fib_sequence[first_nuber_for_multiplicatiom] * fib_sequence[next_nuber_for_multiplicatiom]
            # print(multiplication)
            if multiplication == prod:
                check_true = True
                answer.append(fib_sequence[first_nuber_for_multiplicatiom])
                answer.append(fib_sequence[next_nuber_for_multiplicatiom])
                answer.append(check_true)
                break
            elif multiplication > prod:
                answer.append(fib_sequence[first_nuber_for_multiplicatiom])
                answer.append(fib_sequence[next_nuber_for_multiplicatiom])
                answer.append(check_true)

                break

            else:
                first_nuber_for_multiplicatiom += 1
                next_nuber_for_multiplicatiom += 1

    return answer
print(productFib(714))
