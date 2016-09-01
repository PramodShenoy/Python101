def factorial1(n):
    f = 1
    for i in range(n):
	f *= i+1

    return f


def factorial2(n):
    if n == 0:
	return 1
    return n * factorial2(n-1)



print factorial1(5)
print factorial2(5)
