print("Введите значение начала отрезка")
begin = int(input())
print("Введите значение конца отрезка")
end = int(input())

def fizz_buzz (begin,end):
    fb_str = ''
    for x in range(begin, end+1):
        if x%3 == 0:
            if x%5 == 0:
                fb_str = fb_str + (" ") + ('FizzBuzz')
            fb_str = fb_str + (" ") + ('Fizz')
        elif x%5 == 0:
            fb_str = fb_str + (" ") + ('Buzz')
        else:
            fb_str = fb_str + (" ") + str(x)
    s = " "
    return fb_str
    
print(fizz_buzz(begin,end))