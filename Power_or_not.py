print("ВВедите положительное целое число ")
num = int(input())


def power_or_not(num):
    n = num / 3
    while n > 1:
        n = n / 3
        if n == 1:
            return True

if power_or_not(num):
    print("yes")
else:
    print("no")
    

