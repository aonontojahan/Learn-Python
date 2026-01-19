n = int(input())

for num in range(1, n + 1):

    if num % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    if num < 2:
        prime_status = "Not Prime"
    else:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_status = "Prime"
        else:
            prime_status = "Not Prime"

    print("Number", num, ":", parity, prime_status)
