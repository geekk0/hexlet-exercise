type(a)=int
    type(b)=int
     c = a+b
     d = a*b
     e = a/b
     f = a-b
if a == b :
    print ("Ввведите разные числа")
    sys.exit()
elif a<1 or b<1 : 
    print ("Числа от 1")
    sys.exit()
elif a>10 or b>10 :
    print ("Числа до 10")
    sys.exit()
else :
    print ("Введите желаемое арифметическое действие")
    action = str(input());
if  action == 'сложение':
    print("Результат :",c)
elif action == 'умножение':
    print("Результат :",d)
elif action == 'деление':
    print("Результат :",e)
elif action == 'вычитание':
    print("Результат :",f)
else :
    print("Корректно введите действие")
    sys.exit()