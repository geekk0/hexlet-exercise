# BEGIN (write your solution here)
print("Введите длину ряда чисел Фиб")
count = int(input())

def fib(count):
    fib1 = 0
    fib2 = 1
    fib_list = [fib1,fib2]
    for i in range (0, count):
        if i == 0: fib_list[i] = 0
        elif i == 1: fib_list[i] = 1
        elif i == 2:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[i-2] + fib_list[i-1])
            
    return fib_list

            
print(fib(count))





