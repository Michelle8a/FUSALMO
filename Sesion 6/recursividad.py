#Factorial
def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f


def factorial_recur(x):
    if x == 0:
        return 1
    else:
        return x * factorial_recur(x-1)

'''
factorial_recursivo(4)
= 4 * factorial_recursivo(3)
= 4 * (3 * factorial_recursivo(2))
= 4 * (3 * (2 * factorial_recursivo(1)))
= 4 * (3 * (2 * (1 * factorial_recursivo(0))))
= 4 * (3 * (2 * (1 * 1)))     # porque factorial_recursivo(0) devuelve 1
= 4 * (3 * (2 * 1))
= 4 * (3 * 2)
= 4 * 6
= 24

'''




def fact(x):
    return 1 if x == 0 else x * fact(x - 1)


n = 5

print(factorial(n))
print(factorial_recur(n))
print(fact(n))

