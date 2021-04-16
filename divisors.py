def divisor(a):
    for i in range(1, int(a / 2) + 1):
        if a % i == 0:
            print(i)
    print(a)


a = int(input("Find the divisors of: "))

divisor(a)