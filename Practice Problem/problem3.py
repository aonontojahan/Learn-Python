result = int(input("Enter a number to check if it's prime or not: "))
if result > 1:
    for i in range(2, int(result/2)+1):
        if (result % i) == 0:
            print("{0} is not a prime number".format(result))
            break
    else:
        print("{0} is a prime number".format(result))